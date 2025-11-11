plans = {
    "Месячный": {"цена": 10000, "места": 10, "уровень": "Начальный", "Тренировок": 12 },
    "Полугодовой": {"цена": 45000, "места": 5, "уровень": "Средний", "Тренировок": 72 },
    "Годовой": {"цена": 80000, "места": 3, "уровень": "Продувирнутый", "Тренировок": 150 }
}

services = {
    "Тренер": 5000,
    "Питание": 3000,
    "Бассейн": 4000
}
def fitnes_center(plans, services,clients):
    total = 0
    orders = []
    name = input("Ваше имя: ").title().strip()
    if name in clients:
        print(f"С возвращением, {name}")
        level = clients(name)['уровень']
        points = clients[name]['баллы']
    else:
        print("Добро пожаловать в фитнес зал")
        level = input("Ваш уровень для тренировок [начальный / средний / продвинутый]: ")
        clients[name] = {'уровень': level, "баллы": 0, "история": []}
        points = 0 #ball
    level_rank = {'начальный':1, 'средний':2, 'продувинутый':3}
    if level not in level_rank:
        print("Ошибка: неверный уровень")
        return
    
    while True:
        print("Доступно абноменты:")
        for plan, info in plans.items():
            print(plan, info)
        choice = input("Выберите абонимент (или 'cтоп')").title().strip()
        if choice == 'Стоп':
            break
        if choice not in plans:
            print("Такого абонемента нет.")
            continue
        if plans[choice]["места"] == 0
            print("Месь не осталось")
            continue
        if level_rank[level]< level_rank[plans[choice]['уровень']]:
           print("Ваш уровень недостаточнен для этого абонемента")
           continue
        try:
            count = int(input("Количество абонементов хотите? "))
        except ValueError  
        print("Пишите только числа")
        continue
    if count > plans[choice]["Места"]:
        print("Числ")







                 