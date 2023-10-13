""" import random to
make randomized array """
import random

def get_correct_input(var_type, frase):
    """ returns correct input value """
    if var_type == 'int':
        value = 0
        while True:
            input_value = input(frase)
            try:
                value = int(input_value)
                return value
            except ValueError:
                print("Ввод инкорректен, повторите..")
    else:
        return input_value

def array_creator():
    """ returns randomazed array """
    rows = get_correct_input("int", "Введите количество рядов ")
    columns = get_correct_input("int", "Введите количество мест в ряду ")
    places = []
    for _ in range(rows):
        random_row = []
        for _ in range(columns):
            random_row.append(random.randint(0, 1))
        print(random_row)
        places.append(random_row)
    return places

def places_calculater(places, operation):
    """ returns count of sold places if 2nd 
    argument is False and of free places if it's True"""
    places_calculater_count = 0
    for i in places:
        for j in i:
            places_calculater_count += j
    if operation:
        return len(places) * len(places[0]) \
            - places_calculater_count
    return places_calculater_count

def row_calculator(places):
    """ returns information about the row """
    row_number  = get_correct_input("int", "Введите номер ряда ")
    if row_number - 1 > len(places):
        print("Данного ряда не существует")
        return 0
    free_places = 0
    sold_places = 0
    for i in places[row_number-1]:
        if i != 0:
            sold_places += 1
        else:
            free_places += 1
    print(f"В этом ряду \n \
    Свободных мест: {free_places} \n \
    Проданных мест: {sold_places} \n")
    return 0

def main():
    """ the main function """
    places = array_creator()
    while True:
        task = input("Введите команду:\n\
Посчитать \n \
    a) количество проданных билетов на сеанс \n \
    b) количество свободных мест \n \
    c) количество билетов в заданном ряду \n")
        if task not in \
            ['a', 'b', 'c', 'exit']:
            print("Ввод инкорректен! \n Повторите попытку..")
            continue
        if task == 'exit':
            break
        if task == 'a':
            places_value = places_calculater(places, False)
            print(f"Количество проданных мест: {places_value}\n")
        elif task == 'b':
            places_value = places_calculater(places, True)
            print(f"Количество свободных мест: {places_value}\n")
        elif task == 'c':
            row_calculator(places)

if __name__ == "__main__":
    main()
