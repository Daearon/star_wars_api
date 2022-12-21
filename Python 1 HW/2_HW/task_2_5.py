# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

import random
initial_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(initial_list)
for i in range(len(initial_list)-1, 0, -1):
    k = random.randint(0, i + 1)
    initial_list[i], initial_list[k] = initial_list[k], initial_list[i]
print(initial_list)
