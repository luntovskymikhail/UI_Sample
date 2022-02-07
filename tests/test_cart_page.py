import allure
import pytest
from pages.MainPage import MainPage


@allure.epic('Корзина покупателя')
class TestCartPage:

    url = MainPage.main_url

    @pytest.fixture(autouse=True)
    def get_main_page(self, driver):
        with allure.step(f'Перехожу по ссылке {self.url}'):
            driver.get(self.url)
