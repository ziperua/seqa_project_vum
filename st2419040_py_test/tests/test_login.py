import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from tests.test_data import VALID_USER, VALID_PASSWORD, LOCKED_USER, WRONG_PASSWORD

def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login(VALID_USER, VALID_PASSWORD)
    
    assert "inventory" in driver.current_url

def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login(VALID_USER, WRONG_PASSWORD)
    
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username and password do not match" in error.text

def test_no_username(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", VALID_PASSWORD)

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Epic sadface: Username is required" in error.text

def test_locked_out_user(driver):
    page = LoginPage(driver)
    page.open()
    page.login(LOCKED_USER, VALID_PASSWORD)

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Epic sadface: Sorry, this user has been locked out" in error.text

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.logout()

    assert "Swag Labs" in driver.title

def test_products_displayed(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    products = inventory_page.get_products()

    assert len(products) > 0
