import json


class JsonHelper:
    """
    Модуль для работы с джейсон файлами.
    Умеет открывать (open) и записывать (write).
    При инициализации обязателен путь в виде строки.
    """

    def __init__(self, path: str):
        self.path = path

    def open(self, *args):
        """
        Открывает джейсон файл.

        :param args: Использовать этот параметр только при чтении данных.
        Если в него передать строку в кавычках (ключ), откроет только
        данные по полученному значению ключа.
        """
        with open(f'{self.path}', encoding='utf-8') as f:
            args_str = ''.join(args)
            return json.load(f)[args_str] if args else json.load(f)

    def write(self, data: dict):
        """
        Записывает данные в джейсон файл.

        :param data: данные которые записываем, словарь обязателен.
        """
        with open(f'{self.path}', 'w', encoding='utf-8') as w:
            w.write(json.dumps(data, indent=2, ensure_ascii=False))
