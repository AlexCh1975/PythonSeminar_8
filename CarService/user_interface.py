
import re
from datetime import datetime
import modul_print as mp

# Меню 
def menu_carservice():
    print('-------------------------------------------------')

    print("Выберите тип операции: ")

    print("     Новый клиет: 1")
    print("     Поиск по фамилии: 2")
    print("     Поиск по гос. номеру: 3")
    print("     Внести изменения в базу: 4")

    while True:
        index = int(input("Тип операции: "))
        if 0 < index < 5:
            return index
        else:
            print(f"{index} Некоректный выбор!")

# Доп. меню
def ui_change():
    print("Внести изменения в базу:")
    print("     Изменение № телефона клиента: 1")
    print("     Добавить транспортное средство: 2")
    print("     Ремотные работы: 3")
    print("     Удалить клиента из базы: 4")

    while True:
        index = int(input("Тип операции: "))
        if 0 < int(index) < 5:
            return index
        else:
            print(f"{index} Некоректный выбор!")
    
def ui_person(): 
    data_person = ui_add_person()
    data_car = ui_add_car()
    data = {}
    data['persons'] = data_person
    data['cars'] = data_car
    return data

# Добавление данных клиента 
def ui_add_person():
    print('-------------------------------------------------')

    data_person = []
    print("Введите данные клиента!")

    while True:
        surname = input("Фамилия: ")
        if surname.isalpha() and len(surname) > 1: 
            surname = surname.capitalize()
            data_person.append(surname)
            break
        else:
            print("Некорректный ввод!")

    while True:
        name = input("Имя: ")
        if name.isalpha() and len(name) > 1: 
            name = name.capitalize()
            data_person.append(name)
            break
        else:
            print("Некорректный ввод!")

    while True:
        birth_date = input("Дата рождения (DD.MM.YYYY): ")
        if birth_date.isdigit() or '.' in birth_date: 
            data_person.append(birth_date)
            break
        else:
            print("Некорректный ввод!")

    while True:
        phone = input("Введите номер телефона: ")
        if phone.isdigit(): 
            data_person.append(phone)
            break
        else:
            print("Некорректный ввод!")

    print('-------------------------------------------------')
    return data_person

# Добавление данных автомобиля
def ui_add_car():
    print('-------------------------------------------------')
    print("Внесите данные автомобиля!")
    data_car = []

    while True:
        brand = input("Марка: ")
        if brand.isalpha() and len(brand) > 1:
            data_car.append(brand.capitalize())
            break
        else:
            print("Некорректный ввод!")

    while True:
        model = input("Модель: ")
        if model.isalnum() and len(model) > 1:
            data_car.append(model.capitalize())
            break
        else:
            print("Некорректный ввод!")

    while True:
        year_issue = input("Год выпуска: ")
        if year_issue.isdigit():
            year_issue = int(year_issue)
            data_car.append(year_issue)
            break
        else:
            print("Некорректный ввод!")

    while True:
        mileage = input("Пробег (км)(миль): ")
        if mileage.isdigit(): 
            mileage = int(mileage)
            data_car.append(mileage)
            break
        else:
            print("Некорректный ввод!")

    while True:
        vin = input("VIN-номер (мин 10 мак 17): ")
        if 9 < len(vin) < 18: 
            data_car.append(vin.capitalize())
            break
        else:
            print("Некорректный ввод!")

    while True:
        state_number = input("Гос номер: ")
        if state_number.isalnum(): 
            state_number = state_number.lower()
            data_car.append(state_number)
            break
        else:
            print("Некорректный ввод!")
    return data_car

#  Поиск по фамилии       
def ui_searh_surname():
    print('-------------------------------------------------') 
    surname = input("Введите фамилию для поиска: ") 
    while True:
        # surname = input("Введите фамилию для поиска: ")
        if surname.isalpha() and len(surname) > 1:
            surname = surname.capitalize()
            return surname
        else: 
            print("Некоректный ввод!")

# Поиск по гос. номеру
def ui_searh_state_number():
    print('-------------------------------------------------')
    state_number = input("Введите гос. номер авто: ")  
    while True:
        # state_number = input("Введите гос. номер авто: ")
        if state_number.isalnum():
            state_number = state_number.lower()
            return state_number
        else: 
            print("Некоректный ввод!")

# Добавление данных о ремонте
def ui_change_repair():
    print('-------------------------------------------------')
    data = []
    # while True:
    #     date = input("Введите дату ремонта (DD.MM.YYYY): ")
    #     if date.isdigit() or '.' in date:
    #         data.append(date)
    #         break
    #     else:
    #         print("Некоректный ввод!")

    repair_op = input("Ремонт: ")
    data.append(repair_op)

    while True:
        price = input("Стоимость ремонта: ")
        if price.isdigit() or '.' in price:
            price = float(price)
            data.append(price)
            break
        else:
            print("Некоректный ввод!")

    return data

# Выбор id клиента
def ui_select_person(data):
    print('-------------------------------------------------')
    mp.print_res(data)
    while True:
        id = input("Введите id нужного клиента: ")
        if id.isdigit():
            id = int(id)
            return id
        else:
            print("Некоректный ввод!")

# Новый телефон клиента
def ui_new_phone():
    print('-------------------------------------------------')
    while True:
        n_phone = input("Введите новый телефон: ")
        if n_phone.isdigit():
            return n_phone
        else:
            print("Некоректный ввод!")



