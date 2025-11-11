
    usl = """
    1. Показать список фильмов (с ценами и возрастными ограничениям).
    2. Купить билет на фильм (пользователь вводит имя и возраст).
    Если возраст меньше минимального - билета не продаётся.
    У одного зрителя может быть только один билет.
    3. Отменить билет по имени зрителя.
    4. Показать все купленные билеты (имя, возраст зрителя, фильм, цена).
    5. Посчитать общую выручку кинотеатра.
    6. Выйти из программы.
    """

    movies = {
        "Интерстлеер": (400, 13),
        "Начало": (250, 16),
        "Матрица": (200, 16),
        "Аватар": (350, 12),
    }

    purchases = {}  

    def show_movies():
        print("\nСписок фильмов:")
        for name, (price, age_min) in movies.items():
            print(f"{name}: цена {price} сом, мин. возраст {age_min}")

    def buy_ticket():
        name = input("Введите имя зрителя: ").strip().title()
        if not name:
            print("Имя не может быть пустым.")
            return
        if name in purchases:
            print("У этого зрителя уже есть билет.")
            return

        age_str = input("Введите возраст зрителя: ").strip()
        if not age_str.isdigit():
            print("Возраст должен быть целым числом.")
            return
        age = int(age_str)

        print("Выберите фильм:")
        for m in movies:
            print("-", m)
        movie_input = input("Название фильма: ").strip()
        key_map = {k.casefold(): k for k in movies}
        movie_key = key_map.get(movie_input.casefold())
        if not movie_key:
            print("Такого фильма нет.")
            return

        price, min_age = movies[movie_key]
        if age < min_age:
            print("Возраст меньше допустимого — билет не продаётся.")
            return

        purchases[name] = (age, movie_key, price)
        print(f"Билет оформлен: {name}, фильм '{movie_key}', цена {price} сом.")

    def cancel_ticket():
        name = input("Введите имя зрителя для отмены билета: ").strip().title()
        if name in purchases:
            del purchases[name]
            print(f"Билет у {name} отменён.")
        else:
            print("Билет для этого имени не найден.")

    def show_purchases():
        if not purchases:
            print("Покупок нет.")
            return
        print("\nКупленные билеты:")
        for name, (age, movie, price) in purchases.items():
            print(f"Имя: {name}, Возраст: {age}, Фильм: {movie}, Цена: {price} сом")

    def total_revenue():
        total = sum(price for (_, _, price) in purchases.values())
        print(f"Общая выручка: {total} сом")

    if __name__ == "kino"   
        while True:
            print(usl)
            choice = input("Выберите действие (1-6): ").strip()
            if choice == "1":
                show_movies()
            elif choice == "2":
                buy_ticket()
            elif choice == "3":
                cancel_ticket()
            elif choice == "4":
                show_purchases()
            elif choice == "5":
                total_revenue()
            elif choice == "6":
                print("Выход.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")