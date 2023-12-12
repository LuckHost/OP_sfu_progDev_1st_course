""" There is an interface, GUI of the App"""
import tkinter
from tkinter import END, W, E, Button, Scrollbar, Text, Tk
import app_functions

class App():
    """ User window class """
    def __init__(self, master):
        """ creating buttons and canvas """
        self.program_output = Text(height=10, width=45,
                                    bg="#D9D8D7")
        self.program_output.insert(1.0, "Здесь будет информация о программе")
        self.program_output.grid(row=0, sticky=W+E, columnspan=3)
        self.scroll = Scrollbar(command=self.program_output.yview)
        self.scroll.grid(row=0, column=2, sticky=E)
        self.program_output.config(yscrollcommand=self.scroll.set)

        self.text_input = Text(height=2, width=15)
        self.text_input.grid(row=0, column=3, columnspan=2, sticky=W)
        self.buttons_initilize(master)

    def buttons_initilize(self, master):
        """ initilize buttons on window """
        self.but = Button(master, text="Вывести информацию об\nорганизациии",
                          command=self.first_but).grid(column=0, row=2)
        self.but1 = Button(master, text="Вывести информацию\nоб отделе",
                           command=self.second_but).grid(column=0, row=3)
        self.but2 = Button(master, text="Вывести информацию\nо сотруднике",
                           command=self.third_but).grid(column=1, row=2)
        self.but3 = Button(master, text="Добавить отдел",
                           command=self.fourth_but).grid(column=1, row=3)
        self.but4 = Button(master, text="Удалить отдел",
                           command=self.fifth_but).grid(column=2, row=2)
        self.but5 = Button(master, text="Добавить сотрудника",
                           command=self.sixth_but).grid(column=2, row=3)
        self.but6 = Button(master, text="Удалить сотрудника",
                           command=self.seventh_but).grid(column=3, row=2)
        self.but7 = Button(master, text="Выход",
                           command=self.eighth_but).grid(column=3, row=3)
        self.but8 = Button(master, text="О программе",
                           command=self.ninth_but).grid(column=2, row=4)
        
    def output(self, output_str):
        """ sets some text on the label. """
        self.program_output.delete(1.0, END)
        return self.program_output.insert(1.0, output_str)

    def first_but(self):
        """ gets info about an organization """
        return self.output(organization.get_info())

    def second_but(self):
        """ gets info about an department """
        department = self.find_dep(organization)
        if department != 0:
            return self.output(department.get_info())
        return self.output("Отделов еще нет!")

    def third_but(self):
        """ gets info about some employee """
        depart = self.find_dep(organization)
        worker = self.find_worker(depart)
        if worker != 0:
            return self.output(worker.get_info())
        return self.output("Сотрудников еще нет!")

    def fourth_but(self):
        """ add new department """
        name = self.get_correct_input("str", [], "Введите название отдела")
        purpose = self.get_correct_input("str", [], "Назначение?")
        app_functions.Department(organization, name, purpose)
        return self.output("Успешно!")

    def fifth_but(self):
        """ delete department from organization """
        department = self.find_dep(organization)
        department.delete(organization)
        return self.output("Успешно!")

    def sixth_but(self):
        """ find department and add new employee """
        department = self.find_dep(organization)
        if department == 0:
            return self.output("Сначала нужно создать отдел!")
        name = self.get_correct_input("str", [], "Введите имя")
        post = self.get_correct_input("str", [], "Пост сотрудника?")
        app_functions.Employee(department, name, post)
        return self.output("Успешно!")

    def seventh_but(self):
        """ delete employee from department """
        depart = self.find_dep(organization)
        worker = self.find_worker(depart)
        worker.delete(depart)
        return self.output("Успешно!")

    def eighth_but(self):
        """ exit function """
        quit()

    def ninth_but(self):
        """ retuns app info """
        return self.output("""Программа написана Ходыкиным алксандром
                           Группа: КИ23-17/2Б
                           Программа предназначена для хранения
                           данных об организации, ее отдела и сотрудниках""")

    def find_dep(self, organization):
        """ finds a department by user input """
        departs = organization.dep_base
        if len(departs) == 0:
            return 0
        dep_names = departs.keys()
        dep_name = self.get_correct_input("str",
                                dep_names, "Введите название отдела ")
        return departs[dep_name]

    def find_worker(self, depart):
        """ finds an employee by user input """
        if depart == 0:
            return 0
        workers_names = depart.emp_base.keys()
        if len(workers_names) == 0:
            return 0
        worker_name = self.get_correct_input("str",
                                workers_names, "Введите имя сотрудника ")
        return depart.emp_base[worker_name]

    def get_correct_input(self, inp_type = "str",
                          posbl_value = [], usr_str = "Введите значение"):
        """ returns correct input values (int or string)"""
        while True:
            self.output(usr_str)
            inp_value = tkinter.StringVar()
            self.inp_but = Button(text="Записать",
                          command=lambda:
                              inp_value.set(self.text_input.get(1.0, END)))
            self.inp_but.grid(row=0, column=5, columnspan=2, sticky=W)
            self.inp_but.wait_variable(inp_value)
            inp_value =  inp_value.get()
            if inp_type == "str" and\
            (inp_value in posbl_value
            or posbl_value == []):
                return inp_value
            if inp_type == "int":
                try:
                    int_inp_value = int(inp_value)
                    if int_inp_value in posbl_value:
                        return int_inp_value
                except ValueError:
                    pass
            self.output("Неправильный ввод,\n Повторите попытку")

def main():
    """main function -  Royal documentation"""
    root = Tk()
    root.geometry("800x300")
    App(root)
    root.mainloop()

if __name__ == "__main__":
    organization = app_functions.Organization()
    main()
