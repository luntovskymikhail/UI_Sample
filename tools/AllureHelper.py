import allure
from allure_commons.types import AttachmentType


class AllureHelper:
    """
    Класс для работы с системой отчетности Allure.
    """

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self):
        """
        Сделает скриншот и ничего больше.
        """
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="screenshot_failed_test",
                      attachment_type=AttachmentType.PNG)

    def compare(self,
                what: str,
                expected: str,
                actual: str,
                accuracy: bool = True):
        """
        Сверяет ожидаемый результат с фактическим.
        В случае несоответствия выбрасывает ассерт
        и делает скриншот.

        :param what: что сверяем (тайтл, ссылка, текст и.т.д.)
        :param expected: ожидаемый результат
        :param actual: фактический результат
        :param accuracy: необязательный, выключает точное совпадение
        """
        if accuracy:
            if expected != actual:
                with allure.step(f'Ожидаю увидеть точное совпадение {what}: {expected}'):
                    with allure.step(f'Вижу по факту: {actual}'):
                        self.screenshot()
                        assert False, 'Смотри покрасневший шаг ' \
                                      'со скриншотом во вложении'
        if not accuracy:
            if expected not in actual:
                with allure.step(f'Ожидаю увидеть частичное совпадение {what}: {expected}'):
                    with allure.step(f'Вижу по факту: {actual}'):
                        self.screenshot()
                        assert False, 'Смотри покрасневший шаг ' \
                                      'со скриншотом во вложении'

    def difference(self,
                   what: str,
                   element1: str,
                   element2: str,
                   accuracy=True):
        """
        Сверяет между собой два элемента.
        В случае совпадения выбрасывает ассерт
        и делает скриншот.

        :param what: что сверяем (тайтл, ссылка, текст и.т.д.)
        :param element1: первый элемент (наименьший текст)
        :param element2: второй элемент (наибольший текст)
        :param accuracy: необязательный, выключает точное совпадение
        """
        if accuracy:
            if element1 == element2:
                with allure.step(f'Ожидалось что {what} будет несоответствовать'):
                    with allure.step(f'Совпадающие значения: {element1}'):
                        self.screenshot()
                        assert False, 'Смотри покрасневший шаг ' \
                                      'со скриншотом во вложении'
        if not accuracy:
            if element1 in element2:
                with allure.step(f'Ожидалось что {what} будет несоответствовать'):
                    with allure.step(f'Совпадающие значения: {element1}'):
                        self.screenshot()
                        assert False, 'Смотри покрасневший шаг ' \
                                      'со скриншотом во вложении'
