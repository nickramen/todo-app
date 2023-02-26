from flask import Flask, request, send_from_directory, session, jsonify
import sqlite3
from src.database import create_connection
import json

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'your_secret_key_here'

# Route for serving static files
@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('assets', path)


########## USER SATISFACTION ##########
@app.route('/user_satisfaction', methods=['POST'])
def user_satisfaction():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        
        user_id = session.get('user_id')
        rate = cursor.execute("SELECT user_satisfaction FROM tbUsers WHERE user_id = ?",(user_id,)).fetchone()[0]
        print(rate)
    return rate

########## USER GRAPHS ##########
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


@app.route('/task_per_category_count', methods=['GET'])
def task_per_category_count():
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are assigned to each day of the week
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        user_id = session.get('user_id')
        
        cursor.execute('''
                        SELECT tbCategories.cat_description, COUNT(tbTasks.task_id) AS task_count
                        FROM tbCategories
                        LEFT JOIN tbTasks ON tbCategories.cat_id = tbTasks.cat_id
                        LEFT JOIN tbUsers ON tbTasks.user_id = tbTasks.user_id
                        WHERE tbTasks.user_id = ?
                        GROUP BY tbCategories.cat_description
                        ''',(user_id,))
        
        tasks = cursor.fetchall()
        
        categories = []
        task_count = []
        
        for row in tasks:
            categories.append(row[0])
            task_count.append(row[1])
        
    return categories, task_count

########## ADMIN GRAPHS ##########
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

@app.route('/admin_task_per_category', methods=['GET'])
def admin_task_per_category():
    # Make the database connection and cursor object
    # Select all the tasks from tbTasks
    # Determine how many tasks are assigned to each category
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        cursor.execute('''
                        SELECT tbCategories.cat_description, COUNT(tbTasks.task_id) AS task_count
                        FROM tbCategories
                        LEFT JOIN tbTasks ON tbCategories.cat_id = tbTasks.cat_id
                        GROUP BY tbCategories.cat_description;
                        ''')
        tasks = cursor.fetchall()
        
        categories = []
        task_count = []

        for row in tasks:
            categories.append(row[0])
            task_count.append(row[1])
        
    return categories, task_count

@app.route('/admin_overview_category_total', methods=['GET'])
def admin_overview_category_total():
    # Make the database connection and cursor object
    # Select all the catgories from tbCateogries
    # Determine how many cateogories are in total
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        cursor.execute('SELECT COUNT(*) FROM tbCategories')
        categories = cursor.fetchone()[0]
        
    return categories
    
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
    # Determine how many users have been registered in total
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

@app.route('/admin_overview_user_satisfaction', methods=['GET'])
def admin_overview_user_satisfaction():
    
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        data = cursor.execute('SELECT user_satisfaction FROM tbUsers').fetchall()
        # Filter out users who haven't taken the survey (i.e., whose rating is 0)
        ratings = [rating[0] for rating in data if rating[0] != 0]
        # Calculate the percentage of users who gave each rating
        counts = [0] * 5
        for rating in ratings:
            counts[rating-1] += 1
        total = sum(counts)
        percentages = [int(count/total*100) if total > 0 else 0 for count in counts]
        # Calculate the overall user satisfaction score
        satisfaction_score = (percentages[0]/100 * 20) + (percentages[1]/100 * 40) + (percentages[2]/100 * 60) + (percentages[3]/100 * 80) + (percentages[4]/100 * 100)

        return satisfaction_score


@app.route('/admin_user_active_inactive', methods=['GET'])
def admin_user_active_inactive():
        
    with create_connection() as myConnection:
        cursor = myConnection.cursor()
        cursor.execute('SELECT user_status FROM tbUsers')
        users = cursor.fetchall()
        
        def count_users(tasks):
            active_count = 0
            inactive_count = 0
            for user in users:
                if user[0] == 1:
                    active_count += 1
                elif user[0] == 0:
                    inactive_count += 1
            return [active_count, inactive_count]

        user_count = count_users(users)
        
    return user_count