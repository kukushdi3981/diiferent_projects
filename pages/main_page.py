from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    main_Url = "https://www.tinkoff.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.main_Url)
        return self

    @property
    def platezhi_menu_item(self):
        return self.driver.find_element_by_css_selector("nav div:nth-child(5) a")
