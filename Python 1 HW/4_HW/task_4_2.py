# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def find_multipliers(number):
    list_of_multipliers = []
    i = 2
    while i <= number:
        if number % i == 0:
            list_of_multipliers.append(i)
            number //= i
        else:
            i += 1
    return list_of_multipliers


initial_number = retrieve_integer("Введите натуральное число: ")
print(find_multipliers(initial_number))