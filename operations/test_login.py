import pytest
from selenium import webdriver
import allure
from selenium.webdriver.chrome.options import Options

# https://www.youtube.com/watch?v=CKTIkGxCNXU
# pytest -v  login.py
# pytest -v   -p no:warnings login.py

@pytest.fixture()
def test_setup():
    global driver

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.quit()


@allure.description("Validate OrangeHRM with valid credentials")
@allure.severity(severity_level="CRITICAL")
def test_validLogin(test_setup):
    driver.get("http://192.168.5.25/user-management/auth/login");
    driver.implicitly_wait(20)
    driver.find_element_by_id("inputEmail3").clear()
    driver.find_element_by_id("inputPassword3").clear()
    enter_username("admin@mail.com")
    enter_password("111111")
    log("Clicking login button")
    driver.find_element_by_id("login-form").click()
    # assert "dashboard" in driver.current_url


@allure.step("Entering Username as {0}")
def enter_username(username):
    driver.find_element_by_id("inputEmail3").send_keys(username)


@allure.step("Entering Password as {0}")
def enter_password(password):
    driver.find_element_by_id("inputPassword3").send_keys(password)


@allure.step("{0}")
def log(message):
    print(message)
