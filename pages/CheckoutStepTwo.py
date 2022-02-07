import allure
from pages.MainPage import MainPage


class CheckOutStepTwo(MainPage):
    """
    Первый этап подтверждения покупки.
    Предполагает ввод данных пользователя.
    """

    check_two_url = f'{MainPage.base_url}/checkout-step-two.html'

    def __init__(self, driver):
        super().__init__(driver)

        self.data = self.JH.open('check_two_page')

        find_id = self.find_id

        # локаторы
        self.finish_btn = find_id('finish')

    @allure.step('Нажать кнопку "Завершить"')
    def click_finish_btn(self):
        self.finish_btn().click()
        return self
