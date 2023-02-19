from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session, jsonify
import sqlite3

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
    
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
        cursor = myConnection.cursor()
    
        cursor.execute('SELECT day_id, day_description FROM tbDays')
        days = cursor.fetchall()
        
        cursor.execute('SELECT task_id, task_description, task_status, day_id FROM tbTasks')
        tasks = cursor.fetchall()
        
        tasks_by_day = {day[0]: [] for day in days}
        for task in tasks:
            tasks_by_day[task[3]].append((task[0], task[1], task[2]))
            
            
    task_count = task_done_undone()
    task_per_day_count = task_per_day()
        
    return render_template('index.html', days=days, tasks=tasks, tasks_by_day=tasks_by_day, task_count=task_count,task_per_day_count=task_per_day_count)



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
    
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
        cursor = myConnection.cursor()
    
        task_description = request.form['task_description']
        day_id = request.form['day_id']
        
        last_id = cursor.execute('SELECT MAX(task_id) FROM tbTasks').fetchone()[0]
        if last_id is None:
            last_id = 0
        
        cursor.execute('INSERT INTO tbTasks VALUES (?, ?, ?, ?)', (last_id + 1, task_description, 0, day_id))
        myConnection.commit()
    
        return redirect(url_for('index'))

@app.route('/task_status', methods=['POST'])
def task_status():
    
    # Make the database connection and cursor object
    # Get the id from the request body
    # If task is undone(0) set it as done. Otherwise, if the task is done(1) set it as undone.
    # Update task status using the id
    # Redirect to the home page
    
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
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
    
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
        cursor = myConnection.cursor()
        
        taskId = request.get_data(as_text=True)
        cursor.execute('DELETE FROM tbTasks WHERE task_id == ?', (taskId,))
        
        return redirect(url_for('index'))
    
@app.route('/task_per_day', methods=['POST'])
def task_per_day():
    
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are assigned to each day of the week
    
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
        cursor = myConnection.cursor()
        
        cursor.execute('SELECT day_id FROM tbTasks')
        tasks = cursor.fetchall()
        
        def count_tasks(tasks):
            monday = 0
            tuesday = 0
            wednesday = 0
            thursday = 0
            friday = 0
            saturday = 0
            sunday = 0
            
            for task in tasks:
                if task[0] == 1:
                    monday += 1
                elif task[0] == 2:
                    tuesday += 1
                elif task[0] == 3:
                    wednesday += 1
                elif task[0] == 4:
                    thursday += 1
                elif task[0] == 5:
                    friday += 1
                elif task[0] == 6:
                    saturday += 1
                elif task[0] == 7:
                    sunday += 1
                    
                    
            return [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

        task_per_day_count = count_tasks(tasks)
        
    return task_per_day_count
    
@app.route('/task_done_undone', methods=['POST'])
def task_done_undone():
    
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are done and how many are undone
    
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
        cursor = myConnection.cursor()
        
        cursor.execute('SELECT task_status FROM tbTasks')
        tasks = cursor.fetchall()
        
        def count_tasks(tasks):
            done_count = 0
            undone_count = 0
            for task in tasks:
                if task[0] == 1:
                    done_count += 1
                elif task[0] == 0:
                    undone_count += 1
            return [done_count, undone_count]

        task_count = count_tasks(tasks)
        
    return task_count

#####################################################
#               LOGIN AND SIGNUP
#####################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
            
    return render_template('login.html')

@app.route('/submit_login', methods=['GET', 'POST'])
def submit_login():
    # Make the database connection and cursor object
    with sqlite3.connect("../db/src/database/mydb.sqlite3") as myConnection:
        cursor = myConnection.cursor()
        
        username = request.form['login-username']
        password = request.form['login-password']
        cursor.execute("SELECT * FROM tbUsers WHERE user_username = ? AND user_password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            # set user_id as session variable
            session['user_id'] = user[0]
            return jsonify({'success': True})
        else:
            flash('Invalid username or password', 'error')
            return jsonify({'success': False})



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    
    