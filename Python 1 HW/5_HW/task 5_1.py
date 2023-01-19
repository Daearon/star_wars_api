#Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

import random
import sys


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


initial_text = "абв"
amount_of_words = retrieve_integer("Enter your amount of words: ")
if amount_of_words <= 0:
    sys.exit("Entered data is incorrect")

list_of_words = []
for i in range(amount_of_words):
    created_text = random.sample(initial_text, 3)
    list_of_words.append("".join(created_text))

print(" ".join(list_of_words))

redacted_list_of_words = list(filter(lambda i: initial_text not in i, list_of_words))
print(" ".join(redacted_list_of_words))

