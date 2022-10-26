import logger as log

st_num = []

def init(st):
    global st_num
    st_num.append(st)

def print_res(data):
    print('-------------------------------------------------')
    person_tuple = ('id', 'Фамилия', 'Имя', 'Дата рождения', 'Телефон')
    car_tuple = ('Марка', 'Модель', 'Гот выпуска', 'Пробег', 'VIN', 'Гос. номер')
    repair_tuple = ('Дата ремонта', 'Перечень работ', 'Стоимость')
    index = 0
    if len(data[0]) == 5:
        
        for i in range(len(data)):
            index = 0
            for j in range(len(data[i])):
                print(f'{person_tuple[index]}: {data[i][j]}')
                index +=1
            print('-------------------------------------------------')
    elif len(data[0]) == 8:
       
        for i in range(len(data)):
            index = 0
            init(st_num.append(data[i][6]))
            init(data[i][6])
            for j in range(1, len(data[i]) - 1):
                print(f'{car_tuple[index]}: {data[i][j]}')
                index +=1
            print('-------------------------------------------------')
       
    else: 
        for i in range(len(data)):
            index = 0
            print(f'{car_tuple[5]}: {st_num[i]}')
            for j in range(len(data[i]) - 1):
                print(f'{repair_tuple[index]}: {data[i][j]}')
                index +=1
            print('-------------------------------------------------')
        
    