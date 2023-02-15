import sqlite3

try:
    myConnection = sqlite3.connect("database/mydb.sqlite3")
    cursor = myConnection.cursor()
    cursor.execute("CREATE TABLE tbDays (id INT PRIMARY KEY, description VARCHAR(50))")
except Exception as ex:
    print(ex)


# def connection():
#     try:
#         myConnection = sqlite3.connect("database/mydb.sqlite3")
#         cursor = myConnection.cursor()
#         return cursor

#     except Exception as ex:
#         print(ex)

# def create_tables():
#     try:
#         cursor = connection()
#         cursor.execute("CREATE TABLE tbDays (id INT PRIMARY KEY, description VARCHAR(50))")
#     except Exception as ex:
#         print(ex)

# def insert_rows():
#     try:
#         cursor = connection()
#         cursor.execute("INSERT INTO tbDays (id, description) VALUES (?, ?)", (1,"Monday"))
#         # cursor.execute("INSERT INTO tbDays VALUES (?,?)",(2,"Tuesday"))
#         # cursor.execute("INSERT INTO tbDays VALUES (?,?)",(3,"Wednesday"))
#         # cursor.execute("INSERT INTO tbDays VALUES (?,?)",(4,"Thursday"))
#         # cursor.execute("INSERT INTO tbDays VALUES (?,?)",(5,"Friday"))
#         # cursor.execute("INSERT INTO tbDays VALUES (?,?)",(6,"Saturday"))
#         # cursor.execute("INSERT INTO tbDays VALUES (?,?)",(7,"Sunday"))
#     except Exception as ex:
#         print(ex)

# def select_rows():
#     try:
#         cursor = connection()
#         cursor.execute("SELECT id, description FROM tbDays")
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#         # myConnection.close()
#     except Exception as ex:
#         print(ex)

# #create_tables()
# insert_rows()
# select_rows()