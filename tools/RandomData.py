import requests
from random import randint
from mimesis import Address, Person


class RandomData:

    @staticmethod
    def generate_text(length: str = 'default') -> str:
        """
        Создает рандомный текст на кириллице. \n
        Почитать доку можно тут: https://fish-text.ru/api

        :param length: short, default, long, quote
        """

        fish_text_url = 'https://fish-text.ru/get'

        regular_lorem = \
            requests.get(url=fish_text_url,
                         params={"format": "html",
                                 "type": "sentence",
                                 "number": "1"})
        big_lorem = \
            requests.get(url=fish_text_url,
                         params={"format": "html",
                                 "type": "paragraph",
                                 "number": "15"})

        quote_lorem = \
            requests.get(url=fish_text_url,
                         params={"format": "html",
                                 "type": "title",
                                 "number": "1"})

        error_msg = 'В функцию generate_text передан неизвестный ' \
                    'параметр, скорее всего опечатка в слове '

        if length == 'default':
            text = regular_lorem.text[3:-4]  # срез убирает тэги
        elif length == 'short':
            text = regular_lorem.text[3:5]  # 2 символа без тэга
        elif length == 'middle':
            text = big_lorem.text[3:259]  # 256 символов
        elif length == 'long':
            text = ''
            while len(text) <= 4096:
                text = big_lorem.text[3:-4]  # гарантирует больше 4096
        elif length == 'quote':
            text = quote_lorem.text[4:-5]  # срез убирает тэги
        else:
            raise TypeError(error_msg)

        return text.replace('  ', ' ')

    @staticmethod
    def zip():
        return randint(10_000, 99_999)

    @staticmethod
    def first_name():
        return Person(locale='en').name()

    @staticmethod
    def last_name():
        return Person(locale='en').last_name()
