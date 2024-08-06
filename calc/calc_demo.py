def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"
    
# Def — это зарезервированное слово в языке программирования Python,
# которое используется для определения функций.
# Функции позволяют дать имя определённому блоку команд, чтобы впоследствии запускать этот блок
# по указанному имени в любом месте программы и сколь угодно много раз.

class a:
    sembrbr = 15
    s = "В этом предложении только 38 символов."
    
    

# def test_class():
#     print("test", a != None)

# def TestClassA():
#     return isinstance(a, int | str )


def testClass():
    return a.s 

print(testClass())