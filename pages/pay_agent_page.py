from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentAgentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @property
    def oplata_tab_link(self):
        return self.driver.find_element_by_css_selector("div.ui-menu-second__items a[title='Оплатить']")

    def wait_page_loaded(self):
        self.wait.until(lambda driver: self.driver.find_element_by_css_selector("div div.ui-menu-second__items"))


