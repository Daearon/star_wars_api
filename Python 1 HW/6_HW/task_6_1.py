# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
import random


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


list_size = retrieve_integer("Введите размер вашего списка: ")
number_list = [random.randint(1, 30) for i in range(list_size)]
edited_number_list = list(number_list[i] for i in range (1, len(number_list)) if number_list[i] > number_list[i-1])
print(number_list)
print(edited_number_list)