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

        res_c = list(cur.execute("""
                    SELECT * FROM cars WHERE state_number == ?
                    """, (state_number,)))
        person_id = res_c[0][-1]
        
        res_p = list(cur.execute("""
                    SELECT * FROM persons WHERE id == ?
                    """, (person_id,)))

        res = []
        res.append(res_p)
        res.append(res_c)

    return res
surname = 'Тресков'
# print(search_surname('db_carservice.db', surname))