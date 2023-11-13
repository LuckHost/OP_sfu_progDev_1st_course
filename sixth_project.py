class Organization():
    org_name = "ООО Пошла родимая"
    org_doc = "Компания по разработке универсальных\
        методов и подходов проектирования\
            различных сисстем оптимизации\
                разработки"
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance == super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        pass

    dep_base = {}

class Department(Organization):
    emp_base = {}
    def __new__(cls, *args, **kwargs):
        pass
    
    @classmethod
    def add_emp(cls, employee, emp_name):
        cls.dep_base.update(emp_name, employee)
        
        

class Employee(Department):
    def __init__(cls, *args, **kwargrs):
        worker_name = "Акакий"
        worker_phone = "88005553535"
    pass

def get_correct_input(type = "str", posbl_value = [], usr_str = "Введите значение"):
    while True:
        inp_value = input(usr_str)
        if type == "str" and inp_value in posbl_value:
            return inp_value
        if type == "int":
            try:
                int_inp_value = int(inp_value)
                if int_inp_value in posbl_value:
                    return int_inp_value
            except ValueError:
                pass
        print("Неправильный ввод,\nПовторите попытку")

def main():
    """ main methood """
    """ царская документация """
    pass

if __name__ == "__main__":
    main()