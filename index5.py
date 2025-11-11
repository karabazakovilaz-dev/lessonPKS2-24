# Функции - это кусочек кода который мы можем написать один раз и использовать множество раз 
#  она помогает:
#  1) не повтарять один и тот же кол
#  2) делает программу аккуратнее и понятнее
#  3) удобно передавать данныу внутрь и получать результат

# Функция бывают двух видов:
#   1) встроенные функции print(), input(), type(), len(), list(), dict(), и т.п
#   2 ) пользоватиские функции, те функции что мы пишем сами через 
#    def - исп только тогда когда мы создаем функции      

# Функция без оргумента
def HelloPrint():
    return 'Hello world'

print(HelloPrint())

# Функция с оргументами
def HelloPrint(name):
    return f'Hello world {name}'

print(HelloPrint("Albert"))

# Создайте калькулятор используя функцию, цикл, условие и ввод и вывод данных
def calc(num1, simbol, num2):
    while True:
        if simbol =='+':
            return num1+num2
        elif simbol =='-':
            return num1-num2
        elif simbol =='*':
            return num1*num2
        elif simbol =='/':
            return num1/num2
        elif simbol =='**':
            return num1**num2
        elif simbol =='//':
            return num1//num2
        elif simbol =='%':
            
            return num1%num2
a = int(input("Первое:"))
s = input("Символ + - * / ** // %: ")
b = int(input("Второе:"))
print(calc(a,s,b))        
        