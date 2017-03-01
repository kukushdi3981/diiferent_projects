import pytest
from app.application import Application

def test_work_with_cart(app = Application()):
    app.select_platezhi_menu_item()
    app.select_komunal_platez_type()
    app.check_and_select_region(" Москве", "г. Москва")
    provider_name = app.get_target_provider()
    app.select_pay_provider()
    app.go_to_pay_tab()

    #часть2
    app.go_to_payment_menu_item()
    app.search_pay_provider(provider_name)
    cur_provider = app.get_first_provider_in_search_res()
    assert cur_provider == provider_name

    #часть3
    app.go_to_payment_menu_item()
    app.select_komunal_platez_type()
    app.check_and_select_region(" Санкт-Петербурге", "г. Санкт-Петербург")
    result = app.check_provider_in_list(provider_name)
    assert result is None
    app.quit()
