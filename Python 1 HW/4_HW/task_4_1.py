# Вычислить число c заданной точностью d
from decimal import Decimal


def retrieve_decimal(msg):
    while True:
        try:
            return Decimal(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def round_result(initial_number, required_accuracy):
    final_number = initial_number.quantize(required_accuracy)
    return final_number


number = retrieve_decimal("Введите целое или дробное число: ")
accuracy = retrieve_decimal("Введите дробное число для определения точности вычисления: ")
print(round_result(number, accuracy))
