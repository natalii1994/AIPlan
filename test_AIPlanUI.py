import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(15)
    yield browser

def test_authorization(browser):
    browser.get('https://test.aiplan.aisa.ru/signin')

    login = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
    sleep(2)
    login.send_keys('ttest06031994@mail.ru')

    password = browser.find_element(By.CSS_SELECTOR,"input[type='password']")
    sleep(2)
    password.send_keys('123456')

    sleep(2)
    button_click = browser.find_element(By.CSS_SELECTOR,"button.full-w")
    button_click.click()

    div_click = browser.find_element(By.CSS_SELECTOR,"div.text-avatar")
    sleep(2)
    div_click.click()

    p_click = browser.find_element(By.CSS_SELECTOR,"p.profile-button__exit-text")
    sleep(2)
    p_click.click()

    sleep(2)
    browser.quit()