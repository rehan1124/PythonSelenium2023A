import inspect
import os
import time

import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:

    def take_screenshot(self):
        # Check if directory <screenshots> is present
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = time.strftime('%Y%m%d%H%M%S')
        frame = inspect.currentframe()
        calling_frame = inspect.getouterframes(frame)[1]

        # Check if a directory with <Test classname> exists
        class_name = calling_frame[0].f_locals.get('self', None).__class__.__name__
        classname_dir = os.path.join(os.getcwd(), "screenshots", class_name)
        if not os.path.exists(classname_dir):
            os.makedirs(classname_dir)

        # Check if a directory with <Test name> exists
        function_name = calling_frame.function
        functionname_dir = os.path.join(os.getcwd(), "screenshots", class_name, function_name)
        if not os.path.exists(functionname_dir):
            os.makedirs(functionname_dir)

        screenshot_name = f"{class_name}_{function_name}_{timestamp}.png"

        screenshot_path = os.path.join(os.getcwd(), "screenshots", class_name, function_name, screenshot_name)
        time.sleep(1)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
