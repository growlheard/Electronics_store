import csv

from electronics_store.exceptions import InstantiateCSVError


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
        try:
            with open(file_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                if 'name' not in reader.fieldnames or 'price' not in reader.fieldnames or 'quantity' not in reader.fieldnames:
                    raise InstantiateCSVError("Файл item.csv поврежден")
                for row in reader:
                    name = row['name']
                    price = int(float(row['price'])) if cls.is_integer(row['price']) else float(row['price'])
                    quantity = int(float(row['quantity'])) if cls.is_integer(row['price']) else float(row['quantity'])
                    item = cls(name, price, quantity)
                    cls.items_list.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")



class Phone(Item):
    """
        Класс Phone наследуемый от класса Ithem
        """

    def __init__(self, name, price, quantity, sim_card):
        super().__init__(name, price, quantity)
        self.sim_card = sim_card

    def __repr__(self):
        return f"{super().__repr__()},{self.sim_card}"

    @property
    def sim_card(self) -> int:
        """Возвращаем кол-во сим-карт"""
        return self.__sim_card

    @sim_card.setter
    def sim_card(self, sim_card: int):
        """
        Обновляет количество сим-карт и выбрасывает исключение
        """
        if sim_card > 0:
            self.__sim_card = sim_card
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        else:
            raise ValueError("Эти данные сложению не подлежат")


class MixinLog:
    """
    Доп функционал класса KeyBoard
     """
    def __init__(self, *args):
        self._language = "EN"
        super().__init__(*args)

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """
        Метод для изменения языка
        """
        if self._language == "RU":
            self._language = "EN"
        else:
            self._language = "RU"


class KeyBoard(MixinLog, Item):
    """
    класс KeyBoard который наследуется от MixinLog и Ithem
    """
    pass
