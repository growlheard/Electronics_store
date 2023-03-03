import csv


class Item:
    pay_rate = 1
    all = []
    items_list = []

    def __init__(self, name, price, quantity):
        """
        Атрибуты экземпляра класса
        :param name:
        :param price:
        :param quantity:
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        """
        Возвращает наименование товара
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Обновляет наименование товара и выбрасывает исключение
        """
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = name

    def calculate_total_price(self):
        """
        Общая стоимость товара в магазине
        :return:
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяем скидку к цене товара
        :return:
        """
        self.price *= self.pay_rate

    @staticmethod
    def is_integer(num):
        """
        Проверка на целое число
        :param num:
        :return:
        """
        return float(num).is_integer()

    @classmethod
    def create_items_from_csv(cls, file_path: str):
        """
        Считывает данные из csv файла и создает экземпляры класса
        """
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name = row['name']
                price = int(float(row['price'])) if cls.is_integer(row['price']) else float(row['price'])
                quantity = int(float(row['quantity'])) if cls.is_integer(row['price']) else float(row['quantity'])
                item = cls(name, price, quantity)
                cls.items_list.append(item)




