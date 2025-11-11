class Airlane:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.flights = []

    def add_flight(self, flight_name, quantity):
        new_flight = {"name": flight_name, "quantity": quantity}  
        self.flights.append(new_flight)  
        print(f"Рейс {flight_name} добавлен с количеством билетов {quantity}")

def delete_flight(self, flight_name):
    
    if any(flight["name"] == flight_name for flight in self.flights):
        self.flights = [flight for flight in self.flights if flight["name"] != flight_name]
        print(f"Рейс {flight_name} успешно удален")
    else:
        print(f"Рейс {flight_name} не найден")

    def      show_flights(self):
         for flight in self.flights:
            print(f"Рейс: {flight['name']}, Количество билетов: {flight['quantity']}")  

    def deposit(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Поздравляю, покупка {amount} билетов совершена на имя {self.name}")
    

airlane = Airlane("airBilal", 100)  
airlane.add_flight("Бишкек-Ташкант", 23)
airlane.add_flight("Бишкек-Жалал Абад", 23)
airlane.add_flight("Бишкек-ОШ", 23)
airlane.show_flights() 
airlane.deposit(20)
