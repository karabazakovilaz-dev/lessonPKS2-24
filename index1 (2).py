# # name = 'Bilal'
# # prof = 'student'
# # age = 16
# # # конкатенация строк (сложные строк) с помошью +
# # bio = 'I am '+name+','+str(age)+' years, I am a '+prof 
# # print(bio)
# # # форматирофание строк с помошью f-строк
# # bio2 = f'I am {name}, {age} years, I am a {prof}'
# # print(bio2)
# # # форматирование строк с помошью метода format 
# # bio3 = 'I am {0}, {1} years, I am a {2}'.format(name, age, prof)
# # print(bio3) 

# # # индексы это порядковый номер символа в строке 
# # # индексы начинаются с 0
# # name = 'Elnura Abdullaeva Rashidovna'
# # print(name[7],name[8],name[9],name[10],name[11],name[12],name[13],name[14])

# # # срезы строк (substring) (start:stop:step)
# # print(name[0:6]) # с 0 тндекса по 6 не включая
# # print(name[7:17]) # 
# # print(name[0:14:2]) #  шаг 2  
# # print(name[:6]) # с начала по 6 не включая
# # print(name[::-1]) # реверс строки

# # age = int(input('Ведите ваш возраст:'))
# # age = int(age) # проебразование строки и целое число
# # if  age >= 16 and age < 16:
# #     print('пока рано')
# # elif age >= 16 and age < 18:
# #     print('готовься службе')
# # elif age >= 18 and age <= 45:
# #     print('идем служить')
# # elif age > 454 and age <= 60:
# #      print('пора на пенсию')
# # elif age > 60 and age <= 100:


# contact_names = ['Elnura', 'Yusuf', 'Denis', 'Aibiyke', 'Aijan']
# print("Ващи контакты", contact_names)
# request = int(input("Нажмите на 1 - если хотите добавить новое имя \nНажмите на 2 - если хотите искать имя\nНажмите нв 3 - если хотите удалить имя \nВаш выбор:"))
# if request == 1: 
#      new_name = input('Введите имя для поиска: ')
#      contact_names.append(new_name)
#      print(contact_names)
# elif request == 2:
#       name = input('Введите имя для поиска: ')
#       if name in contact_names:
#             print(name)
#       else:
#             print("Нет ткого имени") 
# elif request == 3:
#       name =  input('Введите имя для удаленния: ').title()
#       if name in contact_names:
#             contact_names. remove(name)
#             print(contact_names)
#       else:
#             print("нет такого имени")
contact_names = ['Пицца', 'Бургер', 'Суши', 'Салат', 'Паста']
print("Ваши блюда:", contact_names)
request = int(input("Нажмите на 1 - если хотите добавить новое блюдо\nНажмите на 2 - если хотите искать блюдо\nНажмите на 3 - если хотите удалить блюдо\nНажмите на 4 - если хотите изменить блюдо\nВаш выбор:"))
if request == 1:
    new_name = input('Добавить нове блюдо для заказа: ').title()
    contact_names = "append" (new_name)
    print(contact_names)
elif request == 2:
    name = input('Проверить, есть ли блодо в заказе:').title()
    if name in contact_names:
     print(name)
    else:
     print("нет такого блюда")
elif request == 3:
    name = input('Удалить блюда из заказа:').title()
    'if' in contact_names
    contact_names.remove(name)
    print(contact_names)
else:
    print("нет такого блюда")
    if request == 4:
       name = input('Изменить блюдо из заказа:')
       'if' in contact_names
       contact_names.remove(name)
       print(contact_names)
    else:
       print("блюдо изменино")
      