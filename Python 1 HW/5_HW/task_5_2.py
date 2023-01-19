# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

initial_file_name = input("Enter the name of the file with the text: ")
data = input("Enter your text for further redact(e.g. aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvv: ")
final_file_name = input("Enter the file name to record: ")

with open(initial_file_name + ".txt", 'w', encoding='UTF-8') as fp:
    print(data, file=fp)
with open(initial_file_name + ".txt", 'r') as file:
    initial_text = file.readline()
    text_split = initial_text.split()


def encoded(some_string):
    encoding_part = ''
    previous_char = ''
    count = 1
    if not some_string:
        return ''
    for char in some_string:
        if char != previous_char:
            if previous_char:
                encoding_part += str(count) + previous_char
            count = 1
            previous_char = char
        else:
            count += 1
    else:
        encoding_part += str(count) + previous_char
        return encoding_part


text_split = encoded(initial_text)
with open(final_file_name + ".txt", 'w', encoding='UTF-8') as file:
    file.write(f'{text_split}')
print(text_split)