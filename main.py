import time
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación."
                            )
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_tariff_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    phone_number_field_click = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    phone_number_field = (By.XPATH, '//*[@id="phone"]')
    next_button_in_phone_number = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    code_sms_field = (By.ID, 'code')
    add_card_click = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    # Selector del botón para agregar tarjeta de crédito
    card_number_field = (By.XPATH, '//*[@id="number"]')  # Selector del campo de entrada del número de tarjeta
    code_card_field = (By.CSS_SELECTOR, "input[placeholder='12']")
    add_button_click = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    x_button_click = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    conductor_message_field = (By.XPATH, '//*[@id="comment"]')
    blanket_and_tissues_button = (By.XPATH,
                                  '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]')
    ice_cream_button = (By.XPATH,
                        '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_address, to):
        self.set_from(from_address)
        self.set_to(to)

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff_button).click()

    def select_phone_number(self):
        self.driver.find_element(*self.phone_number_field_click).click()

    def fill_phone_number(self, phone_number):
        phone_number_input = self.driver.find_element(*self.phone_number_field)
        phone_number_input.clear()  # Limpiar el campo de entrada
        phone_number_input.send_keys(phone_number)

    def select_code_sms(self, code_sms):
        code_sms_input = self.driver.find_element(*self.code_sms_field)
        code_sms_input.clear()  # Limpiar el campo de entrada
        code_sms_input.send_keys(code_sms)

    def add_credit_card(self, card_number, code_card):
        add_card_button = self.driver.find_element(*self.add_card_button)
        add_card_button.click()  # Clic para abrir el modal de agregar tarjeta
        time.sleep(1)
        card_number_input = self.driver.find_element(*self.card_number_field)
        card_number_input.send_keys(card_number)
        time.sleep(1)
        card_code_button = self.driver.find_element(*self.code_card_field)
        card_code_button.send_keys(code_card)

    def fill_conductor_message(self, conductor_message):
        conductor_message_input = self.driver.find_element(*self.conductor_message_field)
        conductor_message_input.clear()  # Limpiar el campo de entrada
        conductor_message_input.send_keys(conductor_message)

    def request_blanket_and_tissues(self):
        blanket_and_tissues_button = self.driver.find_element(*self.blanket_and_tissues_button)
        blanket_and_tissues_button.click()

    def request_ice_cream(self, quantity=2):
        for _ in range(quantity):
            ice_cream_button = self.driver.find_element(*self.ice_cream_button)
            ice_cream_button.click()

    def request_taxi(self):
        taxi_button = self.driver.find_element(*self.order_a_taxi_button)
        taxi_button.click()

    def select_next_button(self):
        next_button = self.driver.find_element(*self.next_button_in_phone_number)
        next_button.click()

    def select_add_card_click(self):
        add_card_click = self.driver.find_element(*self.add_card_click)
        add_card_click.click()

    def select_confirm_button(self):
        confirm_button = self.driver.find_element(*self.confirm_button)
        confirm_button.click()

    def select_add_button(self):
        add_button = self.driver.find_element(*self.add_button_click)
        add_button.click()

    def select_x_button(self):
        x_button = self.driver.find_element(*self.x_button_click)
        x_button.click()


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
        time.sleep(1)
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(1)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        time.sleep(1)
        routes_page.request_taxi()
        time.sleep(1)
        routes_page.select_comfort_tariff()
        time.sleep(1)
        routes_page.select_phone_number()
        phone_number = "+1 123 123 12 12"  # Número de teléfono a rellenar
        routes_page.fill_phone_number(phone_number)
        routes_page.select_next_button()
        time.sleep(1)
        code_sms = retrieve_phone_code(driver=self.driver)
        routes_page.select_code_sms(code_sms)
        routes_page.select_confirm_button()
        time.sleep(1)
        routes_page.select_add_card_click()
        card_number = "1234 5678 9100"  # Número de tarjeta de ejemplo
        code_card = "111"
        routes_page.add_credit_card(card_number, code_card)
        routes_page.select_add_button()
        time.sleep(1)
        routes_page.select_x_button()
        conductor_message = "Muéstrame el camino al museo"
        routes_page.fill_conductor_message(conductor_message)
        # Solicitar una manta y un panuelo
        routes_page.request_blanket_and_tissues()
        # Solicitar 2 helados
        routes_page.request_ice_cream(quantity=2)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
