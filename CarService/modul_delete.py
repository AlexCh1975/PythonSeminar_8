import sqlite3 as sq
import logger as log

def delete(path, id, surname):

    with sq.connect(path) as con:
        cur = con.cursor()

        res_c = list(cur.execute("""
                    SELECT * FROM cars WHERE person_id == ?
                    """, (id,)))
        id_c = res_c[0][0]

        res_r = list(cur.execute("""
                    SELECT * FROM repair WHERE car_id == ?
                    """, (id_c,)))

        cur.execute('DELETE FROM persons WHERE id == ?', (id,))
        cur.execute('DELETE FROM cars WHERE person_id == ?', (id,))
        cur.execute('DELETE FROM repair WHERE car_id == ?', (id_c,))

        print(f'Запись о клиенте {surname} удолена!')
 
