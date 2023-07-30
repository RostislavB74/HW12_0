import datetime
# import telebot
# from time import strftime


def main_bd(date):
    # print(date)
    # test_date = input("Ввведите дату в формате 'dd-mm-yyyy': ")
    str_date = str(date)
    now = datetime.datetime.now()
    then = datetime.datetime.strptime(str_date, "%d/%m/%Y")
    delta1 = datetime.datetime(now.year, then.month, then.day)
    delta2 = datetime.datetime(now.year+1, then.month, then.day)
    # print(delta1)
    # print(delta2)
    result = ((delta1 if delta1 >= now else delta2) - now).days
    # print(result)
    return result


if __name__ == "__main__":
    main_bd()
