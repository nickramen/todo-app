import sqlite3

try:
    # make the database connection and cursor object
    myConnection = sqlite3.connect("database/mydb.sqlite3")
    cursor = myConnection.cursor() 

    # create a set of queries in executescript()
    # below set of queries will create and insert
    # data into table
    cursor.executescript("""
        PRAGMA foreign_keys = ON;
        
        CREATE TABLE tbDays (
            day_id INTEGER PRIMARY KEY,
            day_description VARCHAR(50)
        );
        
        CREATE TABLE tbTasks (
            task_id INTEGER PRIMARY KEY, 
            task_description VARCHAR(250),
            task_status INT(1),
            day_id INTEGER REFERENCES tbDays(day_id)
        );
        
        INSERT INTO tbDays VALUES (1,'Monday');
        INSERT INTO tbDays VALUES (2,'Tuesday');
        INSERT INTO tbDays VALUES (3,'Wednesday');
        INSERT INTO tbDays VALUES (4,'Thursday');
        INSERT INTO tbDays VALUES (5,'Friday');
        INSERT INTO tbDays VALUES (6,'Saturday');
        INSERT INTO tbDays VALUES (7,'Sunday');
        
        INSERT INTO tbTasks VALUES (1, 'Complete project report', 1, 1);
        INSERT INTO tbTasks VALUES (2, 'Attend team meeting', 1, 2);
        INSERT INTO tbTasks VALUES (3, 'Submit expense report', 0, 3);
        INSERT INTO tbTasks VALUES (4, 'Review code changes', 1, 4);
        INSERT INTO tbTasks VALUES (5, 'Prepare for client presentation', 1, 5);
        INSERT INTO tbTasks VALUES (6, 'Update website content', 0, 6);
        INSERT INTO tbTasks VALUES (7, 'Call vendor for new equipment', 1, 7);
        INSERT INTO tbTasks VALUES (8, 'Draft marketing email', 1, 1);
        INSERT INTO tbTasks VALUES (9, 'Attend project kickoff meeting', 1, 2);
        INSERT INTO tbTasks VALUES (10, 'Review performance metrics', 0, 3);
    """)
    
    # commit the changes and close the database connection 
    myConnection.commit() 
    myConnection.close()
    
except Exception as ex:
    print(ex)