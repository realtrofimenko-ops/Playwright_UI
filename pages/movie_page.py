import allure
from pages.base_page import BasePage


class MoviePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.url = "https://dev-cinescope.coconutqa.ru/movies/64744"

        self.review_input = "[data-qa-id='movie_review_input']"
        self.rating_button = "button[role='combobox']"
        self.send_button = "[data-qa-id='movie_review_submit_button']"

    @allure.step("Открыть страницу фильма")
    def open(self):
        self.open_url(self.url)

    @allure.step("Добавить отзыв '{text}' с оценкой {rating}")
    def add_review(self, text, rating):

        self.enter_text_to_element(self.review_input, text)

        self.click_element(self.rating_button)

        self.page.get_by_role("option", name=str(rating)).click()

        self.click_element(self.send_button)

    @allure.step("Проверить, что отзыв появился")
    def check_review_exists(self, text):
        self.wait_for_element(f"text={text}")