# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

while True:
    try:
        n = int(input("Введите свое число: "))
    except ValueError:
        print("Вы вводите не цифровое значение, попробуйте еще раз")
        continue
    break

my_list = []

for i in range(1, n+1):
    number = round((1 + 1/i) ** i, 3)
    my_list.append(number)

print(my_list)

sum_of_digit = round(sum(my_list), 4)
print(sum_of_digit)