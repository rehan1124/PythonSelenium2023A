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
    is_grid_enabled = read_config("DEFAULT", "GRID")

    print(
        f"Application url: {url}; Browser: {browser}; Implicit wait applied: {default_wait_time} seconds; \
        Grid: {is_grid_enabled}"
    )

    # Create driver instance based in <browser>
    if is_grid_enabled.__eq__("No"):
        # If Selenium-Grid is <No>, then below code will be executed based on browser option given.
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser.__eq__("firefox"):
            driver = webdriver.Firefox()
        elif browser.__eq__("edge"):
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()
    else:
        # If Selenium-Grid is <Yes>, then below code will be executed based on browser option given.
        if browser == "chrome":
            options = webdriver.ChromeOptions()
        elif browser.__eq__("firefox"):
            options = webdriver.FirefoxOptions()
        elif browser.__eq__("edge"):
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.ChromeOptions()

        selenium_hub_url = "http://172.29.112.1:4444/wd/hub"
        driver = webdriver.Remote(command_executor=selenium_hub_url, options=options)

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
