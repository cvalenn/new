ask_answer = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user():
    while True:
        ask = input("Введите вопрос: ")
        if ask in ask_answer:
            print(ask_answer[ask])


ask_user()
    