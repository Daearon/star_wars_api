from utils.http_requests import HttpMethods

"""Метод для тестирования Api Root"""

base_url = "https://swapi.dev"  # базовый url


class ApiRest:


    @staticmethod
    def get_veider():
        """метод для получения информации о Вейдере"""
        get_resource_vader = "/api/people/4/"  # Ресурс метода GET vader
        get_url = base_url + get_resource_vader
        print(get_url)
        result_get_veider = HttpMethods.get(get_url)
        print(result_get_veider.text)
        return result_get_veider

    @staticmethod
    def get_films_characters_url(films) -> set[str]:
        """метод для получения информации о фильмах"""
        set_characters_url = set()
        for film in films:
            get_url = film  # URL метода GET films
            print(get_url)
            result_get_films = HttpMethods.get(get_url)
            print(result_get_films.text)
            check_get_films = result_get_films.json()
            characters = check_get_films.get("characters")  # получение списка из url персонажей
            for i in characters:  # цикл для преобразования списка в множество url
                set_characters_url.add(i)
        return set_characters_url

    @staticmethod
    def get_characters(set_characters_url: set[str]) -> set[str]:
        """метод для получения информации о персонажах из фильмов"""
        set_characters = set()
        for i in set_characters_url:   # Проходим циклом по url персонажей
            get_url = i  # URL метода GET characters
            print(get_url)
            result_get_characters = HttpMethods.get(get_url)
            print(result_get_characters.text)
            check_get_films = result_get_characters.json()
            character_name = check_get_films.get("name") # получаем имена персонажей
            set_characters.add(character_name) # формируем множество с уникальными именами персонажей
        return set_characters
