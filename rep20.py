# # Написать функцию car_rental(cars, services), которая:
# #  1. Спрашивает у пользователя имя и количество пассажиров.
# #  2. Позволяет арендовать машину (пока не введёт стоп).
# #  3. Проверяет: есть ли такая категория, есть ли свободные машины, хватает ли мест для пассажиров.
# #  4. Если всё ок → спросить количество дней.
# #  5. После выбора машины → спросить про дополнительные услуги (несколько через запятую).
# #  • Каждая услуга оплачивается за все дни аренды.
# #  6. Сохранить заказ (машина, дни, услуги, цена).
# #  7. Если сумма всех заказов > 25000 сом, то скидка 10%.
# #  8. В конце вывести: список арендованных машин (с услугами), итоговую сумму, остаток машин по категориям.

# def car_rental(cars, services):
#     total = 0  # общая сумма всех заказов
#     orders = []  # список заказов

#     name = input("Введите ваше имя: ")
#     try:
#         passengers = int(input("Введите количество пассажиров: "))
#     except ValueError:
#         print("Ошибка: количество пассажиров должно быть числом!")
#         return

#     while True:
#         print("\nДоступные категории машин:")
#         for car_type, info in cars.items():
#             print(f"{car_type} — цена: {info['цена']} сом/день, осталось: {info['машины']} шт, макс пассажиров: {info['макс_пассажиров']}")

#         choice = input("Какую машину хотите арендовать? (для выхода введите 'стоп'): ").title()
#         if choice.lower() == 'стоп':
#             break

#         if choice not in cars:
#             print("Ошибка: нет такой категории машины.")
#             continue

#         if cars[choice]['машины'] <= 0:
#             print("Извините, машин этой категории нет в наличии.")
#             continue

#         if passengers > cars[choice]['макс_пассажиров']:
#             print(f"Ошибка: выбранная машина рассчитана максимум на {cars[choice]['макс_пассажиров']} пассажиров.")
#             continue

#         try:
#             days = int(input("На сколько дней арендуете машину? "))
#             if days <= 0:
#                 print("Количество дней должно быть положительным числом.")
#                 continue
#         except ValueError:
#             print("Ошибка: введите число дней корректно.")
#             continue

#         print("\nДоступные дополнительные услуги (через запятую, если несколько):")
#         for srv_name, srv_price in services.items():
#             print(f"- {srv_name} ({srv_price} сом/день)")

#         services_input = input("Выберите доп. услуги или введите 'нет': ").strip()
#         chosen_services = []
#         services_cost = 0

#         if services_input.lower() != 'нет' and services_input != '':
#             selected_services = [s.strip().title() for s in services_input.split(',')]
#             invalid_services = [s for s in selected_services if s not in services]
#             if invalid_services:
#                 print(f"Ошибка: нет таких услуг: {', '.join(invalid_services)}")
#                 continue
#             for s in selected_services:
#                 chosen_services.append(s)
#                 services_cost += services[s] * days

#         base_cost = cars[choice]['цена'] * days
#         order_cost = base_cost + services_cost

#         total += order_cost
#         cars[choice]['машины'] -= 1

#         orders.append({
#             'машина': choice,
#             'дни': days,
#             'услуги': chosen_services,
#             'цена': order_cost
#         })

#         print(f"Вы арендовали {choice} на {days} дней. Стоимость: {order_cost} сом.")

#     if total > 25000:
#         discount = total * 0.1
#         print(f"\nОбщая сумма до скидки: {total} сом")
#         total -= discount
#         print(f"Вам предоставлена скидка 10%: -{discount:.2f} сом")

#     print("\nВаши заказы:")
#     for i, order in enumerate(orders, 1):
#         uslugi_str = ', '.join(order['услуги']) if order['услуги'] else 'без доп. услуг'
#         print(f"{i}. {order['машина']} на {order['дни']} дней, услуги: {uslugi_str}, стоимость: {order['цена']} сом")

#     print(f"\nИтоговая сумма к оплате: {total:.2f} сом")

#     print("\nОстаток машин по категориям:")
#     for car_type, info in cars.items():
#         print(f"{car_type}: {info['машины']} шт")
#         Пример данных:
# cars = {
#     "Эконом": {"цена": 2000, "машины": 5, "макс_пассажиров": 4},
#     "Комфорт": {"цена": 3500, "машины": 3, "макс_пассажиров": 5},
#     "Бизнес": {"цена": 6000, "машины": 2, "макс_пассажиров": 5},
#     "Внедорожник": {"цена": 8000, "машины": 2, "макс_пассажиров": 7}
# }

# services = {
#     "Детское кресло": 500,
#     "GPS-навигация": 700,
#     "Страховка": 1500
# }

# # Запуск:
# car_rental(cars, services)


