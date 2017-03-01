from selenium import webdriver

from pages.main_page import MainPage
from pages.payments_page import PaymentsPage
from pages.komunalplatezhi_page import KomunalPlateziPage
from pages.pay_agent_page import PaymentAgentPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.payments_page = PaymentsPage(self.driver)
        self.komunalplatezhi_page = KomunalPlateziPage(self.driver)
        self.payagent_page = PaymentAgentPage(self.driver)

    def quit(self):
        self.driver.quit()

    def get_current_region_name(self):
        return self.komunalplatezhi_page.region_pay_link.get_attribute("textContent")

    def get_target_provider(self):
        self.komunalplatezhi_page.wait_pay_agents_list_loaded()
        return self.komunalplatezhi_page.pay_agent_link.get_attribute("textContent")

    def select_platezhi_menu_item(self):
        self.main_page.open()
        self.main_page.platezhi_menu_item.click()

    def select_komunal_platez_type(self):
        self.payments_page.wait_page_loaded()
        self.payments_page.komunal_plat_link.click()

    def get_target_reg_element(self, target_region):
        reg_list = self.komunalplatezhi_page.regions_link_list

        for element in reg_list:
            text = element.get_attribute("textContent")
            if text == target_region:
                return element

        return None


    def check_and_select_region(self, targ_region, choose_region):
        self.komunalplatezhi_page.wait_page_loaded()
        self.komunalplatezhi_page.wait_pay_agents_list_loaded()
        region = self.get_current_region_name()
        if region != targ_region:
            self.komunalplatezhi_page.region_pay_link.click()
            self.komunalplatezhi_page.wait_regions_list_loaded()
            targ_elem = self.get_target_reg_element(choose_region)
            if targ_elem is not None:
                targ_elem.click()

            self.komunalplatezhi_page.wait_pay_agents_list_loaded()

        region = self.get_current_region_name()
#        assert region == targ_region

    def select_pay_provider(self):
        self.komunalplatezhi_page.pay_agent_link.click()

    def go_to_pay_tab(self):
        self.payagent_page.wait_page_loaded()
        self.payagent_page.oplata_tab_link.click()

    def go_to_payment_menu_item(self):
       self.main_page.platezhi_menu_item.click()

    def search_pay_provider(self, targ_provider):
        self.payments_page.wait_page_loaded()
        self.payments_page.quick_search_input.send_keys(targ_provider)

    def get_first_provider_in_search_res(self):
        self.payments_page.wait_search_res_loaded()
        return self.payments_page.search_result_list[0].get_attribute("textContent")

    def check_provider_in_list(self, targ_provider):
        provider_list = self.komunalplatezhi_page.provider_link_list

        for element in provider_list:
            text = element.get_attribute("textContent")
            if text == targ_provider:
                return element

        return None
