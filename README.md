#### Attention!
This markdown file contains a description in two languages. If it's convenient for you to continue in English, just read on.

Этот файл содержит описание на двух языках. Если вам удобнее читать на русском, пролистайте примерно в середину документа.

---
# First semester projects

This repository contains all projects of the Fundamentals of Programming course from the first semester of Faculty of Software Engineering (computer science) of SibFU. 

## Project 1

__Task:__ Write a program that calculates the *n*th generalized Fermat number using the formula:
$$x(n)=a^i+b^i,$$
$$2 ≤ a, 1 ≤ b, 0 ≤ b$$ 
Where 
$$i = 2^n$$ 
And check the divisibility of the resulting number by 2, 3 and 5.

__Input Values:__ numbers *a*, *b* and *n*
__Export:__ The *n*th number of the sequence, the message about
the divisibility of the received number.

__Description:__
This project tested basic knowledge about working with the IDE. A fairly simple task with an equally simple solution.

__Usage exaple__:

![](markdown_images/1st_pr_output.png)

## Project 2
__Task:__ In a randomized two-dimensional array find all the necessary values:
1) Find the number of "1"
2) Find the number of "0"
3) Find the number of "1" and "0" in a given row

__Input values:__ Action number. 
__Export:__ Some number.

__Description:__
This practical work was aimed at studying arrays. The functions are simple, there are no complicated points in the logic of the code. Instead of the ones and zeros that are specified in the task, sold and free tickets are used.

__Usage example:__

![](markdown_images/2nd_pr_output.png)

## Project 3
__Task:__ Write a selection sort function. 

__Input values:__ Array of numbers.
__Export:__ Sorted array.

__Description:__
In this practical work the simplest sorting function was written. In addition, there are few menu and input check functions. 
Sort function:
```
def selection_sort(arr):
    """ sorts by choise """
    arr_lenght = len(arr)
    for i in range(arr_lenght):
        min_index = i
        for j in range(i+1, arr_lenght):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

__Usage example:__

![](markdown_images/3rd_pr_output.png)

## Project 4
__Task:__ 
Write a programm that stores information about universities.
Structure: Name, opening year, amount of faculties, number of students. 
The program must let:
+ Download information from a file
+ Search for a university by name
+ Filter for a universities by the number of students
+ Add new universities
+ Delete universities
+ Save information in a file

Use the _json_ module to complete the task.

__Input values:__ The task number.
__Export:__ The necessary information.

__Description:__
All tasks are separated by function. There is a _json_ file named "data.json". There is a dictionary with universities information in this file. As always, the Menu function and input verification have been added in the program.

__Usage example:__

![](markdown_images/4th_pr_output.png)

## Project 5 

There is some problem with projects numeration in my course. Because of this, I just made this empty project. But it is still a very important project in my education.

__The whole code:__
```
print(":DDDDDDDD:")
print("it's like :) and ):")
print("Mio the best")
```

## Project 6 
__Task:__
Write a program that stores information about the organization, employees, and departments. There are a number of departments in the organization, each of which has a number of workers at different posts.
Develop and implement a class diagramm and all the necessary methods and functions.

__Input values:__ The task number.
__Export:__ The necessary information.

__Description:__
That was my first project with classes. 
It contains three classes. Each of which contains arguments:
+ Organization
    + Departments database 
    + Organization name
    + Docstring
+ Department 
    + Employees database
    + Department name 
    + Number of workers 
    + The department`s purpose
+ Employee
    + Name
    + Work phone number
    + E-mail
    + Age
    + Post

The program allows the user to get information about the organization, department and employee. In addition it allows add and delete departments and employees from databases. By database, I mean a dictionary with class objects.

__Diagram:__

![](markdown_images/6th_pr_diagram.png)

__Usage example:__

![](markdown_images/6th_pr_output.png)

## Project 7

__Task:__ 
Implement a GUI by using GUI library 
Place the implementation of the graphical interface in a separate file.

__Description:__
The Tkinter library was used in this project. In addition, the entire graphics module works on the principle of OOP. The basis of the program is taken from project 6

__Usage example:__

![](markdown_images/7th_pr_output.png)

---
#Проекты 1-го семестра

Еще в разработке :D