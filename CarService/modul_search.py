import sqlite3 as sq

def search_surname(path, surname):

    with sq.connect(path) as con:
        cur = con.cursor()

        res = list(cur.execute("""
                    SELECT * FROM persons WHERE surname == ?
                    """, (surname,)))
    return res


def search_state_number(path, state_number):

    with sq.connect(path) as con:
        cur = con.cursor()

        res = list(cur.execute("""
                    SELECT * FROM persons WHERE vin, state_number == ?
                    """, (state_number,)))

    return res