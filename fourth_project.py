""" importing json to work with json files"""
import json

def get_correct_inp(list_of_values, menu_str = "Введите значение.. "):
    """ returns correct input in list_of_values range"""
    while True:
        try:
            value = int(input(menu_str))
            if value in list_of_values:
                return value
            print("Ввод инкорректен, повторите")
            continue
        except ValueError:
            print("Ввод инкорректен, повторите")

def user_menu():
    """ returns a task number """
    while True:
        print("Выберете действие:\n",
              "1 - Загрузить информацию из файла\n",
              "2 - Поиск по названию\n",
              "3 - Фильтр по количеству студентов\n",
              "4 - Добавить запись\n",
              "5 - Удалить запись\n",
              "6 - Сохранить\n",
              "7 - Выход\n")
        return get_correct_inp([1, 2, 3, 4, 5, 6, 7],
                                "Введите номер действия: ")

def first_task():
    """ get dict from the file """
    path = input("Укажите путь до файла: ")
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Что-то пошло не так,",
              " проверьте указанный путь")
        return None

def second_task(data, name = "СФУ"):
    """ find dict by name """
    if name in data:
        print("Имя: "+ name + "\n",
              "Дата открытия: ", data[name]["opening year"]+ "\n",
              "Количество факультетов: ", data[name]["faculties"]+ "\n",
            "Количество студетов: ", data[name]["students"])
        return True
    print("Вуза ", name, " нет в списке")
    return False

def third_task(data, number, operation):
    """ students count filter """
    for i in data:
        # operation = True --> ">"
        # False --> "<"
        if (int(data[i]["students"]) > number) == operation:
            print(i, " ", data[i])

def fourth_task(data):
    """ add new object """
    unv_name = input("Введите название вуза: ")
    if unv_name in data:
        print("Данный вуз уже есть в списке!\n")
        return 0
    open_year = input("Введите дату открытия: ")
    facult = input("Введите количество факультетов: ")
    stud = input("Введите количество студентов: ")

    data.update({unv_name : {"opening year":open_year,
                             "faculties":facult, "students":stud}})
    return 0

def fifth_task(data, name):
    """ delete object """
    if second_task(data, name):
        usr_decis = get_correct_inp([0, 1],
                 "Вы действительно хотите удалить запись?" + "\n"+
                 "0 - нет \n1 - да\n")
        if usr_decis == 1:
            data.pop(name)

def main():
    """ Main function """
    print("\nВас приветствует программа по работе",
          "с файлами в python")
    print("Практическую выполнил Ходыкин Александр\n")
    data =  {"СФУ" : {"opening year":"2006",
                      "faculties":"96", "students":"15000"}}
    while True:
        task = user_menu()
        if task == 1:
            temp_data = first_task()
            if not temp_data is None:
                data = temp_data
        if task == 2:
            second_task(data, input("Введите название ВУЗа: "))
        if task == 3:
            operation = get_correct_inp([1, 2],
                                        "Введите операцию\n"
                                        "1 - >\n" +
                                        "2 - <\n")
            number = get_correct_inp(range(0, 100000), "Введите число: ")
            if operation == 2:
                third_task(data, number, False)
            else:
                third_task(data, number, True)
        if task == 4:
            fourth_task(data)
        if task == 5:
            fifth_task(data, input("Введите название ВУЗа: "))
        if task == 6:
            with open("data.json", "w", encoding="utf-8") as write_file:
                json.dump(data, write_file)
        if task == 7:
            break

if __name__ == "__main__":
    main()
