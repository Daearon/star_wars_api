# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def transforming_in_binary(my_number):
    if my_number == 0:
        zero = [0]
        return zero
    else:
        result = []
        while my_number:
            result.append(my_number%2)
            my_number = my_number//2
        return result[::-1]


number = retrieve_integer("Введите свое десятичное число: ")
binary_list = transforming_in_binary(number)
print(*binary_list, sep="")