from random import randint

from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.url = "https://dev-cinescope.coconutqa.ru/register"

        self.fullname = "[data-qa-id='register_full_name_input']"
        self.email = "[data-qa-id='register_email_input']"
        self.password = "[data-qa-id='register_password_input']"
        self.repeat_password = "[data-qa-id='register_password_repeat_input']"
        self.submit = "[data-qa-id='register_submit_button']"

    def open(self):
        self.open_url(self.url)

    def register(self):
        email = f"ivan{randint(100000, 999999)}@mail.com"
        password = "Asdqwe123Q"

        self.enter_text_to_element(
            self.fullname,
            "Ivan Test"
        )

        self.enter_text_to_element(
            self.email,
            email
        )

        self.enter_text_to_element(
            self.password,
            password
        )

        self.enter_text_to_element(
            self.repeat_password,
            password
        )

        self.click_element(self.submit)

        self.page.wait_for_url("**/login")

        return email, password