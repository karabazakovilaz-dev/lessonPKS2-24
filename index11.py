class Product:
    def __init__(self, name, price, quantity):  
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def buy(self, amount):
        if amount > self.quantity:
            print(f"Недостаточно товаров в складе {self.name}") 
            return
        self.quantity -= amount
        print(f"Покупка {amount} шт. {self.name} Успешно")

    def show_info(self):
        print(f"Название: {self.name}, Цена: {self.price}, Кол-во: {self.quantity}")

class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date):  
        super().__init__(name, price, quantity)  

    def show_expiration(self):
        print(f"Товар: {self.name}, срок годности до: {self.expiration_date}")

class ElectronicsProduct(Product):  
    def __init__(self, name, price, quantity, warranty_years):  
        super().__init__(name, price, quantity)  
        self.warranty_years = warranty_years

    def show_warranty(self):
        print(f"Товар: {self.name}, срок гарантии: {self.warranty_years} лет")


bread = FoodProduct('Хлеб', 25, 10, "25.11.2025")
laptop = ElectronicsProduct('Ноутбук Acer', 55000, 3, 1)
bread.show_info()
laptop.show_info()
bread.show_expiration()
laptop.show_warranty()
bread.buy(3)
bread.buy(1)