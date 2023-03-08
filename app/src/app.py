import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify
import sqlite3
from src.database import create_connection
from src.graphs import task_per_day, task_done_undone, admin_task_done_undone, admin_task_per_day, admin_overview_task_total,admin_overview_user_total,admin_overview_category_total, admin_task_per_category, user_satisfaction, admin_overview_user_satisfaction,task_per_category_count,admin_user_active_inactive
from src.users import users_list
import json

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'your_secret_key_here'

# Route for serving static files
@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('assets', path)

# DASHBOARDS

# Load index template, Render data to template, Load data for the graphs
@app.route('/index', methods=['GET'])
def index():
    
    user_id = session.get('user_id')
    user_username = session.get('user_username')
    
    if 'user_username' not in session:
        response_data = {'message': 'No active sessions. Please log in.'}
        return redirect(url_for('login', message=response_data['message']))
    
    else:
        with create_connection() as myConnection:
            cursor = myConnection.cursor()
            cursor.execute('SELECT day_id, day_description FROM tbDays')
            days = cursor.fetchall()
            cursor.execute('SELECT cat_id, cat_description FROM tbCategories')
            categories = cursor.fetchall()
            cursor.execute('SELECT task_id, task_description, task_status, day_id FROM tbTasks WHERE user_id == ? AND is_deleted == 0',(user_id,))
            tasks = cursor.fetchall()
            tasks_by_day = {day[0]: [] for day in days}
            for task in tasks:
                tasks_by_day[task[3]].append((task[0], task[1], task[2]))
                
        task_count = task_done_undone()
        task_per_day_count = task_per_day()
        satisfaction_rate = user_satisfaction()
        task_categories = task_per_category_count()[0]
        tasks_per_category = task_per_category_count()[1]
            
        return render_template('index.html', days=days, categories=categories, tasks=tasks, tasks_by_day=tasks_by_day,task_count=task_count,task_per_day_count=task_per_day_count, user_id=user_id,user_username=user_username,satisfaction_rate=satisfaction_rate,task_categories=task_categories,tasks_per_category=tasks_per_category)

# Load admin template, Render data to template, Load data for the graphs
@app.route('/admin', methods=['GET'])
def admin():
    
    if 'user_username' not in session:
        response_data = {'message': 'No active sessions. Please log in.'}
        return redirect(url_for('login', message=response_data['message']))
    elif 'rol_id' in session and session['rol_id'] == 2:
        response_data = {'message': 'Sorry, you do not have permission to see this page.'}
        
        return redirect(url_for('index', message=response_data['message']))
    else:
        admin_task_count =  admin_task_done_undone()
        admin_per_day_count = admin_task_per_day()
        admin_task_total = admin_overview_task_total()
        admin_user_total = admin_overview_user_total()
        admin_category_total = admin_overview_category_total()
        admin_task_per_category_count = admin_task_per_category()
        admin_user_satisfaction = admin_overview_user_satisfaction()
        categories = admin_task_per_category_count[0]
        task_per_category = admin_task_per_category_count[1]
        active_inactive_users = admin_user_active_inactive()
        
    return render_template('admin.html', admin_per_day_count=admin_per_day_count,admin_task_count=admin_task_count,admin_task_total=admin_task_total,admin_user_total=admin_user_total,admin_category_total=admin_category_total,categories=categories,task_per_category=task_per_category,admin_user_satisfaction=admin_user_satisfaction,active_inactive_users=active_inactive_users)


@app.route('/users', methods=['GET'])
def users():
        
    return render_template('users.html')
    

@app.route('/users_list', methods=['GET'])
def users_list():
    
    with create_connection() as myConnection:
        
        try:
            cursor = myConnection.cursor()
            users = cursor.execute("SELECT user_id, user_username, user_email, user_status FROM tbUsers").fetchall()
            return users
        except:
            return jsonify({'success': False})



# TASK ACTIONS

