from playwright.sync_api import expect

from config import BASE_URL
from pages.base_page import BasePage


class MoviePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.movies_url = f"{BASE_URL}/movies"

        self.more_buttons = "[data-qa-id='more_button']"

        self.review_input = "[data-qa-id='movie_review_input']"

        self.rating_button = "form button[role='combobox']"

        self.send_button = "[data-qa-id='movie_review_submit_button']"

    def open_movies(self):
        self.open_url(self.movies_url)

    def open_first_movie(self):

        self.open_movies()

        self.page.locator(self.more_buttons).first.click()

        expect(
            self.page.locator(self.review_input)
        ).to_be_visible()

    def add_review(self, text, rating):

        expect(
            self.page.locator(self.review_input)
        ).to_be_visible()

        self.enter_text_to_element(
            self.review_input,
            text
        )

        self.click_element(
            self.rating_button
        )

        self.page.get_by_role(
            "option",
            name=str(rating)
        ).click()

        self.click_element(
            self.send_button
        )

    def check_review_exists(self, text):

        expect(
            self.page.get_by_text(text)
        ).to_be_visible()