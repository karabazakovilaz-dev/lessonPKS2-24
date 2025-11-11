# # Новая тема работа с файлам 
# # mode - режим открытия файла
# # r - read - чтение
# # w - write - писать создание нового файла старый очищается
# # a - append - добавление
# # x - создание нового файла, если файл существует ошибка
# # b - binary  используется вместо с rb и wb
# # t - text  текстовый режим по умолчанию
# # open() функция во круг которого все крутятся
# # file = open("имя_файла" , "режим")Новая тема работа с файлам 
# # mode - режим открытия файла
# # r - read - чтение
# # w - write - писать создание нового файла старый очищается
# # a - append - добавление
# # x - создание нового файла, если файл существует ошибка
# # b - binary  используется вместо с rb и wb
# # t - text  текстовый режим по умолчанию
# # open() функция во круг которого все крутятся
# # file = open("имя_файла" , "режим")

# with open('data.txt', 'w', encoding='utf-8') as file:
#     file.write('Сегодня ПКС-2-24 сидять на уроке!\n')
#     file.write('Марсель сегодня тихий!\n')


# with open('sab.txt', 'r', encoding='utf-8') as file:
#     print(file.read())


# # записать в файле sab.txt "а я Миленина отец" но чтобы предущая запись не стерлась
# with open('sab.txt', 'a', encoding='utf-8') as file:
#     file.write('Я Пирожок\n')


# Задача: "блокнот"
# Условие:Создай программу, которая:
while True:
    print("""
    1. Добавляет заметку в файл
    2. Показывает все заметки
    3. Ищет заметку по слову
    4. Заканчивает работу по выбору пользователя""")
    choice = input("Выберите действие: ")
    if choice == '1':
        textUser = input("Что хотите добавить? ")
        with open('blokn  ot.txt', 'a', encoding='utf-8') as file:
            file.write(textUser + '\n')
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        break
    else:
        print("Выбирайте от 1го до 4х")
        continue
    with open('notebook.txt', 'a', encoding='utf-8') as file:
        file.write(textUser + '\n')
    print("Заметка добавлена!")
    with open('notebook.txt', 'r', encoding='utf-8') as file:
        print(file.read())
    findWord = input("Какое слово ищем? ")
    with open('notebook.txt', 'r', encoding='utf-8') as file:
        notes = file.readlines()
        for note in notes:
            if findWord in note:
                print(note)
    print("Работа завершена!")