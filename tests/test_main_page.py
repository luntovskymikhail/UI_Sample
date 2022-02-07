import allure
import pytest
from pages.MainPage import MainPage


@allure.epic('Главная страница')
class TestMainPage:

    url = MainPage.main_url

    @pytest.fixture(autouse=True)
    def get_main_page(self, driver):
        with allure.step(f'Перехожу по ссылке {self.url}'):
            driver.get(self.url)

    @allure.story('Проверить наличие всех товаров на главной')
    def test_items_descriptions(self,
                                driver,
                                auth_user):
        MainPage(driver) \
            .check_items_descriptios()

    @allure.story('Проверить ссылки на социальные сети')
    def test_social_networks(self,
                             driver,
                             auth_user):
        MainPage(driver) \
            .click_social_networks()

    @allure.story('Добавить рюкзак в корзину')
    def test_add_to_cart(self,
                         driver,
                         auth_user):
        MainPage(driver) \
            .add_backpack_to_cart()
