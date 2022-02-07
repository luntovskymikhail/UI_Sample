import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage


@pytest.fixture()
def driver():

    d = webdriver.Chrome('./driver/chromedriver.exe')
    d.maximize_window()
    d.implicitly_wait(5)
    yield d
    d.quit()


@pytest.fixture()
def auth_user(driver):
    LoginPage(driver).auth_users('standard_user')
