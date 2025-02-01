#Был выбран 1 вариант (Автомобили)

class Car:
    """
    Базовый класс для автомобилей.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует объект автомобиля.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
        """
        self.brand: str = brand
        self.model: str = model
        self.year: int = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        Возвращаемое значение:
            str: Строковое представление автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление автомобиля.

        Возвращаемое значение:
            str: Официальное представление объекта.
        """
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Возвращаемое значение:
            str: Сообщение о запуске двигателя.
        """
        return f"{self.brand} {self.model} двигатель запущен."


class PassengerCar(Car):
    """
    Дочерний класс для легковых автомобилей.

    Новый атрибут:
        passenger_capacity (int): Количество пассажиров, которое может вместить автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int) -> None:
        """
        Инициализирует объект легкового автомобиля.

        Расширяет конструктор базового класса, добавляя количество пассажиров.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            passenger_capacity (int): Количество пассажиров.
        """
        super().__init__(brand, model, year)
        self.passenger_capacity: int = passenger_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        Возвращаемое значение:
            str: Строковое представление легкового автомобиля с информацией о пассажирах.
        """
        base_str: str = super().__str__()
        return f"{base_str}, Вместимость: {self.passenger_capacity} пассажиров"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление легкового автомобиля.

        Возвращаемое значение:
            str: Официальное представление объекта легкового автомобиля.
        """
        return (f"PassengerCar(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"passenger_capacity={self.passenger_capacity})")

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя для легкового автомобиля.

        Перегрузка осуществлена для того, чтобы добавить информацию о пассажирской вместимости при запуске двигателя.

        Возвращаемое значение:
            str: Сообщение о запуске двигателя с учетом работы легкового автомобиля.
        """
        base_message: str = super().start_engine()
        return f"{base_message} Готов к перевозке до {self.passenger_capacity} пассажиров."

class CargoTruck(Car):
    """
    Дочерний класс для грузовых автомобиле.

    Дополнительные атрибуты:
        cargo_capacity (float): Грузоподъемность автомобиля.
    """
    def __init__(self, brand: str, model: str, year: int, cargo_capacity: float) -> None:
        """
        Инициализирует объект грузового автомобиля.

        Расширяет конструктор базового класса, добавляя атрибут грузоподъемности.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска.
            cargo_capacity (float): Грузоподъемность.
        """
        super().__init__(brand, model, year)
        self.cargo_capacity: float = cargo_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        Возвращаемое значение:
            str: Строковое представление с информацией о грузоподъемности.
        """
        base_str: str = super().__str__()
        return f"{base_str}, Грузоподъемность: {self.cargo_capacity} т"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        Возвращаемое значение:
            str: Официальное представление объекта.
        """
        return (f"CargoTruck(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"cargo_capacity={self.cargo_capacity})")

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя для грузового автомобиля.

        Перегрузка выполнена для добавления информации о грузоподъемности, так как грузовые автомобили
        имеют особенности в запуске двигателя, связанные с перевозкой тяжёлых грузов.

        Возвращаемое значение:
            str: Сообщение о запуске двигателя с учетом специфики грузового автомобиля.
        """
        base_message: str = super().start_engine()
        return f"{base_message} Грузовой автомобиль готов перевозить грузы до {self.cargo_capacity} тонн."


if __name__ == "__main__":
    generic_car = Car("TestoviyBrand", "TestovayaModelka", 2025)
    print(generic_car)
    print(repr(generic_car))
    print(generic_car.start_engine())

    passenger_car = PassengerCar("Geely", "AtlasPro", 2023, 5)
    print(passenger_car)
    print(repr(passenger_car))
    print(passenger_car.start_engine())

    cargo_truck = CargoTruck("Volvo", "FH16", 2021, 18.4)
    print(cargo_truck)
    print(repr(cargo_truck))
    print(cargo_truck.start_engine())