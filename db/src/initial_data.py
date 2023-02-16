import sqlite3

try:
    # make the database connection and cursor object
    myConnection = sqlite3.connect("database/mydb.sqlite3")
    cursor = myConnection.cursor() 

    # create a set of queries in executescript()
    # below set of queries will create and insert
    # data into table
    cursor.executescript("""
        CREATE TABLE tbDays (id INT PRIMARY KEY, description VARCHAR(50));
        INSERT INTO tbDays VALUES ( 1,'Monday');
        INSERT INTO tbDays VALUES ( 2,'Tuesday');
        INSERT INTO tbDays VALUES ( 3,'Wednesday');
        INSERT INTO tbDays VALUES ( 4,'Thursday');
        INSERT INTO tbDays VALUES ( 5,'Friday');
        INSERT INTO tbDays VALUES ( 6,'Saturday');
        INSERT INTO tbDays VALUES ( 7,'Sunday');
        
    """)
    
    # commit the changes and close the database connection 
    myConnection.commit() 
    myConnection.close()
    
except Exception as ex:
    print(ex)