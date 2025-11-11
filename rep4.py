tasks = {
    'Сделать домашку': "не сделано",
    'Почистить зубы': "сделано",
}
usl = """
1. Посмотреть список дел.
2. Добавить новое дело.
3. Удалить дело по названию.
4. Отиетить дело как выполненное.
5. Выйти."""
print(usl)
request = input("Выберите действие : ")
if request == '1':
    for delo, status in tasks.items():
        print(delo) 
elif  request == '2':
    new_task = input("Добавить новое дело")
    status = "не сделано"
    tasks[new_task] = status
    for k,v in tasks.items():
        print(k,v)
elif request == '3':
    del_task = input("Введите название дела для удаления: ")
    if del_task in tasks:
        del tasks[del_task]
        print(f"Дело '{del_task}' удалено.")
    else:
        print(f"Дело '{del_task}' не найдено.")
elif request == '4':
    done_task = input("Введите название дела для отметки как выполненое:")
    if done_task in tasks:
        tasks[done_task] = "сделано"
        print(f"Дело '{done_task}' отмечено как выполненное.")
    else:
        print(f"Дело '{done_task}' не найдено.")
elif request == '5':
    print("Выход из программы.")
else:
    print("Некорректный ввод. Пожалюста, выберите действие от 1 до 5.")