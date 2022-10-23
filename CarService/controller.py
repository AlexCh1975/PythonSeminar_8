import user_interface as ui
import modul_read as read
import modul_write as write
import create_db as c_db
import modul_search as ms
import os


def select():
    path = 'db_carservice.db'
    if os.path.exists(path) and os.path.getsize(path) > 0:
        index = ui.menu_carservice()
        if index == 1:
            data = ui.ui_person()
            write.add_table_person(path, data['persons'])
            data_p = ms.search_surname(path, data['persons'][0])
            if len(data_p) > 1:
                index = data_p[-1][0]
                print(index)
            else:
                index = data_p[0][0]
            data['cars'].append(index)
            write.add_table_car(path, data['cars'])
            
        elif index == 2:
            data = ui.ui_searh_surname()
        elif index == 3:
            data = ui.ui_search_state_number()
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

    else:
        c_db.create_db(path, 'persons')
        c_db.create_db(path, 'cars')
        c_db.create_db(path, 'repair')
            # print(data)
    # key_person = []
    # key_car = []
    

    # key_car = [key for key in data['car']]
    
    # key_per_str = ', '.join(data['person'])
    # person_str = ', '.join(data['person'].values())
    # print(person_str)
    # print(key_per_str)
    # exit()
    # c_db.create_db(path)
    # write.add_db(path, data['person'])

    
    


select()
# write.add_table_person('db_carservice.db', ['Григорьев', 'Вадим', '23.11.76', '1234567'])
# write.add_table_car('db_carservice.db', ['VAZ', 'NIVA', 2018, 23497, 'qwe123fkhdfghjtyu', 'см888ж', 2])