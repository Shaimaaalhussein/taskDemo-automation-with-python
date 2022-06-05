"""
This module contains basic rest api requests
check their responses
"""

#-----------------------------------------------------------------------------------------------
#imports
#-----------------------------------------------------------------------------------------------
from configuration import configFile
from configuration import configurationReader
import pytest
import requests
import json
from jsonpath_ng import jsonpath, parse

#-----------------------------------------------------------------------------------------------
#tests
#-----------------------------------------------------------------------------------------------


def test_api():

#Arrange
 url=configurationReader.get_API_url()+"current"

#Act
 parameters = {
        "access_key": "aa4321e8fe76a182c0b33a32b74df4cb",
        "query": "New York",
    }
 response=requests.get(url,params=parameters)
 body=response.json()
 print(body)

 #Get value using json path
 jsonpath_expression = parse('request.query')
 match = jsonpath_expression.find(body)


# Assert
 assert response.status_code==200
 assert "New York" in  match[0].value