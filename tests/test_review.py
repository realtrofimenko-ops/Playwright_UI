from random import randint

import allure
import pytest

from pages.login_page import CinescopeLoginPage
from pages.movie_page import MoviePage


@allure.epic("UI")
@allure.feature("Отзывы")
@pytest.mark.ui
class TestReview:

    @allure.title("Добавление отзыва к фильму")
    def test_add_review(self, page):

        login_page = CinescopeLoginPage(page)

        login_page.open()

        login_page.login(
            "real.trofimenko@yandex.ru",
            "Asdqwe123Q"
        )

        page.wait_for_timeout(3000)

        movie_page = MoviePage(page)

        movie_page.open()

        review = f"Playwright экзамен {randint(1000,9999)}"

        movie_page.add_review(review, 5)

        movie_page.check_review_exists(review)

        movie_page.make_screenshot_and_attach_to_allure()