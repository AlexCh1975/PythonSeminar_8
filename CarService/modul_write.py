import sndhdr
import sqlite3 as sq



def add_table_person(path, persons):
    # try:
    #     sqlite_connection = sq.connect('db_carservice.sqlite')
    #     cursor = sqlite_connection.cursor()
    #     print("Подключен к SQLite")

    #     # key_per_str = ', '.join(data['person'])
    #     # person_str = ', '.join(data['person'].values())

    #     sqlite_insert_query = """INSERT INTO db_carservice
    #                         VALUES
    #                         (?, ?, ?, ?);"""
        
    #     count = cursor.execute(sqlite_insert_query, data)
    #     sqlite_connection.commit()
    #     print("Запись успешно вставлена ​​в таблицу db_carservice ", cursor.rowcount)
    #     cursor.close()

    # except sq.Error as error:
    #     print("Ошибка при работе с SQLite", error)
    # finally:
    #     if sqlite_connection:
    #         sqlite_connection.close()
    #         print("Соединение с SQLite закрыто")


    # person_tuple = 'Федоров', 'Вадим', '23.11.76', '1234567'
    # person_key = 'surname', 'name', 'birth_date', 'phone'

    with sq.connect(path) as con:
        cur = con.cursor()
        persons_query = ("""INSERT INTO persons
                    (surname, name, birth_date, phone)
                    VALUES
                    ( ?, ?, ?, ?)
                    """)
        cur.execute(persons_query, persons)

def add_table_car(path, cars):
    with sq.connect(path) as con:
        cur = con.cursor()

        cars_query = ("""INSERT INTO cars
                    (brand, model, year_issue, mileage, vin, state_number, person_id)
                    VALUES
                    ( ?, ?, ?, ?, ?, ?, ?)
                    """)
        cur.execute(cars_query, cars)

def add_table_repair(path, repair):
    with sq.connect(path) as con:
        cur = con.cursor()

        repair_query = ("""INSERT INTO repair
                    (date, repair_op, price, car_id)
                    VALUES
                    ( ?, ?, ?, ?)
                    """)
        cur.execute(repair_query, repair)

# repair_tuple = ['20.10.2022', 'ТО', '2550', 'зо999ж']
# person_tuple = ['Григорьев', 'Вадим', '23.11.76', '1234567']
# car_tuple = ['Opel', 'Cadet', 1999, '234987', 'qwe123fkhdgsghlkhg', 'зо999ж', 12]
# create_db('sm_app.sqlite')
# add_table_person('db_carservice.sqlite', person_tuple)
# add_table_car('db_carservice.sqlite', car_tuple)
# add_table_repair('db_carservice.sqlite', repair_tuple)