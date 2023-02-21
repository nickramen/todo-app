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
            rol_id INTEGER REFERENCES tbRoles(rol_id),
            user_satisfaction INTEGER
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
        
        INSERT INTO tbUsers VALUES (1,'admin','admin123','test@gmail.com',1,1,0);
        INSERT INTO tbUsers VALUES (2,'nickramen','nickramen','mytest@gmail.com',1,2,5);
        INSERT INTO tbUsers VALUES (3,'nicole','nicole','nicole@gmail.com',1,2,4);
        INSERT INTO tbUsers VALUES (4,'sarahjones','ilovecats','sjones@gmail.com',1,2,0);
        INSERT INTO tbUsers VALUES (5,'johndoe','password456','johndoe@gmail.com',1,2,4);
        INSERT INTO tbUsers VALUES (6,'janedoe','password789','janedoe@gmail.com',1,2,5);
        INSERT INTO tbUsers VALUES (7,'mikebrown','mbrown123','mikebrown@gmail.com',1,2,2);
        INSERT INTO tbUsers VALUES (8,'jenniferlee','jl123456','jlee@gmail.com',1,2,3);
        INSERT INTO tbUsers VALUES (9,'davidwilliams','dwilliams','dwilliams@gmail.com',1,2,4);
        INSERT INTO tbUsers VALUES (10,'amyparker','aparker123','aparker@gmail.com',1,2,3);
        INSERT INTO tbUsers VALUES (11,'adamjones','ajones456','ajones@gmail.com',1,2,2);
        INSERT INTO tbUsers VALUES (12,'sarahsmith','ssmith123','ssmith@gmail.com',1,2,5);

        
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
        INSERT INTO tbTasks VALUES (11, 'Meet with vendor for product demo', 0, 7, 1, 2);
        INSERT INTO tbTasks VALUES (12, 'Complete software installation', 1, 2, 2, 2);
        INSERT INTO tbTasks VALUES (13, 'Prepare for final exams', 0, 3, 3, 2);
        INSERT INTO tbTasks VALUES (14, 'Create workout plan for the week', 1, 4, 4, 2);
        INSERT INTO tbTasks VALUES (15, 'Organize social event for team', 1, 5, 5, 2);
        INSERT INTO tbTasks VALUES (16, 'Clean the house', 0, 6, 6, 2);
        INSERT INTO tbTasks VALUES (17, 'Book flight tickets for vacation', 1, 7, 7, 2);
        INSERT INTO tbTasks VALUES (18, 'Write blog post for website', 1, 1, 1, 2);
        INSERT INTO tbTasks VALUES (19, 'Prepare for client demo', 1, 2, 2, 2);
        INSERT INTO tbTasks VALUES (20, 'Submit research paper', 0, 3, 3, 2);
        INSERT INTO tbTasks VALUES (21, 'Create exercise routine for the week', 1, 4, 4, 2);
        INSERT INTO tbTasks VALUES (22, 'Plan team building activity', 1, 5, 5, 2);
        INSERT INTO tbTasks VALUES (23, 'Organize closet', 0, 6, 6, 2);
        INSERT INTO tbTasks VALUES (24, 'Book hotel for vacation', 1, 7, 7, 2);
        INSERT INTO tbTasks VALUES (25, 'Write code for new feature', 1, 1, 1, 2);
        INSERT INTO tbTasks VALUES (26, 'Attend training session', 1, 2, 2, 2);
        INSERT INTO tbTasks VALUES (27, 'Research new marketing strategy', 0, 3, 3, 2);
        INSERT INTO tbTasks VALUES (28, 'Schedule appointments with clients', 1, 4, 4, 2);
        INSERT INTO tbTasks VALUES (29, 'Plan company event', 1, 5, 5, 2);
        INSERT INTO tbTasks VALUES (30, 'Clean out the garage', 0, 6, 6, 2);
        INSERT INTO tbTasks VALUES (31, 'Book rental car for vacation', 1, 7, 7, 2);
        INSERT INTO tbTasks VALUES (32, 'Review website analytics', 1, 1, 1, 2);
        INSERT INTO tbTasks VALUES (33, 'Meet with team for project status update', 1, 2, 2, 2);
        INSERT INTO tbTasks VALUES (34, 'Create sales report', 0, 3, 3, 2);
        INSERT INTO tbTasks VALUES (35, 'Run 5 miles', 1, 4, 4, 2);
        INSERT INTO tbTasks VALUES (36, 'Plan team outing', 1, 5, 5, 2);
        INSERT INTO tbTasks VALUES (37, 'Organize bookshelf', 0, 6, 6, 2);
        INSERT INTO tbTasks VALUES (38, 'Book vacation rental', 1, 7, 7, 2);
        
        
        INSERT INTO tbTasks VALUES (39, 'Complete personal project', 1, 1, 1, 3);
        INSERT INTO tbTasks VALUES (40, 'Read book on personal development', 1, 1, 1, 3);
        INSERT INTO tbTasks VALUES (41, 'Meditate for 20 minutes', 0, 1, 1, 2);
        INSERT INTO tbTasks VALUES (42, 'Meet with project team for status update', 1, 2, 2, 3);
        INSERT INTO tbTasks VALUES (43, 'Prepare for client meeting', 1, 2, 2, 3);
        INSERT INTO tbTasks VALUES (44, 'Attend training on new software', 1, 2, 2, 3);
        INSERT INTO tbTasks VALUES (45, 'Follow up with customer support on issue', 1, 2, 2, 3);
        INSERT INTO tbTasks VALUES (46, 'Research industry trends', 0, 2, 2, 3);
        INSERT INTO tbTasks VALUES (47, 'Study for final exam', 0, 3, 3, 3);
        INSERT INTO tbTasks VALUES (48, 'Write research paper on climate change', 1, 3, 3, 3);
        INSERT INTO tbTasks VALUES (49, 'Attend office hours with professor', 0, 3, 3, 3);
        INSERT INTO tbTasks VALUES (50, 'Review class notes for upcoming quiz', 0, 3, 3, 3);
        INSERT INTO tbTasks VALUES (51, 'Go for a 5 mile run', 1, 4, 4, 3);
        INSERT INTO tbTasks VALUES (52, 'Attend yoga class', 0, 4, 4, 3);
        INSERT INTO tbTasks VALUES (53, 'Attend friends wedding', 1, 5, 5, 3);
        INSERT INTO tbTasks VALUES (54, 'Clean kitchen', 1, 6, 6, 3);
        INSERT INTO tbTasks VALUES (55, 'Do laundry', 1, 6, 6, 3);
        INSERT INTO tbTasks VALUES (56, 'Organize closet', 1, 6, 6, 3);
        INSERT INTO tbTasks VALUES (57, 'Wash dishes', 1, 6, 6, 3);
        INSERT INTO tbTasks VALUES (58, 'Vacuum living room', 1, 6, 6, 3);
        INSERT INTO tbTasks VALUES (59, 'Take out trash', 1, 6, 6, 3);
        INSERT INTO tbTasks VALUES (60, 'Book flights for upcoming vacation', 1, 7, 7, 3);
        INSERT INTO tbTasks VALUES (61, 'Research tourist attractions in new city', 0, 7, 7, 3);
    """)
    
    # commit the changes and close the database connection 
    myConnection.commit() 
    myConnection.close()
    
except Exception as ex:
    print(ex)