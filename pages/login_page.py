from pages.base_page import BasePage


class CinescopeLoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.url = "https://dev-cinescope.coconutqa.ru/login"

        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.login_button = "[data-qa-id='login_submit_button']"

    def open(self):
        self.open_url(self.url)

    def login(self, email, password):

        self.enter_text_to_element(
            self.email_input,
            email
        )

        self.enter_text_to_element(
            self.password_input,
            password
        )

        with self.page.expect_response(
            lambda r: "/login" in r.url and r.request.method == "POST"
        ) as response_info:

            self.click_element(self.login_button)

        response = response_info.value

        assert response.ok, (
            f"Логин не выполнился. "
            f"Status={response.status}, "
            f"Body={response.text()}"
        )