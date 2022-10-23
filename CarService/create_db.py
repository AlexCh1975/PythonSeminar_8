import sqlite3 as sq
# from sqlite3 import Error

# def create_connection(path):
#     connection = None
#     try:
#         connection = sq.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

# def create_db(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

def create_db(path, item):
    # with sq.connect(path) as con:
    #     cur = con.cursor()
    #     cur.execute(item)
    if item == 'persons':
        persons = """
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            surname TEXT NOT NULL, 
            name TEXT NOT NULL, 
            birth_date DATE, 
            phone TEXT NOT NULL
        )"""
        create(path, persons)

    elif item == 'cars':
        cars = """
        CREATE TABLE IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year_issue INTEGER,
            mileage INTEGER,
            vin TEXT,
            state_number TEXT NOT NULL,
            person_id INTEGER REFERENCES persons (id) ON DELETE CASCADE
        )"""
        create(path, cars)

    elif item == 'repair':
        repair = """
        CREATE TABLE IF NOT EXISTS repair(
            date TEXT NOT NULL,
            repair_op TEXT NOT NULL,
            price REAL,
            car_id INTEDER NOT NULL REFERENCES cars (id) ON DELETE CASCADE
        )"""
        create(path, repair)

def create(path, item):

    with sq.connect(path) as con:
        cur = con.cursor()
        cur.execute(item)


# connection = create_connection('db_carservice.sqlite')
# create_db(connection, person)
# create_db(connection, car)

# create_db('db_carservice.sqlite', person)
# create_db('db_carservice.sqlite', repair)

# c_db.create_db(path, 'persons')
#     c_db.create_db(path, 'cars')
#     c_db.create_db(path, 'repair')