
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi_button = (By.CLASS_NAME, 'button.button.round')
    comfort_tariff_button = (By.XPATH, "//div[text()='Comfort']")
    phone_number_field_click = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.XPATH, '//*[@id="phone"]')
    next_button_in_phone_number = (By.CLASS_NAME, 'button.button.full')
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    code_sms_field = (By.ID, 'code')
    add_card_click = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, "//div[@class='pp-row disabled']//div[text()='Agregar tarjeta']")
    # Selector del botón para agregar tarjeta de crédito
    card_number_field = (By.ID, 'number')  # Selector del campo de entrada del número de tarjeta
    code_card_field = (By.CSS_SELECTOR, "input[placeholder='12']")
    add_button_click = (By.XPATH, "//button[text()='Agregar']")
    x_button_click = (By.XPATH, "//div[@class='payment-picker open']//div[@class='modal']//div[@class='section "
                                "active']//button[@class='close-button section-close']")
    conductor_message_field = (By.ID, 'comment')
    blanket_and_tissues_checkbox = (By.XPATH,
                                    '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div['
                                    '2]/div/span')
    counter_value_field = (By.CLASS_NAME, 'counter-value')
    reserve_button = (By.XPATH, "//span[@class='smart-button-secondary']")
    plus_button = (By.CLASS_NAME, 'counter-plus')
    modal_title = (By.CLASS_NAME, 'order-header-title')
    details_button = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]/button')
    direction_text = (By.CLASS_NAME, 'o-d-h')

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
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.phone_number_field))
        phone_number_input = self.driver.find_element(*self.phone_number_field)
        phone_number_input.clear()  # Limpiar el campo de entrada
        phone_number_input.send_keys(phone_number)

    def select_code_sms(self, code_sms):
        self.driver.find_element(*self.code_sms_field).send_keys(code_sms)

    def add_credit_card(self, card_number, code_card):
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.add_card_button))
        add_card_button = self.driver.find_element(*self.add_card_button)
        add_card_button.click()  # Clic para abrir el modal de agregar tarjeta
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.card_number_field))
        card_number_input = self.driver.find_element(*self.card_number_field)
        card_number_input.send_keys(card_number)
        card_code_button = self.driver.find_element(*self.code_card_field)
        card_code_button.send_keys(code_card)

    def fill_conductor_message(self, conductor_message):
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.conductor_message_field))
        conductor_message_input = self.driver.find_element(*self.conductor_message_field)
        conductor_message_input.clear()  # Limpiar el campo de entrada
        conductor_message_input.send_keys(conductor_message)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_checkbox).click()

    def request_ice_cream(self, quantity=2):
        for _ in range(quantity):
            ice_cream_button = self.driver.find_element(*self.plus_button)
            ice_cream_button.click()

    def request_taxi(self):
        self.driver.find_element(*self.order_a_taxi_button).click()

    def select_next_button(self):
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.next_button_in_phone_number))
        next_button = self.driver.find_element(*self.next_button_in_phone_number)
        next_button.click()

    def select_add_card_click(self):
        self.driver.find_element(*self.add_card_click).click()

    def select_confirm_button(self):
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable(self.confirm_button))
        confirm_button = self.driver.find_element(*self.confirm_button)
        confirm_button.click()

    def select_add_button(self):
        add_button = self.driver.find_element(*self.add_button_click)
        add_button.click()

    def select_x_button(self):
        WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable
                                            (self.x_button_click))
        x_button = self.driver.find_element(*self.x_button_click)
        x_button.click()

    def reserve_taxi_button(self):
        reserve_button = self.driver.find_element(*self.reserve_button)
        reserve_button.click()

    def find_ice_cream_element(self):
        ice_cream_element = self.driver.find_element(*self.counter_value_field)
        return ice_cream_element

    def find_modal_title(self):
        modal_title = self.driver.find_element(*self.modal_title)
        return modal_title

    def details_button_(self):
        WebDriverWait(self.driver, 35).until(expected_conditions.element_to_be_clickable(self.details_button))
        details_button = self.driver.find_element(*self.details_button)
        details_button.click()

    def card_text(self):
        card_text = self.driver.find_element(*self.direction_text)
        return card_text
