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
        
        CREATE TABLE tbRoles (
            rol_id INTEGER PRIMARY KEY,
            rol_description VARCHAR(50)
        );
        
        CREATE TABLE tbUsers (
            user_id INTEGER PRIMARY KEY, 
            user_username VARCHAR(50),
            user_password VARCHAR(50),
            user_email VARCHAR(50),
            user_status INTEGER(1),
            rol_id INTEGER REFERENCES tbRoles(rol_id)
        );
        
        CREATE TABLE tbDays (
            day_id INTEGER PRIMARY KEY,
            day_description VARCHAR(50)
        );
        
        CREATE TABLE tbCategories (
            cat_id INTEGER PRIMARY KEY,
            cat_description VARCHAR(50)
        );
        
        CREATE TABLE tbTasks (
            task_id INTEGER PRIMARY KEY, 
            task_description VARCHAR(500),
            task_status INTEGER(1),
            day_id INTEGER REFERENCES tbDays(day_id),
            cat_id INTEGER REFERENCES tbCategories(cat_id),
            user_id INTEGER REFERENCES tbUsers(user_id)
        );
        
        INSERT INTO tbRoles VALUES (1,'Administrator');
        INSERT INTO tbRoles VALUES (2,'User');
        
        INSERT INTO tbUsers VALUES (1,'admin','admin123','test@gmail.com',1,1);
        INSERT INTO tbUsers VALUES (2,'nickramen','baleada','mytest@gmail.com',1,2);
        
        INSERT INTO tbDays VALUES (1,'Monday');
        INSERT INTO tbDays VALUES (2,'Tuesday');
        INSERT INTO tbDays VALUES (3,'Wednesday');
        INSERT INTO tbDays VALUES (4,'Thursday');
        INSERT INTO tbDays VALUES (5,'Friday');
        INSERT INTO tbDays VALUES (6,'Saturday');
        INSERT INTO tbDays VALUES (7,'Sunday');
        
        INSERT INTO tbCategories VALUES (1,'Personal');
        INSERT INTO tbCategories VALUES (2,'Work');
        INSERT INTO tbCategories VALUES (3,'School');
        INSERT INTO tbCategories VALUES (4,'Workout');
        INSERT INTO tbCategories VALUES (5,'Social');
        INSERT INTO tbCategories VALUES (6,'Home');
        INSERT INTO tbCategories VALUES (7,'Travel');
        
        INSERT INTO tbTasks VALUES (1, 'Complete project report', 1, 1, 1, 2);
        INSERT INTO tbTasks VALUES (2, 'Attend team meeting', 1, 2, 2, 2);
        INSERT INTO tbTasks VALUES (3, 'Submit expense report', 0, 3, 3, 2);
        INSERT INTO tbTasks VALUES (4, 'Review code changes', 1, 4, 4, 2);
        INSERT INTO tbTasks VALUES (5, 'Prepare for client presentation', 1, 5, 5, 2);
        INSERT INTO tbTasks VALUES (6, 'Update website content', 0, 6, 6, 2);
        INSERT INTO tbTasks VALUES (7, 'Call vendor for new equipment', 1, 7, 7, 2);
        INSERT INTO tbTasks VALUES (8, 'Draft marketing email', 1, 1, 1, 2);
        INSERT INTO tbTasks VALUES (9, 'Attend project kickoff meeting', 1, 2, 2, 2);
        INSERT INTO tbTasks VALUES (10, 'Review performance metrics', 0, 3, 3, 2);
    """)
    
    # commit the changes and close the database connection 
    myConnection.commit() 
    myConnection.close()
    
except Exception as ex:
    print(ex)