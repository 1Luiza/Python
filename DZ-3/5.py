"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
после этого завершить программу.
"""

def get_sum(my_sum=0):
    lst = input("Введите числа через пробел: ").split()
    for el in lst:
        if el != "q":
            my_sum = my_sum + int(el)
        else:
            break
        print(my_sum)
        if "q" in lst:
            exit("Выход из программы")
        else:
            get_sum(my_sum)

get_sum()

