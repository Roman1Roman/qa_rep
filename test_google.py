from selene import be, have, browser
import pytest


def test_negative_search_result(opening_browser_neg):

    assert browser.element('[class="card-section"]')\
    .should(have.text('По запросу asdasdasfasfgsdagfdsgshfdghbfnjmkmjhdndgfjnfukl ничего не найдено')), 'smth is bad'

def test_positive_search_result(search_positive):
    assert browser.element('[id="search"]').should(have.text('Цифровое производство в Санкт-Петербурге'))