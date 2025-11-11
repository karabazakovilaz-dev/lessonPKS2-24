# def numpl(x, y):
#     return x*y
# print(numpl(4,7))

# np = lambda x, y: x*y
# print(np(6,8))
# # 
# orders = ['чай', 'кофе', 'молоко', 'Капучино', 'латте']
# # 1. Отфильтровать заказы, длинее 4 символов
# long_orders = list(filter(lambda order: len(order.lower()) > 4, orders))
# print(long_orders)
# # 2) покозать заказы начинающиеся с буквы "к" без учета регистра
# k_orders = list(filter(lambda k:k.lower().startswith('к'), orders))
# print(k_orders)
# # 3) Преобразовать все что внутри в верхний регистр
# upper_orders = list(map(lambda up: up.upper(), orders))
# print(upper_orders) 

# orders = [
#     {"Название": "чай", "Цена": 120, "Категория": "напиток"},
#     {"название": "кофе", "Цена": 80, "Категория": "напиток"},
#     {"название": "молоко", "Цена": 150, "Категория": "десерт"},
#     {"название": "Салат", "Цена": 200, "Категория": "основное"},
# ]
# # 1
# exp = list(filter(lambda e: e['Цена'] > 150, orders))
# print(exp)
# # 2
# max_item = max(orders, key=lambda x:x['Цена'])
# print(max_item)
# # 3
sort_ord = sorted(orders, key=lambda s:s['Цена'])
for o in sort_ord:
    print(F"{o['название']} - {o['Цена']} - {o['Категория']}")
# 4 
has_dessert = any(o(['Категория'] == 'десерт', orders))
print("Есть ли десерт?:", "Да" if has_dessert else "Нет")
products = [
    {"name": "Футболка", "price": 800, "size":"M", "category":"мужская"}, 
    {"name": "Платье", "price": 1500, "size":"L", "category":"женская"},
    {"name": "Куртка", "price": 3500, "size":"XL", "category":"мужская"},
    {"name": "Шорты", "price": 1200, "size":"S", "category":"Детская"},
    {"name": "ДЖинсы", "price": 2200, "size":"Д", "category":"мужская"},
]