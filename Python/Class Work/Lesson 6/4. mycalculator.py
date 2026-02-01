# Робимо функцію, яка буде реалізовувати калькулятор
def my_calculator():
    a = input("Вкажіть значення a: ")
    b = input("Вкажіть значення b: ")
    intA = int(a)
    intB = int(b)
    print(f"{a} + {b} = {intA + intB}")
    print(f"{a} - {b} = {intA - intB}")
    print(f"{a} * {b} = {intA * intB}")
    if intB==0:
        print("Має спробу ділення на 0")
    else:
        print(f"{a} / {b} = {intA / intB}")

my_calculator()