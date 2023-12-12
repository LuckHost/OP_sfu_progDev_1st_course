""" There is an interface, GUI of the App"""
import tkinter
from tkinter import END, W, E, Button, Label, Text, Tk
import app_functions

class App():
    """ User window class """
    def __init__(self, master):
        """ creating buttons and canvas """
        self.program_output = Label(height=10, width=45,
                                    text="Здесь будет информация")
        self.program_output.grid(row=0, columnspan=1, sticky=W+E)

        self.text_input = Text(height=2, width=5)
        self.text_input.grid(row=0, column=3, columnspan=2, sticky=W)

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

    def output(self, output_str):
        """ sets some text on the label. """
        self.program_output.config(text=output_str)
        return

    def first_but(self):
        """ gets info about an organization """
        self.output(organization.get_info())
        return

    def second_but(self):
        """ gets info about an department """
        department = self.find_dep(organization)
        if department != 0:
            self.output(department.get_info())
            return
        self.output("Отделов еще нет!")
        return

    def third_but(self):
        """ gets info about some employee """
        depart = self.find_dep(organization)
        worker = self.find_worker(depart)
        if worker != 0:
            self.output(worker.get_info())
            return
        self.output("Сотрудников еще нет!")
        return

    def fourth_but(self):
        """ add new department """
        name = self.get_correct_input("str", [], "Введите название отдела")
        purpose = self.get_correct_input("str", [], "Назначение?")
        app_functions.Department(organization, name, purpose)
        self.output("Успешно!")
        return

    def fifth_but(self):
        """ delete department from organization """
        department = self.find_dep(organization)
        department.delete(organization)
        self.output("Успешно!")
        return

    def sixth_but(self):
        """ find department and add new employee """
        department = self.find_dep(organization)
        if department == 0:
            self.output("Сначала нужно создать отдел!")
            return
        name = self.get_correct_input("str", [], "Введите имя")
        post = self.get_correct_input("str", [], "Пост сотрудника?")
        app_functions.Employee(department, name, post)
        self.output("Успешно!")
        return

    def seventh_but(self):
        """ delete employee from department """
        depart = self.find_dep(organization)
        worker = self.find_worker(depart)
        worker.delete(depart)
        self.output("Успешно!")
        return

    def eighth_but(self):
        """ exit function """
        quit()

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
