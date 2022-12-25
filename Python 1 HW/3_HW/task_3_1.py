# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import sample


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def find_number (amount):
    my_list = sample(range(1, (amount+1)*2), k=amount)
    print(my_list)
    sum_of_elements = 0
    for i in range(0, len(my_list), 2):
        sum_of_elements += my_list[i]
    return sum_of_elements


number_amount = retrieve_integer("Введите количество чисел в создаваемом списке: ")
answer = find_number(number_amount)
print(answer)

