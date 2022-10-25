
import sqlite3 as sq
import logger as log



def add_table_person(path, persons):

    with sq.connect(path) as con:
        cur = con.cursor()
        persons_query = ("""INSERT INTO persons
                    (surname, name, birth_date, phone)
                    VALUES
                    ( ?, ?, ?, ?)
                    """)
        cur.execute(persons_query, persons)
        log.all_logger(persons, 'добавлено')
        print(f"{persons[0]} {persons[1]} успешно добавлена.")

def add_table_car(path, cars):
    with sq.connect(path) as con:
        cur = con.cursor()

        cars_query = ("""INSERT INTO cars
                    (brand, model, year_issue, mileage, vin, state_number, person_id)
                    VALUES
                    ( ?, ?, ?, ?, ?, ?, ?)
                    """)
        cur.execute(cars_query, cars)
        log.all_logger(cars, 'добавлено')
        print(f"{cars[0]} {cars[1]} успешно добавлена.")

def add_table_repair(path, repair):
    with sq.connect(path) as con:
        cur = con.cursor()

        repair_query = ("""INSERT INTO repair
                    (date, repair_op, price, car_id)
                    VALUES
                    ( ?, ?, ?, ?)
                    """)
        cur.execute(repair_query, repair)
        log.all_logger(repair, 'добавлено')
        print("Запись о ремонте успешно добавлена.")

