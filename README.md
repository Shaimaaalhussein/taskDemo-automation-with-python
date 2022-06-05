# taskDemo-automation-with-python
This repository contains the project for the
* Automate tamm website using Selenium WebDriver with Python
* Automate swag lab mobile application using Appium with Python
* Automate api requests using requests with python

Follow the instructions in this README to install software requirements and run the project.


# Setup Instructions

## Python Setup

* This project requires Python 3.10.4
* You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

* You should also have a Python editor/IDE of your choice.
was using this [PyCharm](https://www.jetbrains.com/pycharm/).

* You will also need [Git](https://git-scm.com/) to copy this project code.
If you are new to Git, [try learning the basics](https://try.github.io/).

## WebDriver Setup

* For Web UI testing, you will need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/).
* You can use other browsers with Selenium WebDriver, but the project will use Chrome.

## WebDriver and Selenium Setup 

* Open command line 
* Install selenium using "Python -m pip install -U Selenium".
* Install webdriver manager using "pip install webdriver-manager". 

## Pytest Setup 

Install pytest using "pip install pytest".

## Requests Setup 

* This for api requests.
* Install requests using "pip install requests".
* Install json path 'pip install jsonpath-ng'

## Html report setup

pip install pytest-html.

## Appium setup

* Setup the JDK bin folder path in your system’s environment variable.
* Install android SDK >>add ANDROID_HOME in path
* Install appium server GUI v1.22.
* Install nodeJs.
* open appium server adding
  * HOST =127.0.0.1
  * PORT =4723
* Then start server

## Project Setup

1. Clone this repository.
2. Run `cd taskDemo-automation-with-python' to enter the project.
3. Run all the previous installation to install the dependencies.
4. Run 'python -m pytest' for all testcases.
5. Run 'python -m pytest tests/{testname}.py' to run specific test file.
6. Create a branch for your code changes. (See *Repository Branching* below.)
7. For mobile app install latest version from 'https://github.com/saucelabs/sample-app-mobile/releases/'

## Repository Branching

* The `master` branch contains the code for the project's starting point.
* The project is basically empty in the `master` branch.

* If you want to code along with the course, then create a branch for your work off the `master` branch.
To create your own branch named `project/develop`, run:

    * > git checkout master
    * > git branch project/develop
    * > git checkout project/develop

* The `tests/*` contain the completed code for project parts.

* `tests/test_web.py`
* `tests/test_mobile.py`
* `tests/test_api.py`

## Create configuration file

Create a new file named 'configFile'.py and add the following code

import configparser

 # CREATE OBJECT
 config_file = configparser.ConfigParser()

 # ADD WEB SECTION
 config_file.add_section("WebSettings")

 # ADD SETTINGS TO SECTION
 config_file.set("WebSettings", "webUrl", "https://www.tamm.abudhabi/")

 # SAVE CONFIG FILE
 with open(r"configurations.ini", 'w') as configfileObj:

    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

# Adding mobile capabilities with adding the following code:
 
 import json

 # ADD MOBILE CAPABLITIES TO JSON FILE
 desiredCapablities = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "FTNA05CGHGE00GT",
    "appPackage": "com.swaglabsmobileapp",
    "appActivity": "com.swaglabsmobileapp.MainActivity"
 }

  with open('capablity.json', 'w') as f:
    json.dump(desiredCapablities, f)


## Read from configurations files

 import configparser
 
 import json
 # Method to read config file settings

 def read_config():

    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config
 
 # Method to get web URL
 def get_web_url():

    config=read_config()
    webURL = config['WebSettings']['webUrl']
    return webURL
 # Method to get mobile app
 def get_mobile_cap():

    with open('capablity.json', 'r') as f:
        config = json.load(f)
    return config

## Defining Page Objects

*Example Branch: pages/homePage.py*

A **page object** is an object representing a Web page or component.
They have *locators* for finding elements,
as well as *interaction methods* that interact with the page under test.
Page objects make low-level Selenium WebDriver calls
so that tests can make short, readable calls instead of complex ones.

Since we have our test steps, we know what pages and elements our test needs.
There are 3 pages under pages and 2 base pages for common interaction like click or scroll 
each with a few interactions:

1. The base page
   * make action on element by passing locators for web
2. The mobile base page
   * make action on element by passing locators for mobile
3. The home page page
   * Get the locators of home page of tamm and interactions
4. The start and manage page page
   * Get the locators of start and manage page of tamm and interaction
5. The swag lab page
   * Get the locators of swag lab and interactions

Every page object needs a reference to the WebDriver instance.
That's why the `__init__` methods take in and store a reference to `browser`.

## Parallel execution

* we need to install this 'pip install pytest-xdist'
* This command to run parallel 'python -m pytest -n 3'


The "-n 3" arguments tells pytest to run 3 tests in parallel.
We have 1 web test, and most machines can handle 3 Web UI tests simultaneously.
When the tests run, notice how 3 browser instances open at once - one per test.


## Reporting 

* For html report you need to run this 'python -m pytest --html=report.html'
* Report will be saved in project directory named report.html



