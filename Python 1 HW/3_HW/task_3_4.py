# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")



def creating_list(list_length):
    new_list = []
    for i in range(list_length):
        float_number = uniform(0, 9)
        new_list.append(round(float_number, 2))
    return new_list


def finding_difference(new_list):
    min = new_list[0]
    max = 0
    for i in range(len(new_list)):
        if max < new_list[i]:
            max = new_list[i]
        if min > new_list[i]:
            min = new_list[i]
    difference = max - min
    return max, min, round(difference, 2)


length_of_list = retrieve_integer('Введите размер списка: ')
formed_list = creating_list(length_of_list)
print(formed_list)
print(finding_difference(formed_list))


