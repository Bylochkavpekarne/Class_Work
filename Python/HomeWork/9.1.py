print("\n-----Перший рівень-----\n")



print("\n-----Перше завдання-----\n")



user_input = input("Введіть числа через пробіл: ")
ints = list(map(int, user_input.split()))

even_count = 0
odd_count = 0

for item in ints:
    if item % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nСписок чисел:", ints)
print(f"Кількість парних чисел: {even_count}")
print(f"Кількість непарних чисел: {odd_count}")



print("\n-----Друге завдання-----\n")



user_input = input("Введіть числа через пробіл: ")

numbers = list(map(int, user_input.split()))

max_num = max(numbers)
min_num = min(numbers)

print(f"Найбільше число: {max_num}")
print(f"Найменше число: {min_num}")



print("\n-----Другий рівень-----\n")



print("\n-----Перше завдання-----\n")



user_input = input("Введіть числа через пробіл: ")
numbers = list(map(int, user_input.split()))

positive = []
negative = []
zero_count = 0

for n in numbers:
    if n > 0:
        print(f"{n} - додатне число")
        positive.append(n)
    elif n < 0:
        print(f"{n} - від'ємне число")
        negative.append(n)
    else:
        print(f"{n} - нуль")
        zero_count += 1

pos_count = len(positive)
neg_count = len(negative)

if positive:
    min_positive = min(positive)
else:
    min_positive = None

if negative:
    max_negative = max(negative)
else:
    max_negative = None

print("\n--- Результати ---")
print(f"Кількість додатних: {pos_count}")
print(f"Кількість від'ємних: {neg_count}")
print(f"Кількість нулів: {zero_count}")



print("\n-----Друге завдання-----\n")



numbers = list(map(int, input("Введіть список цілих чисел: ").split()))
x = int(input("Введіть число для порівняння: "))

result = []

for n in numbers:
    if n >= x:
        result.append(n)

print("Результат (елементи, не менші за задане число):")
print(result)

# -світло