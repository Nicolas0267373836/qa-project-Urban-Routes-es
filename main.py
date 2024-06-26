import data
from selenium import webdriver
from helpers import retrieve_phone_code
from UrbanRoutesPage import UrbanRoutesPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación
        # del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert routes_page.select_comfort_tariff

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_phone_number()
        phone_number = "+1 123 123 12 12"  # Número de teléfono a rellenar
        routes_page.fill_phone_number(phone_number)
        assert routes_page.driver.find_element(*routes_page.phone_number_field).get_attribute('value') == phone_number

    def test_code_sms(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_next_button()
        code_sms = retrieve_phone_code(driver=self.driver)
        routes_page.select_code_sms(code_sms)
        assert routes_page.driver.find_element(*routes_page.code_sms_field).get_attribute('value') == code_sms

    def test_select_confirm_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_confirm_button()
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (routes_page.add_card_click))

    def test_select_add_card_click(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_add_card_click()
        assert routes_page.driver.find_element(*routes_page.card_number_field)

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = "1234 5678 9100"  # Número de tarjeta de ejemplo
        code_card = "111"
        routes_page.add_credit_card(card_number, code_card)
        assert routes_page.driver.find_element(*routes_page.card_number_field).get_attribute('value') == card_number

    def test_select_add_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_add_button()
        assert routes_page.driver.find_element(*routes_page.x_button_click)

    def test_select_x_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_x_button()
        assert routes_page.driver.find_element(*routes_page.conductor_message_field)

    def test_confirm_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number_confirmation = routes_page.get_phone_number_confirmation()
        assert phone_number_confirmation == "+1 123 123 12 12"

    def test_confirm_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        payment_method_confirmation = routes_page.get_payment_method_confirmation()
        assert payment_method_confirmation == "Tarjeta"

    def test_fill_conductor_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        conductor_message = "Muéstrame el museo"
        routes_page.fill_conductor_message(conductor_message)
        assert routes_page.driver.find_element(*routes_page.conductor_message_field).get_attribute(
            'value') == conductor_message

    def test_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket_and_tissues()
        assert routes_page.blanket_and_tissues_checkbox

    def test_request_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream(quantity=2)
        counter_value_element = routes_page.find_ice_cream_element()
        assert counter_value_element.text == '2'

    def test_reserve_taxi_click(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.reserve_taxi_button()
        modal_title_element = routes_page.find_modal_title()
        assert modal_title_element.text == 'Buscar automóvil'

    def test_modal_card_text(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.details_button_()
        modal_title_element = routes_page.card_text()
        assert modal_title_element.text == 'East 2nd Street, 601'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
