from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_page_loaded(self):
        self.wait.until(lambda driver: len(self.driver.find_elements_by_css_selector\
                                                ("ul li:nth-child(2) a[title='Коммунальные платежи']"))>0)
        self.wait.until(lambda driver : len(driver.find_elements_by_css_selector\
                                                ("div.ui-search-input__input-wrapper span:nth-last-child(1)"))>0)
    def wait_search_res_loaded(self):
        self.wait.until(lambda driver : len(driver.find_elements_by_css_selector\
                                                 ("div.ui-search-flat__title.ui-search-flat__title_alone div"))>0)

    @property
    def komunal_plat_link(self):
        return self.driver.find_element_by_css_selector("ul li:nth-child(2) a[title='Коммунальные платежи']:nth-child(2)")

    @property
    def quick_search_input(self):
        return self.driver.find_element_by_css_selector("div.ui-search-input__input-wrapper input.ui-search-input__input")

    @property
    def search_result_list(self):
        return self.driver.find_elements_by_css_selector("div.ui-search-flat__title.ui-search-flat__title_alone div")

