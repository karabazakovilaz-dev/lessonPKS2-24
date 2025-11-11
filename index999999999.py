class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"
if __name__ == "__main__":
    person = Person(" Нурислам", 16)
    print(person.info())  




    