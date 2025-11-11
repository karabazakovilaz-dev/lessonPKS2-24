# # print("hello"*100)
# # print("hello")
# # print("hello")
# # print("hello")

# # циклы
# # for | while

# # цикл - это когда прогрмма повторяет одно и то же действие много раз

# # цикл for перебирает элементы какого-то набора (списка, строки, диапазона чисел и т.д.)
# # кфтпу() "генератор чисел". он создает последовательность чисел которые удобно перебирать в цикле
# # range(start, stop, step)
# # циклы: for-для and while-пока

# #  цикл for нужен чтобы повторятть действия несколько раз, (список, строка, диапазон чисел, кортежи и т.д.)
# # for переменная in последовательность:
# #     действие

# # range(start, stop, step) - генератор чисел, он создает поседовательность чисел по которой проходить цикл
# # for перменная in последовательность:
# #     действие
# # for name in range(0, 101, 2):
# #     print(name,'hello')
# #     numbers= []
# #     for num in range(1,101,2):
# #         numbers.append(num)
# #         print(numbers)

# # name = 'Abdul345bosid35'
# # nums = []
# # for n in name:
# #      if n.isdigit():
# #         nums.append(n)
# # print(nums)

# # lista = ['Gena', 'Aibike','Mili']
# # lst = []
# # for l in lista:
# #     lst.append(l.upper())
# #     print(lst)

# # float неизменяемый тип
# # str неизменяемый тип
# # int неизменяемый тип
# # bool неизменяемый тип
# # list [] изменяемый тип данных
# # tuple () неизменяемый тип данных
# # set -  множества - {34,46,557} изменяемый тип
# # dict - dictionary - словарки {key:value} изменяемый тип
# # names = {
 #     'Elnura':18,
 #     'Davlet':24,
 #     'Gena':34,
 # }
 # for n, v in names.items():
 #     print(n, v+1)
     # у нас есть список телефоных номеров, нам надо сооздать программу которая
 #будет спрашивать дейтсвие
 # 1-добавить новый номер телефона 
 # 2-ударить номер телефона
 # 3-поиск имени и вывод имени и телефона
 # 4-изменение имени и телефона
 # также должна быть ровно 9 символов, не больше и не меньше,программа
 # должна проверять это и если не соотвествует длине, то говорить
 # пользвателю о том что надо исправить
#contact_names = {
#    'Davlet': 770700700,
#    'Aliya': 20245645,
#    'Adilet': 550343434,
# }

 num_request = input("1-добавить новый номер телефона\n2-удалить номер телефона\n3-поиск имени и вывод имении телефона\n4-изменение имени и телефона\nВыберите действие: ")
 if num_request =='1':
     new_name = input("Введите имя:").title
     if len(new_name) > 2 and len(new_name)< 20:
         new_numbers = input("Введте номер телефона: ")
         if len(new_numbers) == 9:
             contact_names[new_name] = new_numbers
             print(contact_names)
         else:
             print("номер должен быть 9 символов")
     else:
          print("имя должно быть от 3х и выше символов")
 elif num_request == '2':
     for i, v in contact_names.items():
         print('Имя:', i, "Номер",v)
#        del_name = input("Введите имя для удаления: ").title()
my_list = [1, 2, 3, 4, 5]
         if del_name in contact_names.keys():
print(my_list[::-1])  # [5, 4, 3, 2, 1]


contact_names = {
    'Davlet': '770700700',
    'Aliya': '202456450',
    'Adilet': '550343434',
}

num_request = input("1-добавить новый номер телефона\n2-удалить номер телефона\n3-поиск имени и вывод имени и телефона\n4-изменение имени и телефона\nВыберите действие: ")

if num_request == '1':
    new_name = input("Введите имя: ").title()  # Fixed title() method call
    if 2 < len(new_name) < 20:
        new_numbers = input("Введите номер телефона: ")
        if len(new_numbers) == 9:
            contact_names[new_name] = new_numbers
            print(contact_names)
        else:
            print("Номер должен быть 9 символов")
    else:
        print("Имя должно быть от 3х и выше символов")

elif num_request == '2':
    for name, number in contact_names.items():
        print(f'Имя: {name}, Номер: {number}')
    del_name = input("Введите имя для удаления: ").title()
    if del_name in contact_names:
        del contact_names[del_name]
        print(f"Контакт {del_name} удален")
    else:
        print("Такого имени нет в списке контактов")

elif num_request == '3':
    search_name = input("Введите имя для поиска: ").title()
    if search_name in contact_names:
        print(f"Имя: {search_name}, Номер: {contact_names[search_name]}")
    else:
        print("Контакт не найден")

elif num_request == '4':
    old_name = input("Введите имя контакта для изменения: ").title()
    if old_name in contact_names:
        new_name = input("Введите новое имя: ").title()
        new_number = input("Введите новый номер: ")
        if len(new_number) == 9:
            del contact_names[old_name]
            contact_names[new_name] = new_number
            print("Контакт успешно изменен")
        else:
            print("Номер должен быть 9 символов")
    else:
        print("Такого контакта нет")

else:
    print("Неверный выбор")