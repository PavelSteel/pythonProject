from datetime import datetime  # из библиотеки импортировали модуль

# print(дата/время.сейчас())

all_messages = []  # пустой список. В этом списке мы будем хранить информацию (имя пользователя, сообщение, время отправки сообщений)


# функция появляется сообщение в списке all_messages
def add_message(sender,
                text):  # def - мы создаем функцию. Далее - идет название функции (add_message), а внутри скобок - аргументы, которые передаем в функции


    all_messages = []  # пустой список. В этом списке мы будем хранить всю информацию (имя пользователя, сообщение, время отправки сообщения)


# функция добавляет сообщение в список all_messages
def add_message(sender,
                text):  # def - мы создаем функцию. Далее - идет название функции (add_message), а внутри скобок - агрументы, которые передаем в функцию
    new_message = {
        'sender': sender,  # ключ : значение
        'text': text,
        'time': datetime.now()
    }
    all_messages.append(new_message)


# функция для печати информации о сообщениях
def print_message(new_message):
    print('Отправитель', new_message['sender'], '| Текст:', new_message['text'], '| Время отправления:',
          new_message['time'])


def print_all_messages(all_messages):
    for new_message in all_messages:
        print_message(new_message)
