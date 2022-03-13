from collections import Counter
import collections
from typing import Collection
from unicodedata import numeric


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вас3я: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

a = [i['first_name'] for i in students]
for i in set(a):
    print(f'{i}: {a.count(i)}')

    


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

a = [i['first_name'] for i in students]
b = max((zip((a.count(i) for i in set(a)), set(a))))
print(f'Самое частое имя среди учеников: {b[-1]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
n=0
while n <3:
    a = n + 1
    class_name = [i['first_name'] for i in school_students[n]]
    b = max(zip((class_name.count(i) for i in set(class_name)), set(class_name)))
    print(f'Самое частое имя в классе {a}: {b[-1]}')
    n += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

n=0
while n <3:
    class_name_list = [i['first_name'] for i in school[n]['students']]
    male = [is_male[i] for i in class_name_list]
    wooman = male.count(False)
    man = male.count(True)
    print(f"Класс {school[n]['class']}: девочки {wooman}, мальчики {man}")
    n+=1





# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school2 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male2 = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

woman_test = {}
man_test = {}
p=0
while p <2:
    class_name_list2 = [i['first_name'] for i in school2[p]['students']]
    print(class_name_list2)
    male = [is_male2[i] for i in class_name_list2]
    woman_count =  male.count(False)
    man_count =  male.count(True)
    woman_test.update({school2[p]['class']:woman_count})
    man_test.update({school2[p]['class']:man_count})
    p+=1


print(f"Больше всего девочек в классе {max(woman_test, key=woman_test.get)}")
print(f"Больше всего мальчиков в классе {max(man_test, key=man_test.get)}")



