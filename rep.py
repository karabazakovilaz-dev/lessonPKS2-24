menu_food = {
    "плов": 250,
    "манты": 300,
    "Лагман": 280,
    "Шашлык": 250,
    "Бешбармак": 500,
}
Menu_drinks = {
   "Чай": 50,
   "Кофе": 120,
   "Кумыс": 150,
   "Айран": 80,
   "Сок": 100,
}

cart = [] # Ваша корзина куда кладется стоимость заказов
while True:
    req = int(input('1. Показать меню блюд\n2. Показать меню напитков\n3. Заказать блюдо\n4.Заказать напиток\n5. Показать корзину и готовую сумму\n6. Выйти\n6. Выйти\nВыберите действие:'))
    if req == 1:
        for k,v in menu_food.items():
            print(f"{k}; {v}сом")
    elif req == 2:
        for k,v in Menu_drinks.items():
            print(f"{k}:{v}сом")
    elif req == 3:
        print(menu_food)
        name_food = input("Какое блюдо хототе?").title()
        if name_food in menu_food:
            cart.append(menu_food[name_food])
            print(cart)
    elif req == 4:
        print(Menu_drinks)
        name_drink = input("Какой напиток хотите?").title()
        if name_drink in Menu_drinks:
            cart.append(Menu_drinks[name_drink])
            print(cart)
    elif req == 5:
        if not cart:
            print("В корзине", len(cart))
            total = sum(cart)
            print("Общая сумма:", total)
        else:
            print("Вы ничего не заказывали")
    elif req==6:
        print("Спасибо что посетили")
        break
