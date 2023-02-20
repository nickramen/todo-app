from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, jsonify
import sqlite3
from src.database import create_connection
from src.graphs import task_per_day, task_done_undone, admin_task_done_undone, admin_task_per_day, admin_overview_task_total,admin_overview_user_total,admin_overview_category_total, admin_task_per_category

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'your_secret_key_here'

# Route for serving static files
@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('assets', path)

@app.route('/index', methods=['GET'])
def index():
    # Make the database connection and cursor object
    # Fetch all the days and tasks from the database
    # Create a dictionary that maps each day ID to a list of tasks
    # Pass the days and tasks, along with the dictionary to the HTML template
    # Load data for the graphs by calling the method: task_done_undone()
    
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
            
            cursor.execute('SELECT task_id, task_description, task_status, day_id FROM tbTasks WHERE user_id == ?',(user_id,))
            tasks = cursor.fetchall()

            tasks_by_day = {day[0]: [] for day in days}
            for task in tasks:
                tasks_by_day[task[3]].append((task[0], task[1], task[2]))
                
                
        task_count = task_done_undone()
        task_per_day_count = task_per_day()
            
        return render_template('index.html', days=days, categories=categories, tasks=tasks, tasks_by_day=tasks_by_day,task_count=task_count,task_per_day_count=task_per_day_count, user_id=user_id,user_username=user_username)
    
    
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
        categories = admin_task_per_category_count[0]
        task_per_category = admin_task_per_category_count[1]
        
    return render_template('admin.html', admin_per_day_count=admin_per_day_count,admin_task_count=admin_task_count,admin_task_total=admin_task_total,admin_user_total=admin_user_total,admin_category_total=admin_category_total,categories=categories,task_per_category=task_per_category)


#####################################################
#                   TASK ACTIONS
#####################################################


@app.route('/add_task', methods=['POST'])
def add_task():
    # Make the database connection and cursor object
    # Get the task description and day ID from the form
    # Get the last task ID from the database
    # Insert the new task into the database with status set as undone (0)
    # Redirect to the home page
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
    
        task_description = request.form['task_description']
        day_id = request.form['day_id']
        cat_id = request.form['cat_id']
        user_id = request.form['user_id']
        
        last_id = cursor.execute('SELECT MAX(task_id) FROM tbTasks').fetchone()[0]
        if last_id is None:
            last_id = 0
        
        cursor.execute('INSERT INTO tbTasks VALUES (?, ?, ?, ?, ?, ?)', (last_id + 1, task_description, 0, day_id, cat_id, user_id))
        myConnection.commit()
    return jsonify({'success': True})


@app.route('/task_status', methods=['POST'])
def task_status():
    
    # Make the database connection and cursor object
    # Get the id from the request body
    # If task is undone(0) set it as done. Otherwise, if the task is done(1) set it as undone.
    # Update task status using the id
    # Redirect to the home page
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
    
        taskId = request.get_data(as_text=True)
        taskStatus = cursor.execute('SELECT task_status FROM tbTasks WHERE task_id == ?', (taskId,)).fetchone()[0]
        
        if(taskStatus == 1):
            cursor.execute('UPDATE tbTasks SET task_status = ? WHERE task_id = ?', (0, taskId))
            myConnection.commit()
        elif(taskStatus == 0):
            cursor.execute('UPDATE tbTasks SET task_status = ? WHERE task_id = ?', (1, taskId))
            myConnection.commit()
        else:
            return "Failed on updating task status"
    
        return redirect(url_for('index'))


@app.route('/delete_task', methods=['POST'])
def delete_task():
    
    # Make the database connection and cursor object
    # Get the id from the request body
    # Delete task status using the id
    # Redirect to the home page
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        taskId = request.get_data(as_text=True)
        cursor.execute('DELETE FROM tbTasks WHERE task_id == ?', (taskId,))
        
        return jsonify({'success': True})


#####################################################
#               LOGIN AND SIGNUP
#####################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
            
    return render_template('login.html')


@app.route('/submit_login', methods=['GET', 'POST'])
def submit_login():
    # Make the database connection and cursor object
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        username = request.form['login-username']
        password = request.form['login-password']
        cursor.execute("SELECT user_id, user_username, rol_id FROM tbUsers WHERE user_username = ? AND user_password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            # set user_id as session variable
            session['user_id'] = user[0]
            session['user_username'] = user[1]
            session['rol_id'] = user[2]
            return jsonify({'success': True, 'rol_id': user[2]})
        else:
            return jsonify({'success': False})


@app.route('/submit_signup', methods=['GET', 'POST'])
def submit_signup():
    
    # Make the database connection and cursor object
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
                # insert new user into tbUsers with default status and rol_id
                cursor.execute("INSERT INTO tbUsers (user_username, user_email, user_password, user_status, rol_id) VALUES (?, ?, ?, ?, ?)", (username, email, password, 1, 2))
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    
    