from flask import Flask, request, send_from_directory, session, jsonify
import sqlite3
from src.database import create_connection

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'your_secret_key_here'

# Route for serving static files
@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('assets', path)


###############
# USER GRAPHS #
###############

@app.route('/task_per_day', methods=['POST'])
def task_per_day():
    
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are assigned to each day of the week
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        user_id = session.get('user_id')
        cursor.execute('SELECT day_id FROM tbTasks WHERE user_id == ?',(user_id,))
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
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        user_id = session.get('user_id')
        cursor.execute('SELECT task_status FROM tbTasks WHERE user_id == ?',(user_id,))
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


################
# ADMIN GRAPHS #
################

@app.route('/admin_task_per_day', methods=['GET'])
def admin_task_per_day():
    
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are assigned to each day of the week
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        user_id = session.get('user_id')
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

        admin_task_per_day_count = count_tasks(tasks)
        
    return admin_task_per_day_count
    
@app.route('/admin_task_done_undone', methods=['GET'])
def admin_task_done_undone():
    
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are done and how many are undone
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        user_id = session.get('user_id')
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

        admin_task_count = count_tasks(tasks)
        
    return admin_task_count

@app.route('/admin_overview_task_total', methods=['GET'])
def admin_overview_task_total():
    
    # Make the database connection and cursor object
    # Select all the users from tbUsers
    # Determine how many tasks have been created
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        cursor.execute('SELECT task_id FROM tbTasks')
        tasks = cursor.fetchall()
        
        def count_tasks(tasks):
            task_count = 0
            for task in tasks:
                task_count += 1
            return task_count

        admin_total_task = count_tasks(tasks)
        
    return admin_total_task

@app.route('/admin_overview_user_total', methods=['GET'])
def admin_overview_user_total():
    
    # Make the database connection and cursor object
    # Select all the users from tbUsers
    # Determine how many tasks have been created
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        cursor.execute('SELECT user_id FROM tbUsers')
        users = cursor.fetchall()
        
        def count_users(users):
            user_count = 0
            for user in users:
                user_count += 1
            return user_count

        admin_total_user = count_users(users)
        
    return admin_total_user