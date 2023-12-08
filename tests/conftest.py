import allure
import pytest
from selenium import webdriver

from utilities.read_config import read_config


@pytest.fixture()
def setup(request):
    # Read config.ini
    url = read_config("DEFAULT", "url")
    browser = read_config("DEFAULT", "browser")
    default_wait_time = read_config("DEFAULT", "implicit_wait")
    print(
        f"Application url: {url}; Browser: {browser}; Implicit wait applied: {default_wait_time} seconds"
    )

    # Create driver instance based in <browser>
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(default_wait_time)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def capture_screenshot(request, setup):
    yield
    if request.session.testsfailed > 0:
        try:
            allure.attach(
                setup.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture and attach screenshot: {e}")
