import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi_button = (By.CLASS_NAME, 'button.button.round')
    comfort_tariff_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_number_field_click = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')
    phone_number_field = (By.XPATH, '//*[@id="phone"]')
    next_button_in_phone_number = (By.CLASS_NAME, 'button.button.full')
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
        (WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable(self.from_field))
         .send_keys(from_address))

    def set_to(self, to_address):
        (WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable(self.to_field))
         .send_keys(to_address))

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.comfort_tariff_button)).click()

    def select_phone_number(self):
        self.driver.find_element(*self.phone_number_field_click).click()

    def fill_phone_number(self, phone_number):
        phone_number_input = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                                 (self.phone_number_field))
        phone_number_input.clear()  # Limpiar el campo de entrada
        phone_number_input.send_keys(phone_number)

    def select_code_sms(self, code_sms):
        self.driver.find_element(*self.code_sms_field).send_keys(code_sms)

    def add_credit_card(self, card_number, code_card):
        add_card_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                              (self.add_card_button))
        add_card_button.click()  # Clic para abrir el modal de agregar tarjeta
        card_number_input = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                                (self.card_number_field))
        card_number_input.send_keys(card_number)
        card_code_button = self.driver.find_element(*self.code_card_field)
        card_code_button.send_keys(code_card)

    def fill_conductor_message(self, conductor_message):
        conductor_message_input = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                                      (self.conductor_message_field))
        conductor_message_input.clear()  # Limpiar el campo de entrada
        conductor_message_input.send_keys(conductor_message)

    def request_blanket_and_tissues(self):
        blanket_and_tissues_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                                         (self.blanket_and_tissues_button))
        blanket_and_tissues_button.click()

    def request_ice_cream(self, quantity=2):
        for _ in range(quantity):
            ice_cream_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                                   (self.ice_cream_button))
            ice_cream_button.click()

    def request_taxi(self):
        taxi_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                          (self.order_a_taxi_button))
        taxi_button.click()

    def select_next_button(self):
        next_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                          (self.next_button_in_phone_number))
        next_button.click()

    def select_add_card_click(self):
        self.driver.find_element(*self.add_card_click).click()

    def select_confirm_button(self):
        confirm_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                             (self.confirm_button))
        confirm_button.click()

    def select_add_button(self):
        time.sleep(1)
        add_button = self.driver.find_element(*self.add_button_click)
        add_button.click()

    def select_x_button(self):
        x_button = WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                                       (self.x_button_click))
        x_button.click()
