# для начала нужно подключить библиотеки 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# нужно создать функции через def, можно будет потом вызывать эту функцию

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y 

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y

# тест на существование функций
def testFunction():
    return add != None, subtract != None, multiply != None, divide != None

print("Test Function: ",testFunction())

# необходимо создать окно приложения, его заголовок и размер

