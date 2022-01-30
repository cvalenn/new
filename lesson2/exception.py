def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except (ZeroDivisionError, TypeError):
        print('Не могу поделить')

cut_cake(0)