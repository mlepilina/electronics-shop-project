"""Тесты с использованием pytest для модуля keyboard"""
import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard_1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_name_keyboard(keyboard_1):
    """Тестируем наименование клавиатуры"""
    assert str(keyboard_1) == "Dark Project KD87A"


def test_name_language(keyboard_1):
    """Тестируем язык по умолчанию"""
    assert str(keyboard_1.language) == "EN"


def test_change_lang_1(keyboard_1):
    """Тестируем изменение языка с помощью метода change_lang"""
    assert keyboard_1.change_lang() == keyboard_1
    assert str(keyboard_1.language) == "RU"


def test_change_lang_2(keyboard_1):
    """Тестируем изменение языка с помощью метода change_lang"""
    assert keyboard_1.change_lang().change_lang() == keyboard_1
    assert str(keyboard_1.language) == "EN"


def test_cant_change_lang(keyboard_1):
    """Тестируем невозможность изменить язык напрямую"""
    with pytest.raises(AttributeError) as attr_er:
        keyboard_1.language = 'CH'
        assert str(attr_er) == "property 'language' of 'KeyBoard' object has no setter"

