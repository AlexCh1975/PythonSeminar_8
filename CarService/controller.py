from locale import resetlocale
import user_interface as ui
import modul_read as read
import modul_write as write
import create_db as c_db
import modul_search as ms
import modul_print as mp
import modul_update as mu
import modul_delete as md
import logger as log
from datetime import datetime as dt
from time import strftime
import os


def select():
    # path = 'db_carservice.db'
    path = 'db_service.db'
    # if os.path.exists(path) and os.path.getsize(path) > 0:
    index = ui.menu_carservice()

    # Запись нового клиента
    if index == 1:
        add_in_db(path)

    # Поиск по фомилии    
    elif index == 2:
        surname = ui.ui_searh_surname()
        data = search_by_surname(path, surname)
        mp.print_res(data[0])
        mp.print_res(data[1])
        mp.print_res(data[2])

    # Поиск по гос. номеру    
    elif index == 3:
        state_number = ui.ui_searh_state_number()
        search_state_number(path, state_number)

    # Внести изменения в базу            
    elif index == 4:
        index = ui.ui_change()
        if index == 1:
            data = change_phone(path) # Изменение данных (номера телефона)
        if index == 2:
            add_car(path) # добавить авто
        elif index == 3:
            change_repair(path) # ремонт
        elif index == 4:
            change_delete(path) # Удоление данных

    # else:
    #     c_db.create_db(path, 'persons')
    #     c_db.create_db(path, 'cars')
    #     c_db.create_db(path, 'repair')
            # print(data)

# Управление добавлением клиента
def add_in_db(path):
    data = ui.ui_person()
    write.add_table_person(path, data['persons'])
    data_p = ms.search_surname_p(path, data['persons'][0])
    if len(data_p) > 1:
        index = data_p[-1][0]
        # print(index)
    else:
        index = data_p[0][0]
    data['cars'].append(index)
    # print(index)
    write.add_table_car(path, data['cars'])

# Управление поиском по фамилии
def search_by_surname(path, surname):
        data = ms.search_surname(path, surname)
        if data:
            log.all_logger(data, 'поиск по фамилии')
            return data
        else:
            log.all_logger("Клиента с такой фамилией в базе нет!", 'поиск по фамилии')
            print("Клиента с такой фамилией в базе нет!")

# Управление поиском по гос. номеру
def search_state_number(path, state_number):
        data = ms.search_state_number(path, state_number)
        if data:
            log.all_logger(data[0:1], 'поиск по гос. номеру')
            mp.print_res(data[0])
            mp.print_res(data[1])
            mp.print_res(data[2])
        else:
            log.all_logger("Такого номера в базе нет!", 'поиск по гос. номеру')
            print("Такого номера в базе нет!")

# Управление. Добавить ремонт по гос. номеру
def change_repair(path):
    state_number = ui.ui_searh_state_number()
    data = ms.search_state_number(path, state_number)
    id = data[1][0][0]
    if data:
        data_ui = ui.ui_change_repair() # получаем данные по ремонту из ui
        time = dt.now().strftime('%Y-%m-%d %H:%M')
        data_ui.insert(0, time)
        data_ui.append(id)
        write.add_table_repair(path, data_ui)
    else:
        log.all_logger("Такого номера в базе нет!", 'поиск по гос. номеру')
        print("Такого номера в базе нет!")

# Управление. Добавить авто
def add_car(path):
    surname = ui.ui_searh_surname()
    data = ms.search_surname_p(path, surname)
    if len(data) == 1:
        id = data[0][0]
        data_car = ui.ui_add_car()
        data_car.append(id)
        write.add_table_car(path, data_car)
        # print(data_car)

# Управление. Замена телефона клиента
def change_phone(path):
    surname = ui.ui_searh_surname()
    data = ms.search_surname_p(path, surname)
    # print(data)
    if len(data) > 1:
        id = ui.ui_select_person(data)
        n_phone = ui.ui_new_phone()
        mu.update(path, id, n_phone)
    else:
        id = data[0][0]
        n_phone = ui.ui_new_phone()
        mu.update(path, id, n_phone)

# Удоление из базы
def change_delete(path):
    surname = ui.ui_searh_surname() 
    data = ms.search_surname_p(path, surname)  
    if len(data) > 1:
        id = ui.ui_select_person(data)
        log.all_logger(id, 'удоление')
        md.delete(path, id)
    else:
        id = data[0][0]
        log.all_logger(id, 'удоление')
        md.delete(path, id)
    
    


select()
# write.add_table_person('db_carservice.db', ['Григорьев', 'Вадим', '23.11.76', '1234567'])
# write.add_table_car('db_carservice.db', ['VAZ', 'NIVA', 2018, 23497, 'qwe123fkhdfghjtyu', 'см888ж', 2])