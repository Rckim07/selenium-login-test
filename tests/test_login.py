import time
from pages.login_page import LoginPage

def test_login_valid(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)
    assert "inventory" in driver.current_url

def test_login_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "secret_sauce")
    time.sleep(2)
    assert "inventory" not in driver.current_url
def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "wrong_password")
    time.sleep(2)
    assert "inventory" not in driver.current_url

def test_login_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "secret_sauce")
    time.sleep(2)
    assert "inventory" not in driver.current_url

def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "")
    time.sleep(2)
    assert "inventory" not in driver.current_url

def test_login_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    time.sleep(2)
    assert "inventory" not in driver.current_url

def test_login_problem_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("problem_user", "secret_sauce")
    time.sleep(2)
    assert "inventory" in driver.current_url

def test_login_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("performance_glitch_user", "secret_sauce")
    time.sleep(3)  # performance_glitch_user có thể load chậm hơn
    assert "inventory" in driver.current_url

def test_login_with_spaces(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("  standard_user  ", "secret_sauce")
    time.sleep(2)
    assert "inventory" not in driver.current_url

def test_login_sql_injection(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("' OR '1'='1", "' OR '1'='1")
    time.sleep(2)
    assert "inventory" not in driver.current_url
