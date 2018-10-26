# IMC Supervisor Discover Tool

This tool allows you to discover UCS servers from a given subnet. It uses IMC Supervisor API calls to:

* Retrieve the servers already added to IMC Supervisor
* Check for new UCS servers in the IPs from the given subnet (excluding the IPs from the servers present in IMC Supervisor)
* Add the servers found to IMC Supervisor for inventory collection 

## Contact

* Santiago Flores Kanter - sfloresk@cisco.com

## License

Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

## Source installation in linux based systems

Works with python 3.7

In order to run this in your environment follow these steps:

1) Clone repo

```bash
git clone https://www.github.com/ciscose/imcsup_discover.git
```

2) Within the root directory of the application, install pip dependencies (use a virtual environment when possible)

```bash
pip install -r requirements.txt
```


3) Set environmental variables

```bash
export IMCSUP_API_KEY=<YOUR_IMC_API_KEY>
export ICMSUP_URL=<YOUR_IMC_URL>
export CREDENTIAL_POLICY=<IMC_CREDENTIAL_POLICY>
```

For example

```bash
export IMCSUP_API_KEY=123456789901234567890234567800
export ICMSUP_URL=https://10.0.0.1/
export CREDENTIAL_POLICY=lab1
```

4) Run the script

```bash
python main.py -n <network/prefix>
```
For example, if you want to add all servers in subnet 10.0.0.0/24 use this command
```bash
python main.py -n 10.0.0.0/24
```



