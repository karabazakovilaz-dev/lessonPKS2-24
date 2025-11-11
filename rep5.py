tasks = {
    'Сделать домашку': "не сделано",
    'Почистить зубы': "сделано",
}
usl = """
1. Посмотреть список дел.
2. Добавить новое дело.
3. Удалить дело по названию.
4. Отметить дело как выполненное.
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
    print(tasks)
    