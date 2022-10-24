import sqlite3 as sq

def delete(path, id):

    with sq.connect(path) as con:
        cur = con.cursor()

        cur.execute('DELETE FROM persons WHERE id == ?', (id,))

# dellete('db_carservice.sqlite')