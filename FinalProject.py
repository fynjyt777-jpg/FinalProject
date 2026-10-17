from datetime import datetime

def deadline_score():
    # Запрашиваем у пользователя дату сдачи работы
    pass_date = input("Введите дату сдачи работы в формате 'DD.MM.YYYY': ")

    # Проверяем на соответствие заданному формату введенную дату
    try:
        # Преобразуем строку в объект datetime.date или datetime
        pass_date = datetime.strptime(pass_date, "%d.%m.%Y").date()
        print("Дата успешно распознана:", pass_date)
    except ValueError:
        print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")

    # Запрашиваем у пользователя дату окончания приема работ
    deadline_date = input("Введите дату окончания приема работ в формате 'DD.MM.YYYY': ")

    # Проверяем на соответствие заданному формату введенную дату
    try:
        # Преобразуем строку в объект datetime.date или datetime
        deadline_date = datetime.strptime(deadline_date, "%d.%m.%Y").date()
        print("Дата успешно распознана:", deadline_date)
    except ValueError:
        print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")

    quantity_week = (deadline_date - pass_date).days // 7
    if quantity_week > 0:
        print(f"Опоздание при сдаче работы составляет {quantity_week} недели")
    else:
        positive_week = abs(quantity_week)
        print(f"Работа сдана вовремя, за {positive_week} недель до окончания срока")

deadline_score()