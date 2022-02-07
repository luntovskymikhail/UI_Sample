import allure
from pages.MainPage import MainPage


class CheckOutStepOne(MainPage):
    """
    Первый этап подтверждения покупки.
    Предполагает ввод данных пользователя.
    """

    check_one_url = f'{MainPage.base_url}/checkout-step-one.html'

    def __init__(self, driver):
        super().__init__(driver)

        self.data = self.JH.open('check_one_page')

        name = self.name

        # локаторы
        self.first_name_fld = name('firstName')
        self.last_name_fld = name('lastName')
        self.zip_code_fld = name('postalCode')
        self.continue_btn = name('continue')

    @allure.step('Ввести данные пользователя')
    def enter_data(self):
        first_name = self.random.first_name()
        last_name = self.random.last_name()
        zip_code = self.random.zip()
        self.first_name_fld().send_keys(first_name)
        self.last_name_fld().send_keys(last_name)
        self.zip_code_fld().send_keys(zip_code)
        self.continue_btn().click()
        return self
