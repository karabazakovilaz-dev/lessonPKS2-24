# Написать функцию raz_park(park), которая:
# 1. Спрашивает у пользователя его возраст.
# 2. Позволяет покупать билеты на аттракционы (пока не введёт стоп).
# 3. Если аттракциона нет → «Такого аттракциона нет».
# 4. Если мест нет → «Мест больше нет».
# 5. Если возраст меньше, чем ограничение → «Вам пока нельзя на этот аттракцион».
# 6. Если всё в порядке → спросить количество билетов.
# * Если билетов меньше, чем просит пользователь → «Недостаточно мест».
# * Иначе оформить покупку.
# 7. Если итоговая сумма превышает 1500 сом, дать скидку 10%.
# 8. В конце вывести:
# * список купленных аттракционов,
# * общую сумму (со скидкой и без),
# * остаток мест по каждому аттракциону.
def raz_park(park):
    purchases = []
    total_price = 0

    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if age < 0:
                print("Возраст не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Введите корректный возраст (число).")

    while True:
        attraction = input("Введите название аттракциона для покупки билетов (или 'стоп' для выхода): ")
        if attraction.lower() == "стоп":
            break

        if attraction not in park:
            print("Такого аттракциона нет.")
            continue

        attr_info = park[attraction]

        if attr_info["места"] <= 0:
            print("Мест больше нет.")
            continue

        if age < attr_info["возраст"]:
            print("Вам пока нельзя на этот аттракцион.")
            continue

        while True:
            try:
                tickets = int(input("Введите количество билетов: "))
                if tickets <= 0:
                    print("Количество билетов должно быть положительным числом.")
                    continue
                break
            except ValueError:
                print("Введите корректное число билетов.")

        if tickets > attr_info["места"]:
            print("Недостаточно мест.")
            continue

        price = attr_info["цена"] * tickets
        purchases.append({"аттракцион": attraction, "билеты": tickets, "цена": price})
        total_price += price
        attr_info["места"] -= tickets
        print(f"Покупка оформлена: {attraction}, билетов: {tickets}, цена: {price} сом.")

    total_price_without_discount = total_price
    if total_price > 1500:
        discount = total_price * 0.10
        total_price -= discount
        print(f"\nВаша скидка 10%: -{discount:.2f} сом.")

    print("\nСписок купленных аттракционов:")
    for p in purchases:
        print(f"{p['аттракцион']}: билетов {p['билеты']}, цена {p['цена']} сом")

    print(f"\nОбщая сумма без скидки: {total_price_without_discount:.2f} сом")
    print(f"Общая сумма со скидкой: {total_price:.2f} сом")

    print("\nОстаток мест по аттракционам:")
    for k, v in park.items():
        print(f"{k}: {v['места']}")

parkList = {
    "Американские горки": {"цена": 500, "места": 5, "возраст": 12},
    "Колесо обозрения": {"цена": 300, "места": 8, "возраст": 0},
    "Комната страха": {"цена": 400, "места": 4, "возраст": 14},
    "Карусель": {"цена": 200, "места": 6, "возраст": 0}
}

raz_park(parkList)