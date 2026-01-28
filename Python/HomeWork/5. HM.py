print("---Калькулятор---")
a = int(input("Введіть перше число: ")) # вводимо перше число
b = int(input("Введіть друге число: ")) # вводимо друге число
c = input("Введіть дію + , - , * , / ") # вводимо дію
if c == "/" and b == 0: # якщо у с обрана дія / і у b обране число 0
    print("Ви не можете ділити на 0") # тоді буде вивід: Ви не можете ділити на 0
elif c == "+":
    d = a + b
    print(f"a + b = {d}")
elif c == "-":
    d = a - b
    print(f"a - b = {d}")   
elif c == "*":
    d = a * b
    print(f"a * b = {d}")   
elif c == "/":
    d = a / b
    print(f"a / b = {d}")








'''
c = a - b
print(f"a - b = {c}")
c = a + b
print(f"a + b = {c}")
c = a * b
print(f"a * b = {c}")
c = a / b
print(f"a / b = {c}")
'''