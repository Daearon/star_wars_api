# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


list_size = retrieve_integer("Введите число для расчета: ")
number_list = [i+1 for i in range(list_size)]
edited_number_list = list(number_list[i] for i in range (1, len(number_list))
                          if number_list[i] % 20 == 0 or number_list[i] % 21 == 0)
print(number_list)
print(edited_number_list)