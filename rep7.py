students = {
    "Нурисалм":{
        "Математика": [5, 4],
        "История": [3, 4]
    },
    "Арген": {
        "Физика": [4, 5],
        "Литература": [5]
}
}
# print(usl)
while True:
    req = input("Введите действие: ")
    if req == '1':
        for name, prerdmets in students.items():
            print(name)
            for pred, bal in prerdmets.items():
                print(f"   {pred}: {bal}")
    elif req == '2':
        name = input("Добавить ученика: ")
        students[name] = {}
        print("Добавлен в наш список")
    elif req == '3':
        name = input("К какому ученику добавить предмет: ")
        prerdmet = input("Добавить предмет ученику: ")
        students[name] [prerdmet] = []
        print("Успех")
    elif req == '4':
        name = input("К какому ученику добавить оценку: ")
        if name in students:
           prerdmet = input("Выбрать какому предмету: ")
           if prerdmet in students[name]: 
            ball = int(input("Добавить оценку предмету: "))
            students[name][prerdmet].append(ball)
            print("Успех")
        else:  
            print("нет такого предмета. Выберите 3 и добавьте предмет")
    else:
        print("Нет такого ученика") 