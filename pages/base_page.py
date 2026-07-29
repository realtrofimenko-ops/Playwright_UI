import allure
from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url)

    def enter_text_to_element(self, locator, text):
        self.page.fill(locator, text)

    def click_element(self, locator):
        self.page.click(locator)

    def wait_for_element(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def make_screenshot_and_attach_to_allure(self):
        screenshot = self.page.screenshot(full_page=True)

        allure.attach(
            screenshot,
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG
        )