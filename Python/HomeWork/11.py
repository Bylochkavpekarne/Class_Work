print("\n ----- Рівень 1 -----\n")

print("\n ----- Завдання 1 -----\n")

# Вводимо список чисел через пробіл і перетворюємо їх у тип int
numbers = list(map(int, input("Введіть цілі числа через пробіл: ").split()))

count = 0 # Змінна для підрахунку кількості більших елементів

# Проходимо по списку, починаючи з другого елемента
for i in range(1, len(numbers)):
    # Якщо поточний елемент більший за попередній
    if numbers[i] > numbers[i -1]:
        count += 1 # Збільшуємо лічильник

print(f"Кількість елементів: {count}")

print("\n ----- Завдання 2 -----\n")

# Вводимо список чисел
numbers = list(map(int, input("Введіть цілі числа через пробіл: ").split()))

result = [] # Список для збереження унікальних елементів

# Перебираємо кожен елемент списку
for num in numbers:
    # Якщо число зустрічається рівно один раз
    if numbers.count(num) == 1:
        result.append(num) # Додаємо його до результату

# Виводимо список унікальних елементів
print("Елементи, які зустрічаються один раз:", result)

print("\n ----- Рівень 2 -----\n")

print("\n ----- Завдання 1 -----\n")

# Вводимо список чисел
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

max_seq = []  # Найдовша знайдена послідовність
current_seq = [numbers[0]]  # Поточна послідовність (починаємо з першого елемента)

# Проходимо по списку з другого елемента
for i in range(1, len(numbers)):
    # Якщо поточне число більше за попереднє
    if numbers[i] > numbers[i - 1]:
        current_seq.append(numbers[i])  # Додаємо до поточної послідовності
    else:
        # Якщо послідовність перервалась
        if len(current_seq) > len(max_seq):
            max_seq = current_seq  # Оновлюємо максимальну
        current_seq = [numbers[i]]  # Починаємо нову послідовність

# Перевірка після завершення циклу
if len(current_seq) > len(max_seq):
    max_seq = current_seq

# Виводимо довжину та саму послідовність
print("Довжина послідовності:", len(max_seq))
print("Послідовність:", max_seq)

print("\n ----- Завдання 2 -----\n")

# Вводимо список чисел
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# Вводимо кількість позицій для зсуву
n = int(input("Введіть кількість позицій: "))

# Щоб зсув був правильним навіть якщо n більше довжини списку
n = n % len(numbers)

# Робимо зсув вправо
shifted = numbers[-n:] + numbers[:-n]

# Виводимо результат
print("Зсунутий список:", shifted)

print("\n ----- Рівень 3 -----\n")

print("\n ----- Завдання 1 -----\n")

import random  # Імпортуємо модуль для випадкових чисел

# Створюємо два списки по 5 випадкових чисел від 1 до 10
list1 = [random.randint(1, 10) for _ in range(5)]
list2 = [random.randint(1, 10) for _ in range(5)]

print("Список 1:", list1)
print("Список 2:", list2)

# 1. Об'єднання двох списків
union = list1 + list2
print("Об'єднаний список:", union)

# 2. Об'єднання без повторень (через множину)
no_duplicates = list(set(union))
print("Без повторень:", no_duplicates)

# 3. Спільні елементи
common = list(set(list1) & set(list2))
print("Спільні елементи:", common)

# 4. Унікальні елементи кожного списку
unique = list(set(list1) ^ set(list2))
print("Унікальні елементи:", unique)

# 5. Мінімум і максимум кожного списку
min_max = [min(list1), max(list1), min(list2), max(list2)]
print("Мінімум і максимум:", min_max)