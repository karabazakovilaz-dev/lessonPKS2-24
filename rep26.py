while True:
    print("""
    1. Добавляет заказ (блюдо, количество, цена)
    2. Показывает все заказы
    3. Ищет заказы по названию блюда
    4.Подсчиывает общую выручку
    5. Завершает работу по выбору пользователя""")
    choice = input("Выберите действие: ")
    if choice == '1':
        textUser = input("Что хотите добавить? ")
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        break
    else:
        print("Выбирайте от 1го до 4х")
        continue
    with open('notebook.txt', 'a', encoding='utf-8') as file:
        file.write(textUser + '\n')
    print("Заметка добавлена!")
    with open('notebook.txt', 'r', encoding='utf-8') as file:
        print(file.read())
    findWord = input("Какое блюдо ищем? ")
    with open('notebook.txt', 'r', encoding='utf-8') as file:
        notes = file.readlines()
        for note in notes:
            if findWord in note:
                print(note)
total_revenue = 0
for item in products:
    total_revenue += item["price"] * item["quantity"]

print("Общая выручка:", total_revenue, "сомов")

    menu_food = {
"плов": 250,
"манты": 300,
"Лагман": 280,
    "Шашлык": 250,
    "Бешбармак": 500,
}