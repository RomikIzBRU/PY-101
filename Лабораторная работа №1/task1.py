import doctest

class Furniture:

    def __init__(self, material: str, weight: float, is_assembled: bool):
        """
            Создание и подготовка к работе объекта "Мебель"

            :param material (str): Материал, из которого изготовлена мебель.
            :param weight (float): Вес мебели в килограммах.
            :param is_assembled (bool): Указывает, собрана ли мебель.

            Примеры:
            >>> chair = Furniture("дерево", 4, False) # инициализация экземпляра класса
            """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой.")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        if not isinstance(is_assembled, bool):
            raise TypeError("is_assembled должен быть булевым значением.")
        self.material = material
        self.weight = weight
        self.is_assembled = is_assembled

    def assemble(self) -> None:
        """
        Функция которая собирает мебель.
        Примеры:
            >>> chair = Furniture("дерево", 4, False)
            >>> chair.assemble()
        """
        ...

    def move(self, distance: float) -> None:
        """
        Функция, которая двигает мебель на определенное расстояние.
        :param distance (int,float): Расстояние в метрах.
         :raise ValueError: Расстояние должно быть числовым и должно быть положительным, если нет, вызываем ошибку.
        Примеры:
            >>> chair = Furniture("дерево", 12.5, True)
            >>> chair.move(5.2)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным числом")
        ...

class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param make (str): Производитель транспортного средства.
        :param model (str): Модель транспортного средства.
        :param year (int): Год выпуска.

        Примеры:
        >>> car = Vehicle("Porsche", "Cayeene", 2020)
        """
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой.")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой.")
        if not isinstance(year, int) or year < 1886:
            raise ValueError("Год выпуска должен быть целым числом не ранее 1886 года.")
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """
        Функция, которая запускаеь двигатель транспортного средства.

        Примеры:
        >>> car = Vehicle("Porsche", "Cayeene", 2020)
        >>> car.start_engine()
        """
        ...

    def drive(self, distance: float) -> str:
        """
        Функция, которая управляет транспортным средством и проехать определенное расстояние.

        :param distance (float): Расстояние в километрах. Должно быть положительным.
        :raise ValueError: Если расстояние отрицательное, вызывает ошибку.
        :retrun Количество километров которое проехало транспортное средство
        Примеры:
        >>> car = Vehicle("Porsche", "Cayeene", 2020)
        >>> car.drive(123.4)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным числом")
        ...

class SmartHomeDevice:
    def __init__(self, device_name: str, is_online: bool):
        """
        Создание и подготовка к работе объекта "Устройство умного дома"

        :param device_name (str): Название устройства.
        :param is_online (bool): Статус подключения устройства.

        Примеры:
        >>> device = SmartHomeDevice("Умная лампочка", True)
        """
        if not isinstance(device_name, str):
            raise TypeError("Название устройства должно быть строкой.")
        if not isinstance(is_online, bool):
            raise TypeError("Статус подключения должен быть булевым значением.")
        self.device_name = device_name
        self.is_online = is_online

    def turn_on(self) -> str:
        """
        Функция, которая включает устройство
        :return название устройство которое включили
        Примеры:
        >>> bulb = SmartHomeDevice("Умная лампочка", True)
        >>> bulb.turn_on()

        """
        ...

    def turn_off(self) -> str:
        """
        Функция, которая выключает устройство
        :return название устройство которое выключили
        Примеры:
        >>> bulb = SmartHomeDevice("Умная лампочка", True)
        >>> bulb.turn_off()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()

