""" something like a backend of the App"""
class Organization():
    """ base class that contains all departments"""
    def __init__(self):
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
        """ returns information about organization """
        output = f'''Название: {self.org_name},
            \rСпециализация: {self.org_doc},
            \rОтделы:'''
        for i in self.dep_base:
            output += f"{i}; "
        return output

class Department():
    """ Deaprtment class contains employees
    base and department info """
    def __init__(self, organization, name, purpose):
        self.emp_base = {}
        self.dep_name = str(name)
        self.dep_emp_count = 0
        self.dep_purpose = str(purpose)
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
        output = f'''Название: {self.dep_name},
            \rСпециализация: {self.dep_purpose},
            \rКоличество сотрудников: {self.dep_emp_count},
            \rСотрудники: '''
        for i in self.emp_base:
            output += f"{i}; "
        return output

    def delete(self, organization):
        """ delete department """
        del organization.dep_base[self.dep_name]

class Employee():
    """ Employee class contains info
    about one employee """
    def __init__(self, department, name, post):
        self.department = department
        self.worker_name = name
        self.worker_post = post
        print(department.add_employee(self))

    def get_info(self):
        """ returns info about worker """
        return f'''Имя: {self.worker_name},
            \nДолжность: {self.worker_post}'''

    def delete(self, depart):
        """ delete worker """
        del depart.emp_base[self.worker_name]
        depart.dep_emp_count = len(depart.emp_base)
