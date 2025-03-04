import csv
import pytest
from playwright.sync_api import sync_playwright

def read_test_data():
    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='|') 
        test_cases = []
        for row in reader:
            
            params_str, result = row[0], row[1] 
            params = tuple(params_str.split(','))  
            result = int(result)  
            test_cases.append((params, result))  

    return test_cases
    
def pytest_generate_tests(metafunc):
    if "Params" in metafunc.fixturenames and "Result" in metafunc.fixturenames:
        test_data = read_test_data()
        print(f"Generated test data: {test_data}") 
        metafunc.parametrize("Params, Result", test_data)

@pytest.fixture(scope="session")
def setup_teardown():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page() 
        page.goto("https://calculatorlib.com/basic-calculator")
        close_button = page.locator("button.fc-close:nth-child(1)")
        close_button.wait_for(state='visible')
        close_button.click()
        yield page
        ac_button = page.locator(".btn .char", has_text="AC")
        ac_button.click()
        browser.close()
