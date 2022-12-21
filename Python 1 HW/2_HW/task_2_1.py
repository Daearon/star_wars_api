# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

while True:
    try:
        number = float(input("Введите свое вещественное число: "))
    except ValueError:
        print("Вы вводите не цифровое значение, попробуйте еще раз")
        continue
    break

while number != int(number):
    number *= 10

sum = 0
while number > 0:
    sum += number % 10
    number //= 10

print(int(sum))
