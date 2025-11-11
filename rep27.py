# 1)Вам нужно проверить начало конец строки на присутсвие неких текстовых шаблонов, таких как   расрширения 
# файлов, схемы URL и.т.д
filename = 'spam.txt'
url = 'https://www.python.org'
# # 2) Нпсиать функцию "угадай число", используя import random,
# пользователь должени отгодать число что задает копьютер,
# компьютер задает число от 1 до 100. Например компьютер загадал
# число 10  человек ввел число 50 то мы должны писатт ему 
# "число должно быть ниже" и наоборот а если он угадал то выводим "молодец ты угадал"
# и показать сколько попытак он сделал
def guess_number():
    import random
    num = random.randint(100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            number = int(input("Введите число: "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue

        attempts += 1

        if number > num:
            print("Число должно быть ниже!")
        elif number < num:
            print("Число должно быть выше!")
        else:
            print(f"Молодец! Ты угадал число {num} за {attempts} попыток!")
# # 3) Генератор пароля
# # Создайте функцию которая генерирует случайный  пароль длиной
# N символов. Используйте модуль random и буквы/цифры/спецсимволы
# 4) Проверка палиндрома. Напишите функцию которая проверяет
# является ли строка палиндромом. (Читается одинаково с начала и с конца)
# 1)Вам нужно проверить начало конец строки на присутсвие неких текстовых шаблонов, таких как   расрширения 
# файлов, схемы URL и.т.д
filename = 'spam.txt'
url = 'https://www.python.org'

def check_patterns(s):
    
    if s.endswith('.txt'):
        print(f"{s} заканчивается на .txt")
    
    if s.startswith('http://') or s.startswith('https://'):
        print(f"{s} начинается с схемы URL")

check_patterns(filename)
check_patterns(url)

import random 
num = random.randit(1,100)

import random

num = random.randint(1, 100)  

while True:
    number = int(input("Введите число: "))  

    if number > num:
        print("Берите ниже!")
    elif number < num:
        print("Берите выше!")
    else:
        print("Молодец! Ты угадал!")
        break  
import random

num = random.randint(1, 100)  # Компьютер загадывает число
attempts = 0  #

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    number = int(input("Введите число: "))  
    attempts += 1 

    if number > num:
        print("Берите ниже!")
    elif number < num:
        print("Берите выше!")
    else:
        print(f"Молодец! Ты угадал число {num} за {attempts} попыток!")
        break 

    
