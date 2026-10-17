from datetime import datetime

def deadline_score():
    # Запрашиваем у пользователя дату сдачи работы
    pass_date = input("Введите дату сдачи работы в формате 'DD.MM.YYYY': ")

    # Проверяем на соответствие заданному формату введенную дату
    try:
        # Преобразуем строку в объект datetime.date или datetime
        date_obj = datetime.strptime(pass_date, "%d.%m.%Y").date()
        print("Дата успешно распознана:", date_obj)
    except ValueError:
        print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")

    # Запрашиваем у пользователя дату окончания приема работ
    deadline_date = input("Введите дату окончания приема работ в формате 'DD.MM.YYYY': ")

    # Проверяем на соответствие заданному формату введенную дату
    try:
        # Преобразуем строку в объект datetime.date или datetime
        date_obj = datetime.strptime(deadline_date, "%d.%m.%Y").date()
        print("Дата успешно распознана:", date_obj)
    except ValueError:
        print("Неверный формат даты! Пожалуйста, используйте ДД.ММ.ГГГГ")