# Get the task description and day ID from the form, Get the last task ID from 
# the database for the new id, Insert the new task into the db with status set as undone (0)
@app.route('/add_task', methods=['POST'])
def add_task():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
    
        task_description = request.form['task_description']
        day_id = request.form['day_id']
        cat_id = request.form['cat_id']
        user_id = request.form['user_id']
        current_time = datetime.datetime.now()
        
        last_id = cursor.execute('SELECT MAX(task_id) FROM tbTasks').fetchone()[0]
        if last_id is None:
            last_id = 0
        
        try:
            cursor.execute('INSERT INTO tbTasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (last_id + 1, task_description, 0, day_id, cat_id, user_id, current_time, '', 0))
            myConnection.commit()
            return jsonify({'success': True})
        except:
            return jsonify({'success': False})

# Get the id from the request body, If task is undone(0) set it as done. Otherwise, 
# if the task is done(1) set it as undone. Update task status using the id
@app.route('/task_status', methods=['POST'])
def task_status():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
    
        taskId = request.get_data(as_text=True)
        current_time = datetime.datetime.now()
        
        taskStatus = cursor.execute('SELECT task_status FROM tbTasks WHERE task_id = ?', (taskId,)).fetchone()[0]
        
        if(taskStatus == 1):
            cursor.execute('UPDATE tbTasks SET task_status = ?, edit_date = ? WHERE task_id = ?', (0, current_time, taskId))
            myConnection.commit()
            # Get the updated task count data
            cursor.execute('SELECT COUNT(*) FROM tbTasks WHERE task_status = ?', (1,))
            tasks_done = cursor.fetchone()[0]
            cursor.execute('SELECT COUNT(*) FROM tbTasks WHERE task_status = ?', (0,))
            tasks_undone = cursor.fetchone()[0]
            task_count = [tasks_done, tasks_undone]
            return jsonify({'success': True, 'task_count': task_count})
        
        elif(taskStatus == 0):
            cursor.execute('UPDATE tbTasks SET task_status = ?, edit_date = ? WHERE task_id = ?', (1, current_time, taskId))
            myConnection.commit()
            # Get the updated task count data
            cursor.execute('SELECT COUNT(*) FROM tbTasks WHERE task_status = ?', (1,))
            tasks_done = cursor.fetchone()[0]
            cursor.execute('SELECT COUNT(*) FROM tbTasks WHERE task_status = ?', (0,))
            tasks_undone = cursor.fetchone()[0]
            task_count = [tasks_done, tasks_undone]
            return jsonify({'success': True, 'task_count': task_count})
        else:
            return jsonify({'success': False})

# Get the id from the request body and Delete task status using the id
@app.route('/delete_task', methods=['POST'])
def delete_task():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        taskId = request.get_data(as_text=True)
        try:
            #cursor.execute('DELETE FROM tbTasks WHERE task_id == ?', (taskId,))
            cursor.execute('UPDATE tbTasks SET is_deleted = 1 WHERE task_id = ?',(taskId,))
            return jsonify({'success': True})
        except:
            return jsonify({'success': False})
    
# Update task description
@app.route('/update_task', methods=['POST'])
def update_task():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        data = request.get_data(as_text=True)
        data_dict = json.loads(data)
        task_id = data_dict.get('taskId')
        new_description = data_dict.get('newDescription')
        current_time = datetime.datetime.now()
        
        try:
            cursor.execute('UPDATE tbTasks SET task_description = ?, edit_date = ? WHERE task_id = ?', (new_description,current_time,task_id))
            myConnection.commit()
            return jsonify({'success': True})
        except:
            return jsonify({'success': False})

# LOGIN AND SIGNUP
@app.route('/login', methods=['GET', 'POST'])
def login():
            
    return render_template('login.html')

# Log into the account and create user sessions
@app.route('/submit_login', methods=['GET', 'POST'])
def submit_login():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        username = request.form['login-username']
        password = request.form['login-password']
        cursor.execute("SELECT user_id, user_username, rol_id FROM tbUsers WHERE user_username = ? AND user_password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            session['user_username'] = user[1]
            session['rol_id'] = user[2]
            return jsonify({'success': True, 'rol_id': user[2]})
        else:
            return jsonify({'success': False})

# Signup to the app, creates a new user account
@app.route('/submit_signup', methods=['GET', 'POST'])
def submit_signup():

    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        username = request.form['signup-username']
        email = request.form['signup-email']
        password = request.form['signup-password']
        confirm_password = request.form['signup-confirm-password']
        
        if password != confirm_password:
            return jsonify({'success': False})
        else:
            try:
                # insert new user into tbUsers with default status(1=active) and rol_id (2=user)
                cursor.execute("INSERT INTO tbUsers (user_username, user_email, user_password, user_status, rol_id) VALUES (?, ?, ?, ?, ?, ?)", (username, email, password, 1, 2, 0))
                myConnection.commit()
                return jsonify({'success': True})
            except:
                return jsonify({'success': False})


@app.route('/submit_logout', methods=['POST'])
def submit_logout():
    
    try:
        session.pop('user_id', None)
        session.pop('user_username', None)
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

# Let users rate their satisfaction with the app, 1-5 star survey, when user account is created user satisfaction is set to 0, then they can update it from 1-5
@app.route('/update_satisfaction_rate', methods=['POST'])
def update_satisfaction_rate():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        user_id = session.get('user_id')
        userRate = request.get_data(as_text=True)
        
        try:
            cursor.execute('UPDATE tbUsers SET user_satisfaction = ? WHERE user_id = ?',(userRate,user_id))
            myConnection.commit()
            return jsonify({'success': True})
        except:
            return jsonify({'success': False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
