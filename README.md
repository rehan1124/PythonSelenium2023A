# PythonSelenium2023A
A Hybrid Automation Testing framework created using Python, Selenium, Pytest, Openpyxl

* Once project is cloned, navigate to project directory, create a virtual env using below command and install dependencies.
```
python -m venv .venv
venv/Scripts/activate
pip install -r requirements.txt
```

* With above setup done, you are ready to continue using this framework for creating new tests as well as run them.

* To run tests, execute below command to run all tests at once.
```commandline
python -m pytest ./tests -v -s
```

* The framework also support Allure-reports. Make sure you have below installed in your system.
```
1) Java / JDK (Check using <java --version>)
2) Node.js / NPM (Check using <npm --version>)
3) allure-commandline (Install with <npm install -g allure-commandline>) (Check using <allure --version>)
```

* To generate allure reports, user has to first run Pytest tests. To do so, run command:
```
pytest --alluredir="./Reports"
Or
pytest .\tests\test_search.py -v -s --alluredir="Reports"
And then
allure serve Reports
```

