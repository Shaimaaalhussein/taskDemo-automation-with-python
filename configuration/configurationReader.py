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

# Method to get api baseURL
def get_API_url():
    config=read_config()
    apiURL = config['ApiSettings']['APIBaseUrl']
    return apiURL

# Method to get mobile capablities
def get_mobile_cap():
    with open('capablity.json', 'r') as f:
        config = json.load(f)
    return config

