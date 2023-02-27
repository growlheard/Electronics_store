from electronics_store import __version__
from electronics_store.main import Item


def test_version():
    assert __version__ == '0.1.0'


# тестируем метод calculate_total_price
def test_calculate_total_price():
    # создаем экземпляр класса Item
    item = Item("Телефон", 100, 2)
    # проверяем, что общая стоимость товара правильно рассчитывается
    assert item.calculate_total_price() == 200
    assert item.calculate_total_price()


# тестируем метод apply_discount
def test_apply_discount():
    # создаем экземпляр класса Item
    item = Item("Телефон", 100, 2)
    # применяем скидку
    item.apply_discount()
    # проверяем, что цена товара изменилась с учетом скидки
    assert item.price == 100 * item.pay_rate



