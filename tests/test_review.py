from random import randint

import allure
import pytest

from pages.login_page import CinescopeLoginPage
from pages.movie_page import MoviePage


@allure.epic("UI")
@allure.feature("Отзывы")
@pytest.mark.ui
class TestReview:

    @allure.title("Добавление отзыва")
    def test_add_review(
            self,
            register_page,
            login_page,
            movie_page
    ):

        with allure.step("Регистрация пользователя"):
            register_page.open()
            email, password = register_page.register()

        with allure.step("Авторизация"):

            login_page.login(
                email,
                password
            )
            print(login_page.page.url)
            login_page.page.wait_for_timeout(5000)

        with allure.step("Открыть первый фильм"):

            movie_page.open_first_movie()

        review = f"Playwright {randint(10000,99999)}"

        with allure.step("Добавить отзыв"):

            movie_page.add_review(
                review,
                5
            )

        with allure.step("Проверить отзыв"):

            movie_page.check_review_exists(review)

        movie_page.make_screenshot_and_attach_to_allure()