import sqlite3 as sq

def search_surname_p(path, surname):
    with sq.connect(path) as con:
        cur = con.cursor()

        res = list(cur.execute("""
                    SELECT * FROM persons WHERE surname == ?
                    """, (surname,)))
    return res

def search_surname(path, id):

    with sq.connect(path) as con:
        cur = con.cursor()

        res_p = list(cur.execute("""
                    SELECT * FROM persons WHERE id == ?
                    """, (id,)))
       
        res_c = list(cur.execute("""
                    SELECT * FROM cars WHERE person_id == ?
                    """, (id,)))
        id_c = res_c[0][0]

        res_r = list(cur.execute("""
                    SELECT * FROM repair WHERE car_id == ?
                    """, (id_c,)))

        res = []
        res.append(res_p)
        res.append(res_c)
        res.append(res_r)
    return res


def search_state_number(path, state_number):

    with sq.connect(path) as con:
        
        cur = con.cursor()

        res_c = list(cur.execute("""
                    SELECT * FROM cars WHERE state_number == ?
                    """, (state_number,)))
        if res_c:
            person_id = res_c[0][-1]
            car_id = res_c[0][0]
        else: 
               
            return res_c         
        
        res_p = list(cur.execute("""
                    SELECT * FROM persons WHERE id == ?
                    """, (person_id,)))
        
        res_r = list(cur.execute("""
                    SELECT * FROM repair WHERE car_id == ?
                    """, (car_id,)))

        res = []
        res.append(res_p)
        res.append(res_c)
        res.append(res_r)

    return res

