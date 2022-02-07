import allure
import pytest
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.CheckoutStepOne import CheckOutStepOne
from pages.CheckoutStepTwo import CheckOutStepTwo


@allure.epic('Второй этап проверки')
class TestStepTwoPage:

    url = MainPage.main_url

    @pytest.fixture(autouse=True)
    def get_step_two_page(self, driver):
        with allure.step(f'Перехожу по ссылке {self.url}'):
            driver.get(self.url)

    data = []

    @pytest.mark.parametrize(
        ('users'),
        (
                ('standard_user',
                 'problem_user',
                 'performance_glitch_user')
        )

    )
    def test_001(self, driver, users):

        LoginPage(driver) \
            .auth_users(users)

        MainPage(driver) \
            .add_backpack_to_cart() \
            .click_cart_btn()

        CartPage(driver) \
            .click_checkout_btn()

        CheckOutStepOne(driver) \
            .enter_data()

        CheckOutStepTwo(driver) \
            .click_finish_btn()
