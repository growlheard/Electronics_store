import os

import pytest

from electronics_store import __version__
from electronics_store.main import Item, Phone, KeyBoard


def test_version():
    assert __version__ == '0.1.0'


# тестируем метод calculate_total_price
def test_calculate_total_price():
    # создаем экземпляр класса Item
    item = Item("Телефон", 100, 2)
    # проверяем, что общая стоимость товара правильно рассчитывается
    assert item.calculate_total_price() == 200


# тестируем метод apply_discount
def test_apply_discount():
    # создаем экземпляр класса Item
    item = Item("Телефон", 100, 2)
    # применяем скидку
    item.apply_discount()
    # проверяем, что цена товара изменилась с учетом скидки
    assert item.price == 100 * item.pay_rate


def test_create_items_from_csv():
    # Путь к файлу с данными
    file_path = os.path.join(os.path.dirname(__file__), 'items.csv')

    # Создаем товары из файла
    Item.create_items_from_csv(file_path)
    assert len(Item.items_list) == 5

    # Проверяем атрибуты первого товара
    item1 = Item.items_list[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1

    # Проверяем атрибуты второго товара
    item2 = Item.items_list[1]
    assert item2.name == 'Ноутбук'
    assert item2.price == 1000
    assert item2.quantity == 3

    # Проверяем атрибуты третьего товара
    item3 = Item.items_list[2]
    assert item3.name == "Кабель"
    assert item3.price == 10
    assert item3.quantity == 5


def test_sim_card_property():
    # Проверяем что тест отрабатывает верно и возвращает ожидаемое значение
    phone = Phone("Test Phone", 500, 5, 2)
    assert phone.sim_card == 2


def test_sim_card_setter():
    # Проверяем, что setter для sim_card выбрасывает исключение
    phone = Phone("Test Phone", 500, 5, 2)
    with pytest.raises(ValueError):
        phone.sim_card = 0


def test_add_method():
    # Проверяем, что метод add правильно складывает цены двух объектов
    phone1 = Phone("Phone 1", 500, 5, 2)
    phone2 = Phone("Phone 2", 700, 3, 1)
    assert phone1 + phone2 == 1200


def test_add_method_invalid_argument():
    # Проверяем, что метод add выбрасывает исключение
    phone = Phone("Test Phone", 500, 5, 2)
    with pytest.raises(ValueError):
        phone + 5


def test_change_lang_ru_to_en():
    kb = KeyBoard('Dark', 9600, 5)
    kb._language = "RU"
    kb.change_lang()
    assert kb._language == "EN"


def test_change_lang_en_to_ru():
    kb = KeyBoard('Dark', 9600, 5)
    kb._language = "EN"
    kb.change_lang()
    assert kb._language == "RU"
