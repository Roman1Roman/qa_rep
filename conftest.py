from time import sleep

import pytest
from selene import be, have, browser


@pytest.fixture()
def scale_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

# @pytest.fixture()
# def opening_browser_neg(scale_window):
#     browser.open('https://google.com')
#     browser.element('[name="q"]').should(be.blank).type('asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl').press_enter()

# @pytest.fixture()
# def search_positive():
#     browser.element('[class="ExCKkf z1asCe rzyADb"]').click()
#     # browser.element('class="RNNXgb"').click()
#     browser.element('[class="gLFyf"]').type('RedFab').press_enter()
#
# @pytest.fixture()
# def search_negative_assert():
#     browser.element('[class="ExCKkf z1asCe rzyADb"]').click()
#     browser.element('[class="gLFyf"]').type('asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl').press_enter()