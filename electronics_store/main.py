class Item:
    # атрибуты класса
    pay_rate = 1  # уровень цен по умолчанию
    all = []  # список созданных экземпляров класса

    def __init__(self, name, price, quantity):
        # атрибуты экземпляра класса
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)  # добавляем экземпляр в список созданных объектов

    def calculate_total_price(self):
        return self.price * self.quantity  # общая стоимость товара в магазине

    def apply_discount(self):
        self.price *= self.pay_rate  # применяем скидку к цене товара



