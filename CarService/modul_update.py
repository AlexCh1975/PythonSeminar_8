import sqlite3 as sq
import logger as log

def update(path, id, phone_n):

    with sq.connect(path) as con:
        cur = con.cursor()

        cur.execute('UPDATE persons SET phone = ? WHERE id == ?', (phone_n, id,))
        res = cur.execute('SELECT * FROM persons WHERE id == ?', (id,))
        log.all_logger(res, 'изменение номера телефона')
        print("Номер успешно изменен.")
        

            

# print(update('db_carservice.db', 33, 111111))