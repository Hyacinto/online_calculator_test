import pytest
from playwright.sync_api import sync_playwright

def push_button(page,Params):
    print(Params)
    for Param in Params:
        button = page.locator(f'div.calc div.btn div.char.number.ripple:has-text("{Param}"),div.calc div.btn div.char.operator:has-text("{Param}"),div.calc div.btn div.char.operator.equal:has-text("{Param}")')
        button.click()

def test_calculator(Params, Result, setup_teardown):
    page = setup_teardown
    push_button(page, Params)
    actual_result = int(page.inner_text('#calculation span'))
    expected_result = Result
    assert  actual_result == expected_result


