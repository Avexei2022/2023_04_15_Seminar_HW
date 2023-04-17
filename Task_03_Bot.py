
from operator import contains


def get_text_from_file(filename):
    data = open(filename, encoding='utf-8')
    text = data.readlines()
    data.close()
    return text

def get_bot_dictionary(text):
    bot_dict = {}
    for i in range(len(text)):
        dialog_phrase = text[i].split(':')
        bot_dict[dialog_phrase[0]] = dialog_phrase[1]
    return bot_dict


def dialogue(bot_dict):
    print("\nДиалог с Ботей\n")
    while True:
        question = input('Вы: ').lower()
        if contains(bot_dict, question):
            print(f'Бот: {bot_dict[question]}')
        else:
            print("Бот: Не понял. Повтори.\n")
        print("Для выхода нажми Ctrl+C\n")


a = get_text_from_file('bot.txt')
b = get_bot_dictionary(a)
dialogue(b)
