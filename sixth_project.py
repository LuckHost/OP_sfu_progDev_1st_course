""" sixth project, OP, SFU, 
completed by Khodykin Alexander
КИ23-17/2Б"""

class Organization():
    """ organization class
    base class
    contains: name, department base, documentation"""
    def __init__(self):
        """ init the organization """
        self.dep_base = {}
        self.org_name = "ООО Пошла родимая"
        self.org_doc = '''Компания по разработке универсальных
                методов и подходов проектирования
                различных сисстем оптимизации
                разработки'''

    def add_department(self, department):
        """ add a new department to organization base """
        if not department.dep_name in self.dep_base:
            self.dep_base.update({department.dep_name: department})
            return "Добавление успешно"
        return "Такой отдел уже существует!"

    def get_info(self):
        """ returns all info about organiation """
        print(f'''Название: {self.org_name},
            \rСпециализация: {self.org_doc},
            \rОтделы''')
        for i in self.dep_base:
            print(i, "\n")


class Department():
    """ department class
    contains: workers base, department name, 
    workers count and purpose"""
    def __init__(self, organization):
        """ create new deparment and add it in organiation """
        self.emp_base = {}
        self.dep_name = get_correct_input("str", [],
                                      "Введите имя отдела ")
        self.dep_emp_count = 0
        self.dep_purpose = get_correct_input("str", [],
                                      "Введите назначение отдела ")
        print(organization.add_department(self))

    def add_employee(self, employee):
        """ add a new employee to department base """
        if not employee.worker_name in self.emp_base:
            self.emp_base.update({employee.worker_name: employee})
            self.dep_emp_count = len(self.emp_base)
            return "Добавление успешно"
        return "Такой сотрудник уже существует!"

    def get_info(self):
        """ returns info about department """
        print(f'''Название: {self.dep_name},
            \rСпециализация: {self.dep_purpose},
            \rКоличество сотрудников: {self.dep_emp_count},
            \rСотрудники''')
        for i in self.emp_base:
            print(i, "\n")

    def delete(self, organization):
        """ delete department """
        del organization.dep_base[self.dep_name]

class Employee():
    """ worker class 
    contains: name, phone, mail, age, post"""
    __posts = ["Сис. администратор", "Менеджер", "Программист",
               "Директор", "Секретарь"]
    def __init__(self, department):
        self.department = department
        self.worker_name = get_correct_input("str", [],
                                      "Введите имя сотрудника")
        self.worker_phone = get_correct_input("str", [],
                                      "Введите номер сотрудника")
        self.worker_mail = get_correct_input("str", [],
                                      "Введите почту сотрудника")
        self.worker_age = get_correct_input("int", range(18, 99),
                                      "Введите возраст сотрудника")
        self.worker_post = get_correct_input("str",
                                        self.__posts,
                                      "Введите должность сотрудника")
        print(department.add_employee(self))

    def get_info(self):
        """ returns info about worker """
        print(f'''Имя: {self.worker_name},
            \nДолжность: {self.worker_post},
            \nПочта: {self.worker_mail},
            \nНомер: {self.worker_phone},
            \nВозраст: {self.worker_age},''')

    def delete(self, depart):
        """ delete worker """
        del depart.emp_base[self.worker_name]

def get_correct_input(value_type = "str",
                       posbl_value = None, usr_str = "Введите значение"):
    """ returns correct input values (int or string)"""
    while True:
        inp_value = input(usr_str)
        if value_type == "str" and \
        (inp_value in posbl_value
         or posbl_value == []):
            return inp_value
        if value_type == "int":
            try:
                int_inp_value = int(inp_value)
                if int_inp_value in posbl_value:
                    return int_inp_value
            except ValueError:
                pass
        print("Неправильный ввод,\n Повторите попытку")

def find_dep(organization):
    """ find department in organization and return it """
    departs = organization.dep_base
    if len(departs) == 0:
        print("Отделов еще нет!")
        return 0
    dep_names = departs.keys()
    dep_name = get_correct_input("str", dep_names, "Введите название отдела ")
    return departs[dep_name]

def find_worker(organization):
    """ find worker in some department and return it """
    depart = find_dep(organization)
    if depart == 0:
        return 0
    workers_names = depart.emp_base.keys()
    if len(workers_names) == 0:
        print("Сотрудников еще нет!")
        return 0
    worker_name = get_correct_input("str",
                                     workers_names, "Введите имя сотрудника ")
    return depart.emp_base[worker_name]

def user_menu():
    """ returns a task number """
    while True:
        print("Выберете действие:\n",
              "1 - Вывести информацию об организациии\n",
              "2 - Вывести информацию об отделе\n",
              "3 - Вывести информацию о сотруднике\n",
              "4 - Добавить отдел\n",
              "5 - Удалить отдел\n",
              "6 - Добавить сотрудника\n",
              "7 - Удалить сотрудника\n",
              "8 - Выход\n")
        return get_correct_input("int", [1, 2, 3, 4, 5, 6, 7, 8],
                                "Введите номер действия: ")

def main():
    """ the main method that does the main functions 
    царская документация """
    organization = Organization()
    while True:
        task = user_menu()
        match task:
            case 8:
                break
            case 1:
                organization.get_info()
            case 4:
                Department(organization)
            case 2:
                department = find_dep(organization)
                if department != 0:
                    department.get_info()
            case 3:
                worker = find_worker(organization)
                if worker != 0:
                    worker.get_info()
            case 5:
                department = find_dep(organization)
                if department != 0:
                    department.delete(organization)
            case 6:
                department = find_dep(organization)
                Employee(department)
            case 7:
                worker = find_worker(organization)
                if worker != 0:
                    worker.delete(worker.department)

if __name__ == "__main__":
    main()
