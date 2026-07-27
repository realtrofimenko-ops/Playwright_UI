from playwright.sync_api import Page


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
        self.page.locator(locator).wait_for(state="visible")

    def make_screenshot_and_attach_to_allure(self):
        self.page.screenshot(path="screenshot.png", full_page=True)