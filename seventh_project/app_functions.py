import interface

class Organization():
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
        output = f'''Название: {self.org_name}, 
            \rСпециализация: {self.org_doc},
            \rОтделы:'''
        for i in self.dep_base:
            output += f"{i}; "
        return output


class Department():
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
    __posts = ["Сис. администратор", "Менеджер", "Программист",
               "Директор", "Секретарь"]
    def __init__(self, department, name, post):
        self.department = department
        self.worker_name = name
        self.worker_post = post
        print(department.add_employee(self))
    
    def get_info(self):
        """ returns info about worker """
        return f'''Имя: {self.worker_name}, 
            \nДолжность: {self.worker_post},
            \nПочта: {self.worker_mail},
            \nНомер: {self.worker_phone},
            \nВозраст: {self.worker_age},'''
        
    def delete(self, depart):
        """ delete worker """
        del depart.emp_base[self.worker_name]    


def main():
    """ the main method that does the main functions """
    """ царская документация """
    organization = Organization()
    is_running = True
    while is_running:
        task = user_menu()
        if task == 8:
            break
        if task == 1:
            organization.get_info()
        if task == 4:
            Department(organization)
        if task == 2: 
            department = find_dep(organization)
            if department != 0: department.get_info()
            else: return "Отделов еще нет!"
        if task == 3:
            worker = find_worker(organization)
            if worker != 0: worker.get_info()
            else: return "Сотрудников еще нет!"
        if task == 5:
            department = find_dep(organization)
            if department != 0: department.delete(organization)
        if task == 6:
            department = find_dep(organization)
            Employee(department)
        if task == 7:
            worker = find_worker(organization)
            if worker != 0: worker.delete(worker.department)

    

if __name__ == "__main__":
    main()