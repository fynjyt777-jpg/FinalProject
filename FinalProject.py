from datetime import datetime



def deadline_score():
    points = 0
    check1 = True
    while check1:
        # Запрашиваем у пользователя дату сдачи работы
        pass_date = input("Введите дату сдачи работы в формате 'ДД.ММ.ГГГГ': ")

        # Проверяем на соответствие заданному формату введенную дату
        try:
            # Преобразуем строку в объект datetime.date или datetime
            pass_date = datetime.strptime(pass_date, "%d.%m.%Y").date()
            print("Дата успешно распознана:", pass_date)
            check1 = False
        except ValueError:
            print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")

    check2 = True
    while check2:
        # Запрашиваем у пользователя дату окончания приема работ
        deadline_date = input("Введите дату окончания приема работ в формате 'ДД.ММ.ГГГГ': ")

        # Проверяем на соответствие заданному формату введенную дату
        try:
            # Преобразуем строку в объект datetime.date или datetime
            deadline_date = datetime.strptime(deadline_date, "%d.%m.%Y").date()
            print("Дата успешно распознана:", deadline_date)
            check2 = False
        except ValueError:
            print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")

    quantity_week = (deadline_date - pass_date).days // 7
    if quantity_week < 0:
        positive_week = abs(quantity_week)
        print(f"Опоздание при сдаче работы составляет {positive_week} нед.")
        if positive_week < 5:
            points = 5 - positive_week
        else:
            points = 0

    else:
        print(f"Работа сдана вовремя, за {quantity_week} нед. до окончания срока")
        points = 5
    print(f"Количество заработанных баллов {points}")
deadline_score()