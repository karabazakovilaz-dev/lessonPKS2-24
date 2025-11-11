from rep98 import Airlane

def add_flight_cli(airline):
    name = input("Название рейса: ").strip()
    if not name:
        print("Отмена.")
        return
  
    qty = int(input("Количество билетов: "))
    print("Введите целое число для количества билетов.")
    airline.add_flight(name, qty)

def delete_flight_cli(airline):
    name = input("Название рейса для удаления: ").strip()
    if not name:
        print("Отмена.")
        return
    airline.delete_flight(name)

def buy_tickets_cli(airline):
    try:
        amount = int(input("Сколько билетов купить: ").strip())
    except ValueError:
        print("Введите целое число.")
        return
    airline.deposit(amount)

def main():
    # Использует ваш класс Airlane из rep98.py
    airline = Airlane("airBilal", 100)

    while True:
        print("\nМеню:\n1 - Добавить рейс\n2 - Удалить рейс\n3 - Показать рейсы\n4 - Купить билеты\n0 - Выход")
        cmd = input("Выберите действие: ").strip()
        if cmd == "1":
            add_flight_cli(airline)
        elif cmd == "2":
            delete_flight_cli(airline)
        elif cmd == "3":
            airline.show_flights()
        elif cmd == "4":
            buy_tickets_cli(airline)
        elif cmd == "0":
            break
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()