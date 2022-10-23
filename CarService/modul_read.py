import sqlite3 as sq

def get_person(path):

    with sq.connect(path) as con:
        cur = con.cursor()

        res = list(cur.execute("""SELECT * FROM person JOIN car  
                                ON person.id == car.person_id WHERE person.id == ?""", 
                                (2,)))


        keys = ['ID', "Фамилия", "Имя", "Дата рождения", "Телефон", "Марка", "Модель", \
            "Год выпуска", "Пробег", "VIN", "Гос номер"]

        # for i in range(len(res)):
        #     print(f"{keys[i]}: {res[i]}")
        print(res) 

# get_person('db_carservice.db')
