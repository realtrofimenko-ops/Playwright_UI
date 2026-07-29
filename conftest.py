import pytest

from pages.login_page import CinescopeLoginPage
from pages.movie_page import MoviePage

DEFAULT_UI_TIMEOUT = 30000


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=300
    )

    yield browser

    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    context.set_default_timeout(DEFAULT_UI_TIMEOUT)

    yield context

    context.tracing.stop(path="trace.zip")

    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()

    yield page

    page.close()


@pytest.fixture
def login_page(page):
    return CinescopeLoginPage(page)


@pytest.fixture
def movie_page(page):
    return MoviePage(page)