"""Тесты с использованием pytest для модуля phone"""
import pytest
from src.phone import Phone

Phone.pay_rate = 0.8


@pytest.fixture()
def phone_1():
    return Phone("iPhone 11", 30_000, 5, 2)


def test_all(phone_1):
    assert phone_1.all == [phone_1]


def test_calculate_total_price(phone_1):
    assert phone_1.calculate_total_price() == 150000


def test_apply_discount(phone_1):
    assert phone_1.price == 30000
    assert phone_1.apply_discount() is None
    assert phone_1.price == 24000


def test_name(phone_1):
    """Тестируем наименование товара"""
    assert phone_1.name == 'iPhone 11'
    with pytest.raises(Exception) as exc:
        phone_1.name = 'q' * 11
        assert str(exc) == 'Длина наименования товара превышает 10 символов.'


def test_str(phone_1):
    assert str(phone_1) == 'iPhone 11'


def test_repr(phone_1):
    assert repr(phone_1) == "Phone('iPhone 11', 30000, 5, 2)"


def test_number_of_sim(phone_1):
    """Тестируем количество сим-карт"""
    assert phone_1.number_of_sim == 2

    with pytest.raises(ValueError) as val_er:
        phone_1.number_of_sim = 0
        assert str(val_er) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'

    with pytest.raises(ValueError) as val_er:
        phone_1.number_of_sim = 3.0
        assert str(val_er) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'




