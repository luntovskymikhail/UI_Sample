import allure
from pages.MainPage import MainPage


class CartPage(MainPage):
    """
    Корзина для товаров.
    """

    cart_url = f'{MainPage.base_url}/cart.html'

    def __init__(self, driver):
        super().__init__(driver)

        self.data = self.JH.open('cart_page')

        xpath = self.xpath

        # локаторы
        self.checkout_btn = xpath('//button[@data-test="checkout"]')

    @allure.step('Кликнуть по кнопке "Проверка"')
    def click_checkout_btn(self):
        self.checkout_btn().click()
        return self
