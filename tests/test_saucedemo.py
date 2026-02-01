from selenium.webdriver.common.by import By
import pytest


def test_login(driver):
    driver.get("https://www.saucedemo.com")

    # Находим поля ввода
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Проверяем, что после логина мы на странице продуктов
    assert "inventory" in driver.current_url


def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем первый товар в корзину
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Проверяем, что товар появился в корзине
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert cart_item.text != ""


def test_product_name_and_price(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Проверяем первый товар
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert product_name != ""
    assert product_price.startswith("$")
