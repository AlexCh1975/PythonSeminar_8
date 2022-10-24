
def print_res(data):
    print('-------------------------------------------------')
    # print(data[0])
    # exit()
    person_tuple = ('id', 'Фамилия', 'Имя', 'Дата рождения', 'Телефон')
    car_tuple = ('Марка', 'Модель', 'Гот выпуска', 'Пробег', 'VIN', 'Гос. номер')
    repair_tuple = ('Дата ремонта', 'Перечень работ', 'Стоимость')
    index = 0
    if len(data[0]) == 5:
        # for i in data[0]:
        #     print(f'{person_tuple[index]}: {i}')
        #     index += 1
        for i in range(len(data)):
            index = 0
            for j in range(len(data[i])):
                print(f'{person_tuple[index]}: {data[i][j]}')
                index +=1
            print('-------------------------------------------------')
    elif len(data[0]) == 8:
        # temp = []
        # for i in range(1, len(data[0]) - 1):
        #     temp.append(data[0][i])
        # # print(temp)
        # for i in temp:
        #     print(f'{car_tuple[index]}: {i}')
        #     index += 1
        for i in range(len(data)):
            index = 0
            for j in range(1, len(data[i]) - 1):
                print(f'{car_tuple[index]}: {data[i][j]}')
                index +=1
            print('-------------------------------------------------')
    else:    
        for i in range(len(data)):
            index = 0
            for j in range(len(data[i]) - 1):
                print(f'{repair_tuple[index]}: {data[i][j]}')
                index +=1
            print('-------------------------------------------------')