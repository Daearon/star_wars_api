from OOP_Project.Car import Car

class Truck(Car):
    """Создание класса грузовика"""
    def __init__(self, model, year_of_product, engine_capacity, price, mileage):
        """Инициализация атрибутов класса родителя"""
        super().__init__(model, year_of_product, engine_capacity, price, mileage)
        self.number_of_wheels = 8

    def description(self):
        """Описание грузовика"""
        print(f"Грузовик модели {self.model} {self.year_of_product} года производства, мощность двигателя "
              f"{self.engine_capacity} лошадиных сил, стоимость составляет {self.price}, пробег {self.mileage} километров, "
              f"количество колес - {self.number_of_wheels}")

