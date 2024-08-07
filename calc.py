# для начала нужно подключить библиотеки 
from tkinter import *
from tkinter import ttk

# нужно создать функции через def, можно будет потом вызывать эту функцию

def add():
    return entry_number_1 + entry_number_2

def subtract():
     return entry_number_1.get() - entry_number_2.get()

def multiply():
     return entry_number_1.get() * entry_number_2.get()

def divide():
     return entry_number_1.get() / entry_number_2.get()

answer = 0

# сам код калькулятора, надеюсь не нужно обьяснять
def calculate():
    if (combo.get() == '+'):
          answer = int(entry_number_1.get()) + int(entry_number_2.get())
    if (combo.get() == '-'):
          answer = int(entry_number_1.get()) - int(entry_number_2.get())
    if (combo.get() == '*'):
          answer = int(entry_number_1.get()) * int(entry_number_2.get())
    if (combo.get() == '/', entry_number_2 == 0):
          answer = "На ноль делить нельзя"
    if (combo.get() == '/'):
          answer = int(entry_number_1.get()) / int(entry_number_2.get())
    

    label_3.configure(text=answer) # заменить текст на ответ
     
     



# тест на существование функций
def testFunction():
    return add != None, subtract != None, multiply != None, divide != None

print("Test 1, Function: ",testFunction())

# необходимо создать окно приложения, его заголовок и размер

window = Tk()
window.title("Калькулятор")
window.geometry('300x400')


# необходимо создать текст через метод pack
label_1 = Label(window, text = "Введите первое число:")
label_1.pack()

# необходимо создать поле для ввода текста (метод pack сам разместит элементы)
entry_number_1 = Entry(window)
entry_number_1.pack()

label_2 = Label(window, text = "Введите второе число:")
label_2.pack()

entry_number_2 = Entry(window)
entry_number_2.pack()

# можно выбрать несколько значений, ComboBox
combo = ttk.Combobox(window, width=17)
combo['values'] = ('+', '-', '*', '/')
combo.current(0) # по умолчанию выбран +
combo.pack()

# необходимо создать кнопку 
button = ttk.Button(text="Расчитать", command=calculate)
button.pack()
 
# поле для вывода ответа
label_3 = Label(window, text="Ответ= ", ) 
label_3.pack()

# бесконечный цикл, чтобы окно не исчезало
window.mainloop() 