from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KomunalPlateziPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def region_pay_link(self):
        return self.driver.find_element_by_css_selector("h1 span.ui-link.payment-page__title_inner")

    @property
    def regions_link_list(self):
        return self.driver.find_elements_by_css_selector("div.ui-scroll.ui-regions__layout div.ui-regions__item span")

    @property
    def pay_agent_link(self):
        return self.driver.find_element_by_css_selector("ul li a[title='ЖКУ-Москва']:nth-child(2)")

    @property
    def provider_link_list(self):
        return self.driver.find_elements_by_css_selector("div.ui-layout__page-component ul li")

    def wait_page_loaded(self):
        self.wait.until(lambda driver : self.driver.\
                                       find_element_by_css_selector("h1 span.ui-link.payment-page__title_inner"))
        self.wait.until(lambda driver : len(self.driver.\
                                       find_elements_by_css_selector("div.ui-layout__page-component ul li"))>0)

    def wait_regions_list_loaded(self):
        self.wait.until(lambda driver : len(self.driver.find_elements_by_css_selector\
            ("div.ui-scroll.ui-regions__layout div.ui-regions__item"))>0)

    def wait_pay_agents_list_loaded(self):
        self.wait.until(lambda driver : len(self.driver.\
                                       find_elements_by_css_selector("div.ui-layout__page-component ul li"))>0)
