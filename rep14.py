# Написать функцию airline_booking(flights), которая:
#  1. Позволяет пользователю покупать билеты (ввод города).
#  2. Если города нет → «Такого направления нет».
#  3. Если мест нет → «Билеты закончились».
#  4. Если есть → спросить количество билетов.
#  • Если мест меньше → вывести «Недостаточно мест».
#  • Иначе оформить покупку (уменьшить количество мест, добавить в корзину, увеличить сумму).
#  5. Если сумма покупки превысила 20000 сом, дать скидку 20%.
#  6. В конце вывести:
#  • список купленных билетов (город + количество),
#  • общую стоимость (с учётом скидки),
#  • остаток мест по каждому направлению

def airline_booking(flights):
    basket = {} 
    total_sum = 0

    while True:
        city = input("Введите город назначения (или 'стоп' для завершения): ")
        if city.lower() == 'стоп':
            break

        if city not in flights:
            print("Такого направления нет")
            continue

        if flights[city]["места"] == 0:
            print("Билеты закончились")
            continue

        try:
            qty = int(input("Введите количество билетов: "))
            if qty <= 0:
                print("Введите положительное количество билетов")
                continue
        except ValueError:
            print("Введите корректное число")
            continue

        if qty > flights[city]["места"]:
            print("Недостаточно мест")
            continue


        flights[city]["места"] -= qty
        basket[city] = basket.get(city, 0) + qty
        total_sum += flights[city]["цена"] * qty
        print(f"Добавлено {qty} билетов в город '{city}'")


    if total_sum > 20000:
        discount = total_sum * 0.20
        total_sum -= discount
        print(f"Вам предоставлена скидка 20%: -{discount} сом")


    if basket:
        print("\nВы купили билеты:")
        for city, qty in basket.items():
            print(f"{city}: {qty} шт.")
        print(f"Общая стоимость: {total_sum} сом")
    else:
        print("Вы не купили билетов")

    print("\nОстаток мест по направлениям:")
    for city, data in flights.items():
        print(f"{city}: {data['места']} мест")

flights = {
    "Москва": {"цена": 8000, "места": 5},
    "Стамбул": {"цена": 12000, "места": 3},
    "Париж": {"цена": 15000, "места": 2},
    "Бишкек": {"цена": 5000, "места": 6}
}

airline_booking(flights)


