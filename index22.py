# 1.класс Person
# Атрибуты: name, age, balance
# Методы: deposit(amount) — пополнение счёта.
# withdraw(amount) — снятие со счёта.
# info() — возвращает краткую информацию о клиенте.

class Person:
    def init(self, name, age, balance=0):
        self.name = name      
        self.age = age        
        self.balance = balance  


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} пополнил счет на {amount} руб.")
        else:
            print("Сумма пополнения должна быть положительной!")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} снял со счета {amount} руб.")
        elif amount > self.balance:
            print("Недостаточно средств на счету!")
        else:
            print("Сумма снятия должна быть положительной!")


    def info(self):
        return f"Клиент: {self.name}, Возраст: {self.age}, Баланс: {self.balance} руб."

# 2.класс Bank
# Атрибуты: name, clients — список объектов Person
# products — список активных продуктов (депозиты, кредиты, рассрочки), income — доход банка
# Методы: add_client(client), add_product(product)
# calculate_total_profit() — суммирует доходы по всем продуктам.

class Bank:
    def init(self, name):
        self.name = name
        self.clients = []
        self.product = []
        self.income = 0

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен")

    def add_product(self, product):
        self.clients.append(product)
        print(f"Продукт добавлен")

    def add_income(self, amount):
        self.income += amount

    def calculate_total_profit(self, client):
        return self.income

    def add_clients(self):
        print("Наши Клиенты: ")
        for i in self.clients:
            print(f". {i.info()}")
        
    def add_product(self):
        print("Наши Продукты: ")
        for i in self.products:
            print(f". {i.info()}")

# 3. класс BankProduct (базовый класс)
# Атрибуты: client, amount, interest_rate, term_months
# Методы: calculate_interest() — рассчитывает сумму процентов.
# info() — краткая информация о продукте.
class BankProduct:
    def init(self, client, amount, interest_rate, term_months):
        self.client = client
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_months = term_months

    def calculate_interest(self):
        return self.amount * (self.interest_rate / 100) * (self.term_months / 12)

    def info(self):
        return f"Продукт для клиента: {self.client.name}, Сумма: {self.amount} руб., Процентная ставка: {self.interest_rate}%, Срок: {self.term_months} месяцев"

# 4.класс Deposit (наследник BankProduct)
# Деньги клиента передаются банку, и по окончании срока клиент получает сумму + проценты.
# Метод close_deposit() возвращает клиенту деньги и начисленные проценты.
class Deposit(BankProduct):
    def close_deposit(self):
        total_amount = self.amount + self.calculate_interest()
        self.client.deposit(total_amount)
        print(f"Депозит закрыт. Клиент {self.client.name} получил {total_amount} руб. (включая проценты).")
        return total_amount
    # 5.класс Credit (наследник BankProduct)
# Банк выдаёт клиенту деньги, которые тот должен вернуть с процентами.
# Метод monthly_payment() рассчитывает ежемесячный платёж по кредиту.
# Метод close_credit() возвращает банку тело кредита и проценты (уменьшает баланс клиента).

class Credit(BankProduct):
    def monthly_payment(self):
        total_amount = self.amount + self.calculate_interest()
        monthly_payment = total_amount / self.term_months
        return monthly_payment

    def close_credit(self):
        total_amount = self.amount + self.calculate_interest()
        if self.client.balance >= total_amount:
            self.client.withdraw(total_amount)
            print(f"Кредит закрыт. Клиент {self.client.name} выплатил {total_amount} руб. (включая проценты).")
            return total_amount
        else:
            print("Недостаточно средств для закрытия кредита!")
            return 0

# 6. класс Installment (Рассрочка)
# Клиент покупает товар в рассрочку (без процентов, но с комиссией).
# Атрибуты: product_name, commission_rate
# Методы: monthly_payment(), close_installment()

class Installment:
    def init(self, client, product_name, product_price, months, commission_rate):
        self.client = client                 
        self.product_name = product_name    
        self.product_price = product_price    
        self.months = months                 
        self.commission_rate = commission_rate  
        self.paid_months = 0                  
        self.closed = False                  


    def monthly_payment(self):
        commission_total = self.product_price * self.commission_rate
        total_to_pay = self.product_price + commission_total
        monthly = total_to_pay / self.months
        return monthly


    def close_installment(self):
        if not self.closed:
            commission_total = self.product_price * self.commission_rate
            total_to_pay = self.product_price + commission_total
            already_paid = self.paid_months * self.monthly_payment()
            remaining = total_to_pay - already_paid

            if self.client.balance >= remaining:
                self.client.balance -= remaining
                self.closed = True
                print(f"{self.product_name} рассрочка у {self.client.name} закрыта.")
            else:
                print("Недостаточно средств для закрытия рассрочки.")
        else:
            print("Рассрочка уже закрыта.")