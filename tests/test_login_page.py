import allure
import pytest
from pages.LoginPage import LoginPage


@allure.epic('Страница авторизации')
class TestLoginPage:

    url = LoginPage.main_url

    @pytest.fixture(autouse=True)
    def get_login_page(self, driver):
        with allure.step(f'Перехожу по ссылке {self.url}'):
            driver.get(self.url)

    @allure.story('Авторизоваться как заблокированный пользователь')
    def test_auth_blocked_user(self, driver):
        LoginPage(driver) \
            .auth_users('locked_out_user') \
            .check_locked_msg()
