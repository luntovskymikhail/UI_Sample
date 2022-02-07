import allure
from tools.AllureHelper import AllureHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumHelper:
    """
    Класс для упрощенной работы с селениумом.
    """

    def __init__(self, driver):
        self.driver = driver
        self.screenshot = AllureHelper(driver).screenshot

    def scroll(self, height='to_middle'):
        """
        Скроллит страницу на определенную высоту.
        Что бы в случае ассерта было видно что на ней происходило.

        to_middle - на середину страницы (по умолчанию) \n
        to_end - в конец страницы \n
        to_top - на верх страницы

        Если передано число - скроллит на заданное количство пикселей

        :param height: строка или целое число
        """

        size = self.driver.get_window_size()['width']
        step_text = f'Скролю страничку на значение: {height} пикселей'
        scroll = self.driver.execute_script

        with allure.step(step_text):
            try:
                if height == 'to_top':
                    scroll('window.scrollTo(0, 0)')
                elif height == 'to_middle':
                    scroll(f'window.scrollTo(0, {int(size) / 2})')
                elif height == 'to_end':
                    scroll('window.scrollTo(0, document.body.scrollHeight);')
                elif isinstance(size, int):
                    scroll(f'window.scrollTo(0, {int(height)})')
            except ValueError:
                assert False, 'в метод scroll_down передан не правильный ' \
                              'агрумент, скорее всего опечатка, текстом я ' \
                              'принимаю только "to_middle" и "to_end"'

    def wait_hide(self,
                  element,
                  seconds: int = 5):
        """
        Явное ожидание, ждет пока элемент не пропадет с экрана

        :param element: какой элемент ждем
        :param seconds: сколько ждем (по умолчанию 15 секунд)
        """

        step_text = f'Жду пока пропадет "{element.text}", ' \
                    f'но не дольше {seconds} секунд '

        error_text = f'Я ждал пока элемент "{element.text}" пропадет с ' \
                     f'экрана на протяжении {seconds} секунд, но так и не ' \
                     f'дождался, смотри скришнот во вложении '

        with allure.step(step_text):
            try:
                WebDriverWait(self.driver, seconds) \
                    .until(EC.invisibility_of_element_located(element))
            except TimeoutException:
                self.screenshot()
                assert False, error_text

    def wait_appear(self,
                    element,
                    seconds: int = 5):
        """
        Явное ожидание, ждет пока элемент появится на экране

        :param element: какой элемент ждем
        :param seconds: сколько ждем (по умолчанию 15 секунд)
        """

        step_text = f'Жду пока появится "{element.text}", ' \
                    f'но не дольше {seconds} секунд '

        error_text = f'Я ждал пока элемент "{element.text}" появится на ' \
                     f'экране на протяжении {seconds} секунд, но так и не ' \
                     f'дождался, смотри скришнот во вложении '

        with allure.step(step_text):
            try:
                WebDriverWait(self.driver, seconds) \
                    .until(EC.visibility_of(element))
            except TimeoutException:
                self.screenshot()
                assert False, error_text

    def switch_window(self, window: int):
        """
        Переключается на определенную вкладку в случае если открыто несколько.

        :param window: целое число, номер вкладки.
        """
        with allure.step(f'Переключаюсь на окно {window}'):
            self.driver.switch_to.window(self.driver.window_handles[window])

    def hover_on(self, element):
        """
        Имитирует наведение курсора на элемент.

        :param element: элемент на который необходимо навести курсор.
        """
        with allure.step(f'Навожу курсор на {element}'):
            ActionChains(self.driver).move_to_element(element).perform()
