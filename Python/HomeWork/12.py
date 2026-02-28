print("\n ----- Завдання 1 -----\n")

def show_name():
    # Просимо користувача ввести прізвище
    surname = input("Введіть прізвище: ")
    
    # Просимо користувача ввести ім'я
    name = input("Введіть ім'я: ")
    
    # Виводимо результат
    print("Прізвище та ім'я:", surname, name)


# Викликаємо функцію
show_name()

print("\n ----- Завдання 2 -----\n")

def print_numbers(n):
    # Проходимо циклом від 0 до n включно
    for i in range(0, n + 1):
        print(i, end=" ")  # end=" " щоб числа були в один рядок


# Вводимо число
number = int(input("Введіть число: "))

# Викликаємо функцію
print_numbers(number)

print("\n ----- Завдання 3 -----\n")

def find_min_max(numbers):
    # Знаходимо мінімальне значення
    minimum = min(numbers)
    
    # Знаходимо максимальне значення
    maximum = max(numbers)
    
    # Виводимо результат
    print("Мінімальне значення:", minimum)
    print("Максимальне значення:", maximum)


# Вводимо список чисел через пробіл
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# Викликаємо функцію
find_min_max(numbers)