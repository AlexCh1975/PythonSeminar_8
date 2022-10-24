import sqlite3 as sq

def dellete(path):

    with sq.connect(path) as con:
        cur = con.cursor()

        cur.execute('DELETE FROM person WHERE surname == ?', ('Федоров',))

# dellete('db_carservice.sqlite')