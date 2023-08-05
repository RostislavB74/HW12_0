from bot import Bot


if __name__ == "__main__":
    # print('Hello. I am your contact-assistant. What should I do with your contacts?')
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    print('Вітаю. Я Ваш контакт-помічник. Чим я можу Вам допомогти?')
    # print('Для отримання інформації щодо команд введіть help')
    # bot = Bot()
    # bot.book.load("auto_save")
    commands = ['Add-Додати', 'Search-Пошук', 'Edit-Редагувати', 'Load-Загрузити',
                'Remove-Видалити', 'Save-Зберігти', 'Congratulate-Привітати',
                'View-Дивитись', 'Exit-Вихід']
    while True:
        action = input('Type help for list of commands or enter your command\n\
Для отримання інформації щодо команд введіть help або введіть команду на англійській мові\
                       \n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands:
                print(format_str.format(command))
                action = input().strip().lower()
            bot.handle(action)
        #     if action in ['add', 'remove', 'edit']:
        #         bot.book.save("auto_save")
        # else:
        #     bot.handle(action)
        #     if action in ['add', 'remove', 'edit']:
        #         bot.book.save("auto_save")
        if action == 'exit':
            break
