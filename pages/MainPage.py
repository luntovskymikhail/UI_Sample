import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    """
    Страница открывающаяся после авторизации.
    """

    main_url = f'{BasePage.base_url}/inverntoty.html'

    def __init__(self, driver):
        super().__init__(driver)

        self.data = self.JH.open('main_page')

        css = self.css
        cls = self.class_name
        name = self.name

        # локаторы
        self.cart_btn = css('div[class="shopping_cart_container"]')
        self.cart_badge = cls('shopping_cart_badge', text=True)
        self.add_backpack_btn = name('add-to-cart-sauce-labs-backpack')
        self.remove_backpack_btn = name('remove-sauce-labs-backpack')
        self.back_to_products_btn = name('back-to-products')
        self.items_descriptons = cls('inventory_item_label', many=True)
        self.add_to_cart_btns = css('button[class="btn btn_primary btn_small btn_inventory"]', many=True)

    @allure.step('Проверить что мы на главной странице')
    def check_main_page(self):
        self.compare(what='ссылки',
                     expected=self.main_url,
                     actual=self.driver.current_url)

    @allure.step('Сверить описания для товаров на главной')
    def check_items_descriptios(self):
        expected_descriptions = list(self.data['items'].values())
        site_descriptions = str([i.text for i in self.items_descriptons()])

        for item_description in expected_descriptions:
            self.compare(what='описания предмета на сайте',
                         expected=item_description,
                         actual=site_descriptions,
                         accuracy=False)
        return self

    @allure.step('Прокликать ссылки социальных сетей')
    def click_social_networks(self):
        network_urls = list(self.data['social_urls'].values())
        network_btn = lambda text: self.driver.find_element \
            (By.CSS_SELECTOR, f'a[href="{text}"]')
        for network_url in network_urls:
            network_btn(network_url).click()
            self.switch_window(1)
            self.compare(what='ссылки',
                         expected=network_url,
                         actual=self.driver.current_url)
            self.driver.close()
            self.switch_window(0)
        return self

    @allure.step('Кликнуть по кнопке "Перейти в корзину"')
    def click_cart_btn(self):
        self.cart_btn().click()
        return self

    @allure.step('Добавить товар в корзину')
    def _add_item_to_cart(self, item_button):
        start_count = len(self.add_to_cart_btns())
        item_button.click()
        end_count = len(self.add_to_cart_btns())
        self.difference(what='количество кнопок добавить',
                        element1=start_count,
                        element2=end_count)
        self.compare(what='цифры на корзине',
                     expected=1,
                     actual=int(self.cart_badge()))
        return self

    @allure.step('Добавить рюкзак в корзину')
    def add_backpack_to_cart(self):
        self._add_item_to_cart(self.add_backpack_btn())
        return self
