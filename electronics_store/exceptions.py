class InstantiateCSVError(Exception):
    """
    Класс Исключение, возникающее при ошибке в методе instantiate_from_csv.
    """

    def __init__(self, *args):
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self):
        return self.message
