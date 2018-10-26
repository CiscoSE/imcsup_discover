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

import os

__author__ = "Santiago Flores Kanter (sfloresk@cisco.com)"


def get_imcsup_api_key():
    return os.getenv("IMCSUP_API_KEY", "")


def get_imcsup_url():
    return os.getenv("ICMSUP_URL", "")

def get_policy_name():
    return os.getenv("CREDENTIAL_POLICY", "")
