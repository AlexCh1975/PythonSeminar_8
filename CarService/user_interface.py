
import re
from datetime import datetime

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

def ui_change():
    print("Внести изменения в базу:")
    print("     Изменение данных: 1")
    print("     Добавить транспортное средство: 2")
    print("     Ремонт: 3")
    print("     Удалить: 4")

    while True:
        index = int(input("Тип операции: "))
        if 0 < int(index) < 5:
            return index
        else:
            print(f"{index} Некоректный выбор!")
    exit()

    


    # n_person = input("  Новый клиет: 1")
    # search_surname = input("  Поиск по фамилии: 2")
    # search_state_number = input("  Поиск по гос. номеру: 3")
    # all_change = input("  Внести изменения: 4")
    # change = input("    Изменение данных: 1")
    # repair = input("    Ремонт: 2")
    # delete = input("    Удалить: 3")
    
    # if n_person: return 1

def ui_person(): 
    print('-------------------------------------------------')

    # data_person = {}
    data_person = []
    print("Введите данные клиента!")

    while True:
        surname = input("Фамилия: ")
        if surname.isalpha(): 
            # data_person['surname'] = surname
            surname = surname.capitalize()
            data_person.append(surname)
            break
        else:
            print("Некорректный ввод!")

    while True:
        name = input("Имя: ")
        if name.isalpha(): 
            # data_person['name'] = name
            name = name.capitalize()
            data_person.append(name)
            break
        else:
            print("Некорректный ввод!")

    while True:
        birth_date = input("Дата рождения: ")
        if birth_date.isdigit() or '.' in birth_date: 
            # data_person['date_birth'] = birth_date
            data_person.append(birth_date)
            break
        else:
            print("Некорректный ввод!")

    while True:
        phone = input("Введите номер телефона: ")
        if phone.isdigit(): 
            # data_person['phone'] = phone
            data_person.append(phone)
            break
        else:
            print("Некорректный ввод!")

    print('-------------------------------------------------')

    print("Данные Автомобиля.")
    # data_car = {}
    data_car = []

    while True:
        brand = input("Марка: ")
        if brand.isalpha(): 
            # data_car['brand'] = brand
            data_car.append(brand)
            break
        else:
            print("Некорректный ввод!")

    while True:
        model = input("Модель: ")
        if model.isalnum():
            # data_car['model'] = model
            data_car.append(model)
            break
        else:
            print("Некорректный ввод!")

    while True:
        year_issue = input("Год выпуска: ")
        if year_issue.isdigit():
            year_issue = int(year_issue)
            # data_car['year_issue'] = year_issue
            data_car.append(year_issue)
            break
        else:
            print("Некорректный ввод!")

    while True:
        mileage = input("Пробег (км)(миль): ")
        if mileage.isdigit(): 
            mileage = int(mileage)
            # data_car['mileage'] = mileage
            data_car.append(mileage)
            break
        else:
            print("Некорректный ввод!")

    while True:
        vin = input("VIN-номер (мин 10 мак 17): ")
        if 9 < len(vin) < 18: 
            # data_car['vin'] = vin
            data_car.append(vin)
            break
        else:
            print("Некорректный ввод!")

    while True:
        state_number = input("Гос номер: ")
        if state_number.isalnum(): 
            # data_car['state_number'] = state_number
            state_number = state_number.lower()
            data_car.append(state_number)
            break
        else:
            print("Некорректный ввод!")

    data = {}
    data['persons'] = data_person
    data['cars'] = data_car
    return data

#         
def ui_searh_surname():
    print('-------------------------------------------------') 
    surname = input("Введите фамилию для поиска: ") 
    while True:
        # surname = input("Введите фамилию для поиска: ")
        if surname.isalpha():
            surname = surname.capitalize()
            return surname
        else: 
            print("Некоректный ввод!")

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


def ui_change_repair():
    print('-------------------------------------------------')
    data = []
    while True:
        date = input("Введите дату ремонта: ")
        if date.isdigit() or '.' in date:
            data.append(date)
            break
        else:
            print("Некоректный ввод!")

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
   
        

# def ui_repair():        
# def ui_change():        