def cinema_booking(cinema):
    basket = {} 
    total_sum = 0

    while True:
        film = input("Введите название фильма (или 'стоп' для завершения): ")
        if film.lower() == 'стоп':
            break

        if film not in cinema:
            print("Такого фильма нет в кинотеатре")
            continue

        if cinema[film]["места"] == 0:
            print("Билеты на этот фильм закончились")
            continue

        try:
            qty = int(input("Введите количество билетов: "))
            if qty <= 0:
                print("Введите положительное количество билетов")
                continue
        except ValueError:
            print("Введите корректное число")
            continue

        if qty > cinema[film]["места"]:
            print("Недостаточно билетов")
            continue


        cinema[film]["места"] -= qty


        if film in basket:
            basket[film] += qty
        else:
            basket[film] = qty


        total_sum += cinema[film]["цена"] * qty
        print(f"Добавлено {qty} билетов на фильм '{film}'")


    if total_sum > 1000:
        discount = total_sum * 0.10
        total_sum -= discount
        print(f"Вам предоставлена скидка 10%: -{discount} сом")


    if basket:
        print("\nВы купили билеты:")
        for film, qty in basket.items():
            print(f"{film}: {qty} шт.")
        print(f"Итоговая сумма: {total_sum} сом")
    else:
        print("Вы не купили билетов")


cinema = {
    "Аватар": {"цена": 400, "места": 5},
    "Дюна": {"цена": 350, "места": 3},
    "Шрек": {"цена": 200, "места": 10},
    "Чебурашка": {"цена": 250, "места": 4}
}
cinema_booking(cinema)