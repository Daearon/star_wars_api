import csv
from utils.api import ApiRest
from utils.checking import Checking

"""Запросы на получение информации о Дарте Вейдере, фильмах с его участием и персонажей этих фильмов"""


class TestGetInfo:


    """Метод для записи в csv файл"""
    @staticmethod
    def write_names_to_file(names: set[str]):
        with open("file_name.csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for name in names:
                writer.writerow([name])

    def test_get_information(self):
        print("Метод GET - Вейдер")
        result_get_veider = ApiRest.get_veider()  # Получение объекта, ответа на запрос GET
        check_get_veider = result_get_veider.json()
        films = check_get_veider.get("films") # Получение параметра films и списка из url фильмов
        Checking.check_status_code(result_get_veider, 200)

        print("Метод GET - films")
        result_get_films = ApiRest.get_films_characters_url(films) # Получение множества из url персонажей
        print(result_get_films)

        print("Метод GET - characters")
        result_get_characters = ApiRest.get_characters(result_get_films) # Получение множества имен персонажей
        print(result_get_characters)


        self.write_names_to_file(result_get_characters) # запись множества с именами персонажей в файл

        print("Тестирование получения информации прошло успешно")
