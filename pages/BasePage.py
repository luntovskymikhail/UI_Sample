from tools.AllureHelper import AllureHelper
from tools.JsonHelper import JsonHelper as JH
from tools.LocatorHelper import LocatorHelper
from tools.RandomData import RandomData
from tools.SeleniumHelper import SeleniumHelper
from time import sleep as wait


class BasePage:

    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver

        self.JH = JH('./resources/all_data.json')

        # упрощаем внешний вид локаторов
        locator = LocatorHelper(driver)
        self.css = locator.css
        self.xpath = locator.xpath
        self.find_id = locator.find_id
        self.name = locator.name
        self.tag = locator.tag
        self.class_name = locator.class_name
        self.link = locator.link

        # работаем с системой отчетности Allure
        allure_helper = AllureHelper(driver)
        self.compare = allure_helper.compare
        self.difference = allure_helper.difference

        # упрощаем работу с селениумом
        selenium = SeleniumHelper(driver)
        self.scroll = selenium.scroll
        self.switch_window = selenium.switch_window
        self.hover_on = selenium.hover_on
        self.wait_appear = selenium.wait_appear
        self.wait_hide = selenium.wait_hide

        # генерируем рандомные данные
        self.random = RandomData

        self.wait = wait
