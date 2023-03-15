import os

import pytest

from electronics_store import __version__
from electronics_store.exceptions import InstantiateCSVError
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
    assert item1.name == 'Smartphone'
    assert item1.price == 100
    assert item1.quantity == 1

    # Проверяем атрибуты второго товара
    item2 = Item.items_list[1]
    assert item2.name == 'Notebook'
    assert item2.price == 1000
    assert item2.quantity == 3

    # Проверяем атрибуты третьего товара
    item3 = Item.items_list[2]
    assert item3.name == "Cable"
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
    # Проверяем, что метод меняет язык на EN
    kb = KeyBoard('Dark', 9600, 5)
    kb._language = "RU"
    kb.change_lang()
    assert kb._language == "EN"


def test_change_lang_en_to_ru():
    # Проверяем, что метод меняет язык на RU
    kb = KeyBoard('Dark', 9600, 5)
    kb._language = "EN"
    kb.change_lang()
    assert kb._language == "RU"


def test_read_from_csv_file_not_found():
    # Проверяем работу исключения с несуществующим файлом
    with pytest.raises(FileNotFoundError) as exc_info:
        Item.create_items_from_csv('nonexistent_file.csv')
    assert str(exc_info.value) == 'Отсутствует файл item.csv'


def test_read_from_csv_incomplete_file():
    # Проверяем работу исключения с неправильным файлом(меньше колонок)
    with open('test.csv', 'w') as csv_file:
        csv_file.write('name,price\n')  # incomplete file
    with pytest.raises(InstantiateCSVError) as exc_info:
        Item.create_items_from_csv('test.csv')
    assert str(exc_info.value) == 'Файл item.csv поврежден'
    # Удаляем временные файлы
    os.remove('test.csv')
