# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

def Retrieve_Integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")

number_first = Retrieve_Integer("Введите свою первую позицию: ")
number_second = Retrieve_Integer("Введите свою вторую позицию: ")
N = Retrieve_Integer("Введите число, обозначающее диапазон формирующегося списка: ")

my_list = []
for i in range(-N, N+1):
    my_list.append(i)

print(my_list)

if number_first > 0 and number_second > 0 and number_first < len(my_list) and number_second < len(my_list):
    product = my_list[number_first-1] * my_list[number_second-1]
    print(product)
else:
    print("Для этой позиции в списке нет числа")
