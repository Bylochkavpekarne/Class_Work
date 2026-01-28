print("\n-----Школа----\n")

count = 0

while True:

    age = input("Введіть вік учнів: ")
    age = int(age)



    if age > 100:
        print("Программа стикнулася із критичною помилкою! Робота не можлива!")
        break
    if age < 18:
        count += 1
    else:
        continue # якщо це не є дитина школи - print - буде виводитися, якщо if працює
    print(f"Дитині зараз {age} до повноліття лишилося {18-age} років")

print("Кількість дітей школи: ", count)
