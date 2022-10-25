import sqlite3 as sq

def create_db(path, item):

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

# path = 'db_carservice.db'
path = 'db_service.db'

# create_db(path, 'persons')
# create_db(path, 'cars')
# create_db(path, 'repair')