"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
import requests
from jinja2 import Environment
from jinja2 import FileSystemLoader
from envs import *
import xml.etree.ElementTree

requests.packages.urllib3.disable_warnings()

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
IMCSUP_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/imcSupTemplates'))


def makeCall(p_url, method, data=""):
    """
    Main method to make an API call to IMC Supervisor. Please use this one to all the calls that you want to make
    :param p_url: API URL
    :param method: POST/GET are supported at this moment
    :param data: Payload to send
    :return:
    """
    # TODO: IMC Sup can return a 200 (ok) code including an error message on the response
    headers = {'X-Cloupia-Request-Key': get_imcsup_api_key()}
    if method == "POST":
        response = requests.post(get_imcsup_url() + p_url, data=data, headers=headers, verify=False)
    elif method == "GET":
        response = requests.get(get_imcsup_url() + p_url, headers=headers, verify=False)
    else:
        raise Exception(method + " not supported")
    if 199 < response.status_code < 300:
        return response.text
    else:
        raise Exception(response.text)


def getServers():
    """
    Get all servers managed by IMC Supervisor
    :return: XML (in plain text) with the list of servers
    """
    print("Getting all servers from IMC")
    p_url = "cloupia/api-v2/CIMCServerByMacAddress"
    textResponse = makeCall(p_url, "GET")
    xmlResponse = xml.etree.ElementTree.fromstring(textResponse)
    return xmlResponse.find('response').getchildren()


def AddServerRackAccountWithPass(accountName, serverIP, username, password):
    """
    Adds a Server Rack Account
    :param accountName: Name used to identify the server
    :param serverIP: IP address of the server
    :param username: Server username
    :param password: Server password
    :return:
    """
    p_url = "cloupia/api-v2/CIMCInfraAccount"
    template = IMCSUP_TEMPLATES.get_template('AddServerRackAccountWithPass.j2.xml')
    payload = template.render(name=accountName, server=serverIP, username=username, password=password)
    makeCall(p_url, method="POST", data=payload)


def AddServerRackAccountWithCredPolicy(accountName, serverIP, policy):
    """
    Adds a Server Rack Account
    :param accountName: Name used to identify the server
    :param serverIP: IP address of the server
    :param policy: Credential policy name
    :return:
    """
    p_url = "cloupia/api-v2/CIMCInfraAccount"
    template = IMCSUP_TEMPLATES.get_template('AddServerRackAccountWithCredPolicy.j2.xml')
    payload = template.render(name=accountName, server=serverIP, policy=policy)
    makeCall(p_url, method="POST", data=payload)


def getServersIp():
    """
    :return: an array of strings, each item representing an IP for a CIMC server added to IMC Supervisor
    """
    result = []

    for server in getServers():
        result.append(server.findtext("v4IPAddr"))
    return result
