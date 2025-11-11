def order(menu):
    total = 0 
    ordered = []
    while True:
        item = input("Что закажите")
        if item == 'стоп':
            break
        if item in menu:
            total+= menu[item]
            ordered.append(item)
            print(ordered)
        else:
         print('Такого блюда нет')
    print(f"Ваш заказ: {ordered}")
    print(f"Сумма: {total}")                       
menuList = {
    "Бургер":150,
    "Пицца": 500,
    "Салат": 200,
    "Суп": 120.
}
# oкder(menuList)
# Напишите программу с функцией library_system(library), которая:
# 1. Позволяет пользователя взять книгу (ввод названия)
# Если книги нет выести сообщения такой книги нет
# Если есть, но экземпляров больше нет это кнга закончилась
# Если книга доступна уменьшить количество на 1 и добавить в список читателя
# 2. пользователь может брать нексолько книг пока не ведёт стоп
# 3. В конце вывести список взятых книг


def order(library):
    total = 0
    ordered = []
    while True:
        item = input("Какую книгу возмьете: ")
        if item.lower() == 'стоп': 
            break
        if item in library:
            total += library[item]
            ordered.append(item)
            print("Заказано:", ordered)
        else:
            print('Такой книги нет')
    print(f"Ваша книга(и): {ordered}")
    print(f"Сумма: {total}")

library = {
    "Гарри поттер": 3,
    "Властелин колец": 2,
    "Три мушкетёра": 2
}

order(library)


  

















