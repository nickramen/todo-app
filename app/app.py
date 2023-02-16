from flask import Flask, render_template
import sqlite3

app = Flask(__name__,template_folder='template')

@app.route('/index',methods=['GET'])
def get_table():
    # make the database connection and cursor object
    myConnection = sqlite3.connect("../db/src/database/mydb.sqlite3")
    cursor = myConnection.cursor()
    # fetch the table data
    result = cursor.execute('SELECT id, description FROM tbDays')
    return render_template('index.html', days=result.fetchall())
    # return render_template('index.html')
    # return 'Hello world'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    