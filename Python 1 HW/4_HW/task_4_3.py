# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности в том же порядке.
from random import randint


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def create_random_list(number):
    random_list = []
    for i in range(number):
        random_list.append(randint(0, 10))
    return random_list


def sorted_list(random_list):
    unique_numbers_list = []
    for i in random_list:
        if i not in unique_numbers_list:
            unique_numbers_list.append(i)
    return unique_numbers_list


range_number = retrieve_integer("Введите число: ")
random_list = create_random_list(range_number)
print(random_list)
unique_list = sorted_list(random_list)
print(unique_list)