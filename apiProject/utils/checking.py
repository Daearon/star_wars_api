"""Методы для проверки ответов на завросы"""
import json


class Checking:
    """Метод для проверки кода статуса"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        if result.status_code == status_code:
            print("Успешно, код статуса - " + str(result.status_code))
        else:
            print("Провал, код статуса - " + str(result.status_code))

    """Метод для проверки наличия обязательных полей в теле запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе на запрос"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен")

    """Метод для проверки значений обязательных полей по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует в ответе")
        else:
            print("Слово " + search_word + " отсутствует в ответе")


