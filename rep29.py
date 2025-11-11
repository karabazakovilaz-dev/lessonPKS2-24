# Задача "Банковский счет"
# Функционал:
# 1. Проверить баланс
# 2. Пополнить
# 3. Снять
# 4. Показать итог
balance = 0

def get_balance():
    return balance

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Пополненение на {amount} сом. Новый баланс: {balance}")
    else:
        print("Ошибка. Должно быть выше нуля")
def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Снятие на {amount} сом. Новый баланс: {balance}")
    else:
        print("Ошибка. Недостаточно средств или неверная сумма")
def show_summary():
    print(f"Итоговый баланс: {balance} сом")
while True:
    print("\nВыберите действие:")
    print("1. Проверить баланс")
    print("2. Пополнить счет")
    print("3. Снять со счета")
    print("4. Показать итоговый баланс")
    print("5. Выйти")
    choice = input("Введите номер действия (1-5): ")
    if choice == '1':
        print(f"Текущий баланс: {get_balance()} сом")
    elif choice == '2':
        amount = float(input("Введите сумму для пополнения: "))
        deposit(amount)
    elif choice == '3':
        amount = float(input("Введите сумму для снятия: "))
        withdraw(amount)
    elif choice == '4':
        show_summary()
    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")