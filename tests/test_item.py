"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone

Item.pay_rate = 0.8


@pytest.fixture()
def item_tv():
    return Item('Телевизор', 50000, 10)


@pytest.fixture()
def phone_1():
    return Phone("iPhone 11", 30000, 5, 2)


def test_all(item_tv):
    assert item_tv.all == [item_tv]


def test_calculate_total_price(item_tv):
    assert item_tv.calculate_total_price() == 500000


def test_apply_discount(item_tv):
    assert item_tv.price == 50000
    assert item_tv.apply_discount() is None
    assert item_tv.price == 40000


def test_name(item_tv):
    """Тестируем наименование товара"""
    assert item_tv.name == 'Телевизор'
    with pytest.raises(Exception) as exc:
        item_tv.name = 'q' * 11
        assert str(exc) == 'Длина наименования товара превышает 10 символов.'


def test_instantiate_from_csv():
    """Тестируем инициализацию экземпляров класса `Item` данными из файла"""
    Item.all = []
    assert len(Item.all) == 0
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1
    assert Item.all[4].name == 'Клавиатура'
    assert Item.all[4].price == 75
    assert Item.all[4].quantity == 5


def test_instantiate_from_csv_index_error():
    """Тестируем, что при попытке взять несуществующий элемент возникает ошибка индекса"""
    Item.instantiate_from_csv()
    with pytest.raises(IndexError):
        Item.all[9].name = 'Наушники'


def test_string_to_number():
    """Тестируем функцию, возвращающую  число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_string_to_number_value_error():
    """Тестируем, что при попытке передать пустую строку
    или нечисловой символ возникает ошибка значения
    """
    with pytest.raises(ValueError):
        Item.string_to_number('')
        Item.string_to_number('a')


def test_repr(item_tv):
    assert repr(item_tv) == "Item('Телевизор', 50000, 10)"


def test_str(item_tv):
    assert str(item_tv) == 'Телевизор'


def test_add(item_tv, phone_1):
    """Тестируем метод, который выполняет сложение количества товара в магазине"""
    assert item_tv + phone_1 == item_tv.quantity + phone_1.quantity

