from flask import Flask, render_template
import sqlite3

app = Flask(__name__,template_folder='template')

@app.route('/index',methods=['GET'])
def get_initial_data():
    # make the database connection and cursor object
    myConnection = sqlite3.connect("../db/src/database/mydb.sqlite3")
    cursor = myConnection.cursor()
    
    # Fetch all the days and tasks from the database
    cursor.execute('SELECT day_id, day_description FROM tbDays')
    days = cursor.fetchall()
    
    cursor.execute('SELECT task_id, task_description, day_id FROM tbTasks')
    tasks = cursor.fetchall()
    
    # Create a dictionary that maps each day ID to a list of tasks
    tasks_by_day = {day[0]: [] for day in days}
    for task in tasks:
        tasks_by_day[task[2]].append((task[0], task[1]))
    
    # Pass the days and tasks, along with the dictionary to the HTML template
    return render_template('index.html', days=days, tasks=tasks, tasks_by_day=tasks_by_day)
    #return tasks_by_day


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)