import allure
from pages.MainPage import MainPage


class LoginPage(MainPage):
    """
    Страница авторизации на сайте.
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.data = self.JH.open('login_page')

        cls = self.class_name
        find_id = self.find_id

        # локаторы
        self.username_fld = find_id('user-name')
        self.password_fld = find_id('password')
        self.login_btn = find_id('login-button')
        self.error_msg = cls('error-message-container', text=True)

    def auth_users(self, users):
        with allure.step(f'Авторизовываюсь как {users}'):
            self.username_fld().send_keys(users)
            self.password_fld().send_keys('secret_sauce')
            self.login_btn().click()
        return self

    @allure.step('Проверить сообщение о заблокированном пользователе')
    def check_locked_msg(self):
        self.compare(what='сообщения о блокировке',
                     expected=self.data['locked_msg'],
                     actual=self.error_msg())
        return self
