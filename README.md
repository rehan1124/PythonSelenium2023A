# PythonSelenium2023A

A Hybrid Automation Testing framework created using Python, Selenium, Pytest, Openpyxl

* Once project is cloned, navigate to project directory, create a virtual env using below command and install
  dependencies.

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

* Support for Selenium Grid. Go to `SeleniumGridFiles` folder and execute below commands. `selenium-manager true` will
  automatically add drivers

```
<**Standalone** mode>
java -jar selenium-server-4.16.1.jar standalone --selenium-manager true

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

<**Hub** (Router, Distributor, Session Map, New Session Queue, Event Bus) and **Node** mode>

java -jar .\selenium-server-4.16.1.jar hub
java -jar .\selenium-server-4.16.1.jar node --selenium-manager true

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

<**Distributed** mode>

1) Event Bus: Responsible for communication between different grid components

java -jar .\selenium-server-4.16.1.jar event-bus

2) Session Map: Maps session IDs to the Node where the session is running

java -jar .\selenium-server-4.16.1.jar sessions

3) Session Queue: adds new session requests to a queue, which will be queried by the Distributor

java -jar .\selenium-server-4.16.1.jar sessionqueue

4) Distributor: Queries the New Session Queue for new session requests,
and assigns them to a Node when the capabilities match.
Nodes register to the Distributor the way they register to the Hub in a Hub/Node Grid.

java -jar .\selenium-server-4.16.1.jar distributor --sessions <Session Map URL> --sessionqu
eue <Session Queue URL> --bind-bus false

5) Router: Redirects new session requests to the queue,
and redirects running sessions requests to the Node running that session.

java -jar .\selenium-server-4.16.1.jar router --sessions <Session Map URL> --distributor <Distributor URL>
--sessionqueue <Session Queue URL>

6) Nodes:

java -jar .\selenium-server-4.16.1.jar node --selenium-manager true
```

* To make full usage of Selenium Grid, run tests in parallel. Install python package pytest-xdist. Refer
  requirements.txt file. Below command will run 8 tests in parallel. Depends upon number of system processors.

```commandline
python -m pytest tests -n 8
```

* Getting started with _Docker_. Download Standalone Chrome Docker Image from
  here _https://hub.docker.com/r/selenium/standalone-chrome_ and follow the instructions. No need to change any other
  configurations (Only make sure to keep _GRID = Yes_ in _config.ini_ if you don't need to run tests locally). This will
  help you to run tests in Selenium Grid server with Chrome driver inside docker container.
