from flask import Flask, send_from_directory, jsonify, json
from src.database import create_connection

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'your_secret_key_here'

# Route for serving static files
@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('assets', path)


@app.route('/users_list', methods=['POST'])
def users_list():
    
    with create_connection() as myConnection:
        
        try:
            cursor = myConnection.cursor()
            
            users = cursor.execute("SELECT user_id, user_username, user_email, user_status FROM tbUsers").fetchall()
            
            #users = [dict(zip(['user_id', 'user_username', 'user_email', 'user_status'], row)) for row in users]
            
            return jsonify({'success': True, 'userslist': users})
        except:
            return jsonify({'success': False})
