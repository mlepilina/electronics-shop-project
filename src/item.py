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

