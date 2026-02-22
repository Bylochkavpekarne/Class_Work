def writeFileAbonent():
    lastName = input("Вкажіть прізвище: ")
    firstName = input("Вкажіть ім'я: ")
    soName = input("Вкажіть побатькові: ")
    phone = input("Вкажіть телефон: ") 
    address = input("Вкажіть адресу: ")
    fileWriter = open("abonents.txt", 'a', encoding="utf-8")
    fileWriter.write(f"{lastName}\n")
    fileWriter.write(f"{firstName}\n")
    fileWriter.write(f"{soName}\n")
    fileWriter.write(f"{phone}\n")
    fileWriter.write(f"{address}\n")
    fileWriter.close()

def clearFileAbonents():
    fileWriter = open("abonents.txt", 'w', encoding="utf-8")
    fileWriter.close()

def readFileAbonents():
    try:
        fileRead = open("abonents.txt", 'r', encoding="utf-8")
        lines = fileRead.read().splitlines()
        fileRead.close()
        i = 0 
        countAbonent = 1 
        countLines = len(lines) 
        while i < countLines:
            print(f"-----------{countAbonent}----------")
            print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
            print(lines[i+3])
            print(lines[i+4])
            i = i + 5 
            countAbonent = countAbonent + 1
    except FileNotFoundError:
        print("Файл не знайдено!")

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
    
    try:
        action = int(input())
    except ValueError:
        print("Введіть число!")
        continue

    # Всі case повинні бути всередині match, а match — всередині while
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
                while i < len(lines):
                    if lines[i+3] == search:
                        print("----Знайдено абонента----")
                        print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
                        print(lines[i+3])
                        print(lines[i+4])
                        found = True
                        break
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
                    full_name = f"{lines[i]} {lines[i+1]} {lines[i+2]}".lower()
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