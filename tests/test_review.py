from random import randint

import allure
import pytest

from config import EMAIL, PASSWORD
from pages.login_page import CinescopeLoginPage
from pages.movie_page import MoviePage


@allure.epic("UI")
@allure.feature("Отзывы")
@pytest.mark.ui
class TestReview:

    @allure.title("Добавление отзыва к фильму")
    def test_add_review(self, login_page, movie_page):

        with allure.step("Открыть страницу логина"):
            login_page.open()

        with allure.step("Авторизоваться"):
            login_page.login(
                EMAIL,
                PASSWORD
            )

        with allure.step("Открыть фильм, в который можно оставить отзыв"):
            movie_page.open_first_movie()

        review = f"Playwright экзамен {randint(1000,9999)}"

        with allure.step("Добавить отзыв"):
            movie_page.add_review(review, 5)

        with allure.step("Проверить, что отзыв появился"):
            movie_page.check_review_exists(review)

        with allure.step("Сделать скриншот"):
            movie_page.make_screenshot_and_attach_to_allure()