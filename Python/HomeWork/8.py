print("\n-------Рівень один-------\n")
print("\n-----Перше завдання-----\n")



firstNum = int(input("Введіть перше число: "))
secondNum = int(input("Введіть друге число: "))

for i in range(firstNum, secondNum):
    if( i % 7 == 0):
        print(i)



print("\n-----Друге завдання-----\n")



for i in range(firstNum, secondNum):
    print(i)



print("\n----------\n")



for i in range(secondNum, firstNum -1, -1):
    print(i)



print("\n----------\n")



for i in range(firstNum, secondNum):
    print(i) 



print("\n----------\n")



count = 0

for i in range(firstNum, secondNum):
    if( i % 5 == 0):
        count += 1
        print(count)



print("\n-------Рівень два-------\n")



print("\n-----Перше завдання-----\n")

for i in range(firstNum, secondNum):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



print("\n-----Друге завдання-----\n")

user = int(input(" 1 = прямий порядорк введення \n 2 = зворотній порядок"))

if user == 1:
    for i in range(firstNum, secondNum + 1, 7):
        print(i)
else:
    for i in range(secondNum, firstNum - 1, -7):
        print(i)



print("\n-------Рівень три-------\n")



print("\n-------Перше завдання-------\n") 

# -світло