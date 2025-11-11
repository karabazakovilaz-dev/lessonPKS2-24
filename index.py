# import sys

# listPass = {'Gena': 'qwerty'}

# login = input("Введите логин: ")
# if login not in listPass:
#     print("Неверный логин.")
#     sys.exit()

# max_attempts = 3
# for attempt in range(1, max_attempts + 1):
#     password = input("Введите пароль: ")
#     if password == listPass[login]:
#         print("Добро пожаловать!")
#         break
#     else:
#         remaining = max_attempts - attempt
#         if remaining > 0:
#             print(f"Неверный пароль. Осталось попыток: {remaining}")
#         else:
#             print("Превышено количество попыток. Повторите вход через 5 минут.")
#             sys.exit()



class Trasport:
    def init(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    def start(self):
        print("Транспорт начал движение")
    def stop(self):
        print("Транспорт остановил движение")
    def info(self):
        print(f"Скорость: {self._speed} км/ч, Вместимость: {self._capacity} чел")

class Car(Trasport):
    def __init__(self, speed, capacity, brand):
        super().init(speed, capacity)
        self.brand = brand

    def info(self):
        base_info = super().info()
        print(f"Автомобиль: {self.brand}: {base_info}")
    

class Bus(Trasport):
    def init(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number

    def info(self):
        base_info = super().info()
        print(f"Автобус: {self.route_number}, {base_info}")
####################################
                            