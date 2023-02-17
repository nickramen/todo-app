from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__,template_folder='template')

@app.route('/index', methods=['GET'])
def index():
    # make the database connection and cursor object
    myConnection = sqlite3.connect("../db/src/database/mydb.sqlite3")
    cursor = myConnection.cursor()
    
    # Fetch all the days and tasks from the database
    cursor.execute('SELECT day_id, day_description FROM tbDays')
    days = cursor.fetchall()
    
    cursor.execute('SELECT task_id, task_description, isDone, day_id FROM tbTasks')
    tasks = cursor.fetchall()
    
    # Create a dictionary that maps each day ID to a list of tasks
    tasks_by_day = {day[0]: [] for day in days}
    for task in tasks:
        tasks_by_day[task[3]].append((task[0], task[1], task[2]))
    
    # Pass the days and tasks, along with the dictionary to the HTML template
    return render_template('index.html', days=days, tasks=tasks, tasks_by_day=tasks_by_day)
    #return tasks_by_day

@app.route('/add_task', methods=['POST'])
def add_task():
    
    # make the database connection and cursor object
    myConnection = sqlite3.connect("../db/src/database/mydb.sqlite3")
    cursor = myConnection.cursor()

    # Get the task description and day ID from the form
    task_description = request.form['task_description']
    day_id = request.form['day_id']

    # Get the last task ID from the database
    last_id = cursor.execute('SELECT MAX(task_id) FROM tbTasks').fetchone()[0]
    if last_id is None:
        last_id = 0

    # Insert the new task into the database
    cursor.execute('INSERT INTO tbTasks VALUES (?, ?, ?)', (last_id + 1, task_description, day_id))
    myConnection.commit()
    
    # Redirect to the home page
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)