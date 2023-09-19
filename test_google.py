from selene import be, have, browser
import pytest


def test_result_is_found(scale_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_negative_search_result(scale_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl').press_enter()
    assert browser.element('[class="card-section"]')\
    .should(have.text('По запросу asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl ничего не найдено'))
