import configparser
import json
# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD WEB SECTION
config_file.add_section("WebSettings")
# ADD SETTINGS TO SECTION
config_file.set("WebSettings", "webUrl", "https://www.tamm.abudhabi/")

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

# ADD API SECTION
config_file.add_section("ApiSettings")
# ADD SETTINGS TO SECTION
config_file.set("ApiSettings", "APIBaseUrl", "http://api.weatherstack.com/")

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:

    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()


