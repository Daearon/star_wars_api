import json
import allure
from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""


@allure.epic("Test create place")
class TestCreatePlace:

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        token = json.loads(result_post.text)
        Checking.check_json_token(result_post, list(token))
        Checking.check_json_value(result_post, "status", "OK")

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        token = json.loads(result_put.text)
        Checking.check_json_token(result_put, list(token))
        Checking.check_json_value(result_put, "msg", "Address successfully updated")

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, "address", "100 Lenina street, RU")

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        Checking.check_json_token(result_delete, list(token))
        Checking.check_json_value(result_delete, "status", "OK")

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        token = json.loads(result_get.text)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")

        print("Тестирование создания, изменения и удаления новой локации прошло успешно")
