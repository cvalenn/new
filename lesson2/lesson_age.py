
def activity(age):
    if 2 <= age <= 6:
        return ("Вы учитесь в детском саду")
    elif 7 <= age <= 17:
        return ("Вы учитесь в школе")
    elif 18 <= age <= 68:
        return ("Вы работаете")
    else:
        return ("Введите корректный возраст")

x = input("Добро пожаловать! Введите свой возраст:")
print(activity(int(x)))