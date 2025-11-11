# args* kwargs
# argument

def add(*args):
    print(sum(args)) # + числа

add(5,6,7,8,9,0,89)

def add(*args):
    print(args) # Просто выводить числа

add(5,6,7,8,9,0,89)

a = [5,6,7,8,9,]
b = [1,2,*a,3,4]
print(b)

def sum2(*args):
    total = 0
    for n in args:
        total+=n
    print(f"Сумма: {total}")

sum2(1,2,3,4,5,6,7,8,9,12,46)


def printScore(student, *args):
    print(f"Имя: {student}")
    for sc in args:
        print(sc, end=',')

printScore("Мао", 2,2,3,4,4,3,2)


# **Kwargs KEYWORD ARGUMENTS - DICT {KEY:VALUE}
def show(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

show(name='Мао', age='17', birth='12.12.2000', cit="Bshkek")


def pets(owner, **kwargs):
    print(f"Хозяин: {owner}")
    for k,v in kwargs.items():
        print(k,v)

pets('Zahid', dog='Bobik', cat='bruda', eats=['fish', 'meat', 'water'])

#  Комбинация
# def demo(a, *args, **kwargs):
#     print('a =',a)
#     print('args =',args)
#     print('kwargs=',kwargs)

# demo('Gena', 3,4,5,6,7,56,7,8,9 age=45, hobbi='Гимнастика', phone='Redmi')