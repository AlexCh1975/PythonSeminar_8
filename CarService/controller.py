import user_interface as ui
import modul_read as read
import modul_write as write
import create_db as c_db
import modul_search as ms
import modul_print as mp
import os


def select():
    path = 'db_carservice.db'
    # if os.path.exists(path) and os.path.getsize(path) > 0:
    index = ui.menu_carservice()

    # Запись нового клиента
    if index == 1:
        add_in_db(path)

    # Поиск по фомилии    
    elif index == 2:
        surname = ui.ui_searh_surname()
        # data = ui.ui_searh_surname()
        search_by_surname(path, surname)

    # Поиск по гос. номеру    
    elif index == 3:
        state_number = ui.ui_searh_state_number()
        search_state_number(path, state_number)
        # data_p = ms.search_surname(path, data['persons'][0])

    # Внести изменения в базу            
    elif index == 4:
        data = ui.ui_change()
        if index == 1:
            data = ui.ui_change() # Изменение данных
        elif index == 2:
            data = ui.ui_add_car() # добавить авто
        elif index == 3:
            data = ui.ui_change_repair() # ремонт
        elif index == 4:
            data = ui.ui_change_delete() # Удоление данных

    # else:
    #     c_db.create_db(path, 'persons')
    #     c_db.create_db(path, 'cars')
    #     c_db.create_db(path, 'repair')
            # print(data)

def add_in_db(path):
    data = ui.ui_person()
    write.add_table_person(path, data['persons'])
    data_p = ms.search_surname(path, data['persons'][0])
    if len(data_p) > 1:
        index = data_p[-1][0]
        print(index)
    else:
        index = data_p[0][0]
    data['cars'].append(index)
    print(index)
    write.add_table_car(path, data['cars'])

def search_by_surname(path, surname):
        data = ms.search_surname(path, surname)
        # print(data)
        if data:
            print(data)
        else:
            print("Клиента с такой фамилией в базе нет!")

def search_state_number(path, state_number):
        data = ms.search_state_number(path, state_number)
        if data:
            mp.print_res(data[0])
            mp.print_res(data[1])
        else:
            print("Такого номера в базе нет!")

# def search_state_number(path, state_number):
#         data = ms.search_state_number(path, state_number)
#         if data:
#             mp.print_res(data[0])
#             mp.print_res(data[1])
#         else:
#             print("Такого номера в базе нет!")

        

    
    


select()
# write.add_table_person('db_carservice.db', ['Григорьев', 'Вадим', '23.11.76', '1234567'])
# write.add_table_car('db_carservice.db', ['VAZ', 'NIVA', 2018, 23497, 'qwe123fkhdfghjtyu', 'см888ж', 2])