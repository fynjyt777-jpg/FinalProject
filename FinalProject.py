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
# deadline_score()



def late_list():
    dict = {}
    check0 = True
    while check0:
        check1 = True
        while check1:
            # Запрашиваем у пользователя фамилию пользователя
            name = input("Введите фамилию студента: ").strip()  # .strip() - удаляет пустую строку

            if not name:  # Если пришла пустая строка
                print("Вы ввели пустую строчку!")
            elif name.isalpha():  # Если строка состоит только из букв
                check1 = False
            else:
                print("Фамилия должна состоять из букв!")

        check2 = True
        while check2:
            # Запрашиваем у пользователя дату сдачи работы
            pass_date = input("Введите дату сдачи работы в формате 'ДД.ММ.ГГГГ': ")

            # Проверяем на соответствие заданному формату введенную дату
            try:
                # Преобразуем строку в объект datetime.date или datetime
                pass_date = datetime.strptime(pass_date, "%d.%m.%Y").date()
                print("Дата успешно распознана:", pass_date)
                check2 = False
            except ValueError:
                print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")
        dict[name] = pass_date

        choise = input("Ввести данные уще одного студента? \n Введите 1 если Да или 2 если Нет: ")

        match choise:
            case "1":
                print("Продолжаем ввод данных для проверки")
            case "2":
                print("Переходим на следующий шаг")
                check0 = False
            case _:
                print("Введите 1 или 2!")

    check3 = True
    while check3:
        # Запрашиваем у пользователя дату окончания приема работ
        deadline_date = input("Введите дату окончания приема работ в формате 'ДД.ММ.ГГГГ': ")

        # Проверяем на соответствие заданному формату введенную дату
        try:
            # Преобразуем строку в объект datetime.date или datetime
            deadline_date = datetime.strptime(deadline_date, "%d.%m.%Y").date()
            print("Дата успешно распознана:", deadline_date)
            check3 = False
        except ValueError:
            print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")

    result = {name: pass_date for name, pass_date in dict.items() if pass_date > deadline_date}
    print(result)


late_list()
