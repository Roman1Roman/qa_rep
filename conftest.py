import pytest
from selene import be, have, browser

@pytest.fixture()
def opening_browser_neg():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl').press_enter()

@pytest.fixture()
def search_positive():
    browser.element('[class="ExCKkf z1asCe rzyADb"]').click()
    # browser.element('class="RNNXgb"').click()
    browser.element('[class="gLFyf"]').type('RedFab').press_enter()

@pytest.fixture()
def search_neagative_assert():
    browser.element('[class="ExCKkf z1asCe rzyADb"]').click()
    browser.element('[class="gLFyf"]').type('asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl')