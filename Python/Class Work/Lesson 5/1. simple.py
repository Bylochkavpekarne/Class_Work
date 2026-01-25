print("-----Робота із списками в Python-----")

myList = [12, 18, 33, 22]

print("Початковий список:", myList)


mixedList = [12, "Hello", 45.6, True]
print("Спис")



print("Перший елемент списку", myList[0])
myList[0] = "Сало"

print("Змінений список myList", myList)

myList.append(29);
print("Список myLisat пысля додавання нового елмента 29: ", myList)

cats = ["Мурка", "Барсик", "Васька"]
print("Список котиків: ", cats)

myList.extend(cats)
print("myList після додавання списку котів: ", myList)
