class Computer:
    def init(self, comp_id, hourle_rate):
        self._id = comp_id
        self._hourly_rate = hourle_rate # цена/ч
        self._id = False # True-занят, False-свободен
        self._current_client = None
        self._hours = 0

    @property
    def id(self):
        return self.__id
    @property
    def hourly_rate(self):
        return self.__hourly_rate
    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if new_rate >=50 and new_rate <=1000:
            self.__hourly_rate = new_rate
            return self.__hourly_rate
        
    def start_session(self, client, hours):
        if self._is_buys:
            print(f"Комп {self.id} занят")
            return False
        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_buys = True #комп занят
            self._current_client = client
            self._hours = hours
            print(f"{client.name} начал сессию")
            return True
        else:
            print(f"Не хватает денег {client}")

    def end_session(self): #Завершает сессию, считает оплату
        self._is_buys = False
        income = self.__hourly_rate * self._hours
        client_name=self._current_client.name
        print(f"Сессия завершена {client_name}")
        self._current_client = None
        self._hours = 0
        return income
    
    def info(self):
        status = 'Занят' if self._is_buys else 'Свободен'
        print(f"Комп {self.id}:{status}")

class Client:
    def init(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def add_balance(self, amount): #поплнеине счёта.
        if amount >0 and amount<=10000:
            self._balance += amount
            print(f"Баланс поплнен на {amount}сом, теперь у вас {self.balance}")
        else:
            print("Введите коррекное значение на поплнение")
            return False
        
    def pay(self, amount): #уменьшает баланс, если хватает денег.
        pass

    def info(self):
        print(f"Имя: {self.name} на карте: {self.balance} сом")

# 3. Club
# Атрибуты: name, computers — список объектов Computer
# _income — защищённый атрибут, выручка клуба.
# Методы:
# add_computer(computer)
# find_free_computer()
# serve_client(client, hours) — находит свободный комп, запускает сессию.
# end_all_sessions() — завершает все активные сессии и увеличивает доход клуба.
# show_status() — показывает состояние всех компьютеров и доход.


class Club:
    def __init__(self, name):
        self.name = name
        self.computers = []
        self._income = 0
    
    def add_computer(self, computer):
        self.computers.append(computer)
        print(f"Компьютер {computer.id} добавлен в клуб")
    
    def find_free_computer(self):
        for comp in self.computers:
            if not comp._is_buys:
                return comp
        return None
    
    def serve_client(self, client, hours):
        comp = self.find_free_computer()
        if comp:
            if comp.start_session(client, hours):
                print(f"Клиент {client.name} сел за компьютер {comp.id}")
                return True
        else:
            print("Свободных компьютеров нет")
            return False
    
    def end_all_sessions(self):
        total = 0
        for comp in self.computers:
            if comp._is_buys:
                income = comp.end_session()
                total += income
        self._income += total
        print(f"всу сессии завершены. Доход: {total} сом")
    
    def show_status(self):
        print(f"\n статус клуба '{self.name}':")
        print(f"Общий доход: {self._income} сом")
        print("Компьютеры:")
        for comp in self.computers:
            comp.info()
