from random import randint
from mimesis import Address, Person


class RandomData:

    @staticmethod
    def zip():
        return randint(10_000, 99_999)

    @staticmethod
    def first_name():
        return Person(locale='en').name()

    @staticmethod
    def last_name():
        return Person(locale='en').last_name()
