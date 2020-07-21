import pytest
from selenium import webdriver
import allure


# https://www.youtube.com/watch?v=CKTIkGxCNXU

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.implicitly_wait(20)
    driver.maximize_window();
    yield
    driver.quit()


@allure.description("Validate OrangeHRM with valid credentials")
@allure.severity(severity_level="CRITICAL")
def test_validLogin(test_setup):
    print(123321)
    # driver.get("http://192.168.5.25/user-management/auth/login");
    # driver.implicitly_wait(20)
    # driver.find_element_by_id("inputEmail3").clear();
    # driver.find_element_by_id("inputPassword3").clear();
    # enter_username("admin@mail.com");
    # enter_password("111111");
    # log("Clicking login button")
    # driver.find_element_by_id("login-form").click();
    # assert "dashboard" in driver.current_url


# @allure.description("Validate OrangeHRM with invalid credentials")
# @allure.severity(severity_level="NORMAL")
# def test_invalidLogin(test_setup):
#     driver.get("http://192.168.5.25/user-management/auth/login");
#     driver.find_element_by_id("inputEmail3").clear();
#     driver.find_element_by_id("inputPassword3").clear();
#     enter_username("admin@mail.com");
#     enter_password("11122111")
#     log("Clicking login button")
#     driver.find_element_by_id("login-form").click();
#     # try:
#     #     assert "dashboard" in driver.current_url
#     # finally:
#     #     if AssertionError:
#     #         allure.attach(driver.get_screenshot_as_png(),
#     #                       name="Invalid Credentials",
#     #                       attachment_type=allure.attachment_type.PNG)


@allure.step("Entering Username as {0}")
def enter_username(username):
    driver.find_element_by_id("inputEmail3").send_keys(username);


@allure.step("Entering Password as {0}")
def enter_password(password):
    driver.find_element_by_id("inputPassword3").send_keys(password)


@allure.step("{0}")
def log(message):
    print(message)
