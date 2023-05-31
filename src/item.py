import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализируем экземпляры класса `Item` данными из файла"""
        cls.all = []

        with open('../src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for dicty in reader:
                price_number = cls.string_to_number(dicty['price'])
                quantity_number = cls.string_to_number(dicty['quantity'])
                cls(dicty['name'], price_number, quantity_number)

    @staticmethod
    def string_to_number(string):
        number = int(float(string))
        return number

    def __add__(self, other):
        """Сложение экземпляров классов по количеству товара в магазине"""
        if isinstance(other, self.__class__) or issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return 'Объект не принадлежит к классу или не наследуется от класса'
