tarif = {
    '3 часа': 150,
    '5 часа': 220,
    '7 часа': 330,
}

clients = {
    "Agent007": {'password': 'qwerty', 'balance': 300},
}

def register():
    name = input("Придумайте логин: ")
    password = input("Придумайте пароль: ")
    clients[name] = {'password': password, 'balance': 0}
    print(f"Поздравляю {name}! Регистрация прошла успешно!")

def login():
    print("Добро пожаловать")
    name = input("Введите логин: ")
    if name in clients:
        password = input("Введите пароль: ")
        if password == clients[name]['password']:
            print("Снова Добро пожаловать,", name)
            return name
        else:
            print("Пароль не совпадает")
            return None
    else:
        print("Такого пользователя нет")
        return None
def deposit(user): 
    balance = int(input("Введите сумму для пополнения: "))
    clients[user]['balance'] += balance


def money(login):
    print("Ваш счёт:", clients[login]['balance'], "сом")


def buy_tarif(login):
    print("Доступные тарифы:")
    for t, price in tarif.items():
        print(f"{t} — {price} сом")

    choice = input("Выберите тариф (например: 3 часа): ")
    if choice in tarif:
        price = tarif[choice]
        if clients[login]['balance'] >= price:
            clients[login]['balance'] -= price
            print(f"Вы купили тариф '{choice}' за {price} сом!")
            print("Остаток на счёте:", clients[login]['balance'], "сом")
        else:
            print("Недостаточно средств!")
    else:
        print("Такого тарифа нет.")

while True:
    print("Были ли вы у нас?")
    nurislam = input("Да или Нет: ").title()
    if nurislam == 'Да':
        user = login()
        if user:
         while True:
                print("1. Посмотреть баланс")
                print("2. Пополнить баланс")
                print("3. Купить тариф")
                print("4. Выйти")
                choice = input("Выберите действие: ")

                if choice == '1':
                    money(user)
                elif choice == '2':
                    deposit(user)
                elif choice == '3':
                    buy_tarif(user)
                elif choice == '4':
                    print("Выход в главное меню...\n")
                    break
                else:
                    print("Неверный выбор!")
              
               


        

                


