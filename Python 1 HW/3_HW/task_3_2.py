# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample
from math import floor


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def create_list_and_find_product(amount, even_2):
    my_list = sample(range(1, (amount+1)*2), k=amount)
    print(my_list)
    new_list = []
    for i in range(len(my_list)):
        while i < len(my_list)/2 and amount > len(my_list)/2:
            amount = amount - 1
            product = my_list[i] * my_list[amount]
            new_list.append(product)
            i += 1
        if not even_2:
            new_list[len(new_list)-1] = my_list[floor(len(my_list)/2)]
    return new_list


number_amount = retrieve_integer("Введите количество чисел в создаваемом списке: ")
even = number_amount % 2 == 0
product_list = create_list_and_find_product(number_amount, even)
print(product_list)




