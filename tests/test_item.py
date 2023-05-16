"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

Item.pay_rate = 0.8


@pytest.fixture()
def item_tv():
    return Item('Телевизор', 50000, 10)


def test_all(item_tv):
    assert item_tv.all == [item_tv]


def test_calculate_total_price(item_tv):
    assert item_tv.calculate_total_price() == 500000


def test_apply_discount(item_tv):
    assert item_tv.price == 50000
    assert item_tv.apply_discount() is None
    assert item_tv.price == 40000
