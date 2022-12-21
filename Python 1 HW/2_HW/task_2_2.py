# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

while True:
    try:
        N = int(input("Введите свое число: "))
    except ValueError:
        print("Вы вводите не цифровое значение, попробуйте еще раз")
        continue
    break

my_list = []
product = 1

for i in range(N):
    i = i + 1
    product *= i
    my_list.append(product)

print(my_list)
