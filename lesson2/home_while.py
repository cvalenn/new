

def hello_user():
    while True:
        try:
            user_say = input("Как дела? ")
            if user_say == "Хорошо":
                break
        except (KeyboardInterrupt):
            print("Пока")
            break

hello_user()