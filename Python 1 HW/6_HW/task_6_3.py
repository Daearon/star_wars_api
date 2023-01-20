# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")


def create_and_sort_dict(some_list):
    result = {}
    for i in some_list:
        colleague_name = i[0]
        if colleague_name not in result:
            result[colleague_name] = []
        result[colleague_name].append(i)
    result_keys = list(result.keys())
    result_keys.sort()
    sorted_result = {i: result[i] for i in result_keys}
    return sorted_result


names_list = []
amount = retrieve_integer("Введите количество сотрудников, чьи имена Вам необходимо обработать: ")
for i in range(amount):
    name = input("Введите имя сотрудника: ")
    names_list.append(name)

print(create_and_sort_dict(names_list))