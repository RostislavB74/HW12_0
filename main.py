
def main():
    filename = "address_book.bin"
    try:
        load_address_book(filename)
        print("Address book loaded from file.")
    except FileNotFoundError:
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