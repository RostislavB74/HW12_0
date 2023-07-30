
# import datetime
from datetime import datetime
from ab_classes_300723 import AddressBook, Name, Phone, Record, Birthday
import re
import pickle

address_book = AddressBook()
filename = 'address_book.txt'


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NameError as e:
            print(
                f"Give me a name and phone number in format +380(88)777-77-77 or date birthday dd/mm/YYYY")
        except IndexError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77 or date birthday dd/mm/YYYY")
        except TypeError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77 or date birthday dd/mm/YYYY")
        except UnboundLocalError as e:
            print("Contact exists")
        except ValueError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77 or date birthday dd/mm/YYYY")
        except AttributeError as e:
            print(
                f"Give me a name and  phone number in format +380(88)777-77-77 or date birthday dd/mm/YYYY")
    return wrapper


def check_bd(args):
    pattern_bd = r'(\d\d)/(\d\d)/(\d{4})'
    if re.fullmatch(pattern_bd, args):
        data = Birthday(args)
        if isinstance(data.value, datetime):
            birthday = data
            # if rec:
            #     birthday = data
            #     rec.add_birthday(birthday)
            # return res
    else:
        birthday = None
    return birthday


def check_phone(args):
    pattern_ph = r"(\+\d{3}\(\d{2}\)\d{3}\-(?:(?:\d{2}\-\d{2})|(?:\d{1}\-\d{3}){1}))"
    if re.fullmatch(pattern_ph, args):
        phone = Phone(args)
        # if rec:
        #     rec.add_phone(phone)
        # return res
    else:
        phone = None
    return phone


@input_error
def add_contact(*args):
    bd = None
    name = Name(args[0])
    list_phones = []
    rec: Record = address_book.get(str(name))
    if rec:
        for i in range(1, len(args)):
            if not rec.birthday:
                bd = check_bd(args[i])
                rec.birthday = bd
                return rec.add_birthday(rec.birthday)
            phone = check_phone(args[i])
            if phone:
                # list_phones.append(phone)
                # phone = list_phones
                return rec.add_phone(phone)
        else:
            return "Unknown command"
    if not rec:
        for i in range(1, len(args)):
            # if not bd:
            bd = check_bd(args[i])
            birthday = bd
            phone = check_phone(args[i])
            if phone:
                list_phones.append(phone)
                phone = list_phones
            rec = Record(name, phone=list_phones, birthday=birthday)
            return address_book.add_record(rec)
        else:
            return "Unknown command"


# змінити
@input_error
def change_phone(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact {name} in address book"


# Вийти
def exit_command(*args):
    return "Good bye!"


# показати контакт
@input_error
def get_phone(*args):
    name = Name(args[0])
    res: Record = address_book.get(str(name))
    result = res.get_phones(res)
    return f"{res.name} : {result}"


# Привіт
def hello(*args):
    return "How can I help you?"


# Невідома команда пуста команда
def no_command(*args, **kwargs):
    return "Unknown command"


# показати все
@input_error
def show_all_command(*args):
    if Record.__name__:
        return address_book
    return

# коли день народження


@input_error
def get_days_to_birthday(*args):
    name = Name(args[0])
    res: Record = address_book.get(str(name))
    result = res.days_to_birthday(res.birthday)
    if result == 0:
        return f'{name } tomorrow birthday'
    if result == 365:
        return f'{name} today is birthday'
    return f'{name} until the next birthday left {result} days'


# Видалити телефон
@input_error
def remove_phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.remove_phone(phone)
    return f"No contact {name} in address book"

# Видалити запис


@input_error
def delete_record(*args):
    name = Name(args[0])
    if name.value in address_book:
        del address_book[name.value]
        return f"Contact '{name}' has been deleted from the address book."
    return f"No contact '{name}' found in the address book."


def save_address_book(*args):
    with open(filename, "w") as file:
        for record in address_book.data.values():
            name = record.name.value
            phones = [phone.value for phone in record.phones]
            birthday = record.birthday.value.strftime(
                "%d/%m/%Y") if record.birthday else ""
            file.write(f"{name} : {','.join(phones)} : {birthday}\n")

    # with open(filename, "w") as file:
    #     for record in address_book.data.values():
    #         name = record.name.value
    #         phones = [phone.value for phone in record.phones]
    #         birthday = record.birthday.value.strftime(
    #             "%d/%m/%Y") if record.birthday else ""
    #         str_cont = f"{name} : {','.join(phones)} : {birthday}\n"
    #         pickle.dumps(str_cont, fh)
    return 'OK'


def load_address_book(filename):
    if filename == 'address_book.txt':
        # address_book = AddressBook()
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(" : ")
                # print(data)
                name = Name(data[0])
                phones = [Phone(phone) for phone in data[1].split(",")]
                birthday = Birthday(data[2]) if data[2] else None
                record = Record(name=name, phone=phones, birthday=birthday)
                address_book.add_record(record)
        return 'Load'

    if filename == 'address_book.bin':
        with open(filename, "rb") as fh:
            data = pickle.load(fh)
            for keys, values in data.items():
                address_book.add_record(values)
        return address_book


# Команди додати, змінити, видалити телефон, вихід, показати все, показати контакт
COMMANDS = {
    exit_command: ("good bye", "bye", "exit", "end", "close", "quit", "0"),
    add_contact: ("add ", "+ ", "1"),
    change_phone: ("change ", "зміни ", "2"),
    remove_phone: ("remove ", "delete ", "del ", "-", "3"),
    show_all_command: ("show all", "show", "4"),
    get_phone: ("phone ", "5"),
    get_days_to_birthday: ("birthday", "bd", "6"),
    delete_record: ("7"),
    save_address_book: ('save_ab'),
    hello: ("hello", "hi", "!",)

}


def parser(text: str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data
    return no_command, []


def main():
    filename = "address_book.bin"
    try:
        load_address_book(filename)
        print("Address book loaded from file.")
    except FileNotFoundError:
        # address_book = AddressBook()
        print("New address book created.")

    while True:
        user_input = input(">>>")
        if user_input == "save":
            save_address_book(address_book, 'address_book_.txt')
            print("Address book saved to file.")
        elif user_input == "save_csv":
            address_book.serialize_to_csv("address_book.csv")
            print("Address book saved to CSV file.")
        elif user_input == "save_json":
            address_book.serialize_to_json("address_book.json")
            print("Address book saved to JSON file.")
        elif user_input == "save_pickle":
            address_book.serialize_to_pickle("address_book.bin")
            print("Address book saved to bin file.")
        elif user_input.startswith("pages"):
            rec_per_page = None
            try:
                rec_per_page = int(user_input[len("pages"):].strip())
            except ValueError:
                rec_per_page = 3
            for rec in address_book.iterator(rec_per_page):
                print(rec)
                input("For next page press any key")
        else:
            cmd, data = parser(user_input)
            result = cmd(*data)
            print(result)
            if cmd == exit_command:
                break


if __name__ == "__main__":
    main()
# def main():
#     while True:
#         user_input = input(">>>")
#         if user_input.startswith("pages"):
#             rec_per_page = None
#             try:
#                 rec_per_page = int(user_input[len("pages"):].strip())
#             except ValueError:
#                 rec_per_page = 3
#             for rec in address_book.iterator(rec_per_page):
#                 print(rec)
#                 input("For next page press any key")
#         else:
#             cmd, data = parser(user_input)
#             result = cmd(*data)
#             print(result)
#             if cmd == exit_command:
#                 break


# if __name__ == "__main__":
#     main()
