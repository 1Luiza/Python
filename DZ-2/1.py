"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не
запрашивать у пользователя, а указать явно, в программе.hhh hhhh
"""


lst = [5, 'one', 0.1, None]
for el in lst:
    print(f"{el} - {type(el)}")
