# Функція для запису нового абонента у файл
def writeFileAbonent():
    # Отримуємо дані від користувача
    lastName = input("Вкажіть прізвище: ")
    firstName = input("Вкажіть ім'я: ")
    soName = input("Вкажіть побатькові: ")
    phone = input("Вкажіть телефон: ") 
    address = input("Вкажіть адресу: ")
    
    # Відкриваємо файл у режимі 'a' (append) — додавання в кінець файлу без видалення старого вмісту
    fileWriter = open("abonents.txt", 'a', encoding="utf-8")
    
    # Записуємо кожне поле з нового рядка (всього 5 рядків на одного абонента)
    fileWriter.write(f"{lastName}\n")
    fileWriter.write(f"{firstName}\n")
    fileWriter.write(f"{soName}\n")
    fileWriter.write(f"{phone}\n")
    fileWriter.write(f"{address}\n")
    
    # Закриваємо файл, щоб зберегти зміни
    fileWriter.close()

# Функція для повного очищення файлу
def clearFileAbonents():
    # Режим 'w' (write) відкриває файл і одразу видаляє весь його вміст
    fileWriter = open("abonents.txt", 'w', encoding="utf-8")
    fileWriter.close()

# Функція для читання та виведення всіх абонентів
def readFileAbonents():
    try:
        fileRead = open("abonents.txt", 'r', encoding="utf-8")
        # Читаємо весь файл і розбиваємо його на список рядків
        lines = fileRead.read().splitlines()
        fileRead.close()
        
        i = 0                   # Поточний індекс у списку рядків
        countAbonent = 1        # Порядковий номер абонента для виводу
        countLines = len(lines) # Загальна кількість рядків у файлі
        
        # Цикл проходить по списку з кроком 5 (оскільки на кожного абонента 5 рядків)
        while i < countLines:
            print(f"-----------{countAbonent}----------")
            # Виводимо ПІБ (рядки i, i+1, i+2)
            print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
            # Виводимо телефон (рядок i+3)
            print(lines[i+3])
            # Виводимо адресу (рядок i+4)
            print(lines[i+4])
            
            i = i + 5 
            countAbonent = countAbonent + 1
    except FileNotFoundError:
        print("Файл не знайдено!")

# Основна частина програми
action = -1
while action != 0:
    print("0.Вихід")
    print("1.Додати клієнта")
    print("2.Показати усіх клієнтів")
    print("3.Очистити список клієнтів")
    print("4.Пошук по номером")
    print("5.Пошук по прізвищу, імені, побатькові")
    print("6.Пошук по адресі")
    print("->_", end="")
    
    # Перевірка на коректність введення пункту меню (тільки цифри)
    try:
        action = int(input())
    except ValueError:
        print("Введіть число!")
        continue

    # Обробка обраної дії
    match action:
        case 1:
            writeFileAbonent()
            print("--Додали нового абонента---")

        case 2:
            print("--Показуємо усіх абонентів--")
            readFileAbonents()

        case 3:
            clearFileAbonents()
            print("--Очищаємо список абонентів--")

        case 4:
            search = input("Введіть номер телефону: ")
            try:
                fileRead = open("abonents.txt", 'r', encoding="utf-8")
                lines = fileRead.read().splitlines()
                fileRead.close()
                
                i = 0
                found = False
                # Шукаємо збіг у кожному 4-му рядку абонента (індекс i+3)
                while i < len(lines):
                    if lines[i+3] == search:
                        print("----Знайдено абонента----")
                        print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
                        print(lines[i+3])
                        print(lines[i+4])
                        found = True
                        break # Зупиняємо пошук, якщо знайшли
                    i += 5
                if not found:
                    print("Номер не знайдено")
            except FileNotFoundError:
                print("База даних порожня")

        case 5:
            search = input("Введіть ПІБ або частину: ").lower()
            try:
                fileRead = open("abonents.txt", 'r', encoding="utf-8")
                lines = fileRead.read().splitlines()
                fileRead.close()
                
                i = 0
                found = False
                while i < len(lines):
                    # Склеюємо Прізвище, Ім'я та Побатькові в один рядок для пошуку
                    full_name = f"{lines[i]} {lines[i+1]} {lines[i+2]}".lower()
                    # Перевіряємо, чи міститься пошуковий запит у повному імені
                    if search in full_name:
                        print("----Знайдено----")
                        print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
                        print(lines[i+3])
                        print(lines[i+4])
                        found = True
                    i += 5
                if not found:
                    print("Не знайдено")
            except FileNotFoundError:
                print("База даних порожня")

        case 6:
            search = input("Введіть адресу або частину: ").lower()
            try:
                fileRead = open("abonents.txt", 'r', encoding="utf-8")
                lines = fileRead.read().splitlines()
                fileRead.close()
                
                i = 0
                found = False
                while i < len(lines):
                    # Перевіряємо збіг у 5-му рядку абонента (індекс i+4)
                    if search in lines[i+4].lower():
                        print("----Знайдено----")
                        print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
                        print(lines[i+3])
                        print(lines[i+4])
                        found = True
                    i += 5
                if not found:
                    print("Не знайдено")
            except FileNotFoundError:
                print("База даних порожня")