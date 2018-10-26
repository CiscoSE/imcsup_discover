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
import sys, getopt, ipaddress
from controllers import imcsupcontroller
from imcsdk.imchandle import ImcHandle
from imcsdk import imcexception
from envs import *

if __name__ == "__main__":
    # Parameters check
    argv = sys.argv[1:]
    if len(argv) < 1:
        print 'Network and prefix parameters are mandatory:'
        print '\tmain.py -n <network/prefix>'
        sys.exit(2)
    network = None
    prefix = None
    try:
        opts, args = getopt.getopt(argv, "hn:", ["network="])
    except getopt.GetoptError:
        print 'Unrecognized parameters:'
        print '\tmain.py -n <network/prefix>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '\tmain.py -n <network/prefix>'
            sys.exit()
        elif opt in ("-n", "--network"):
            network = arg
    if network is None:
        print 'Network parameter is mandatory:'
        print '\tmain.py -n <network/prefix>'

    # Get a list of server IPs added to IMC Supervisor
    imcServersIp = imcsupcontroller.getServersIp()

    # For each IP in the given subnet, check if that IP is already added to IMC Supervisor
    # If it is not added, check with a bogus credential (123/123) if there is a CIMC
    # If there is a CIMC in the IP, add it to IMC Supervisor with the credential policy configured as CREDENTIAL_POLICY env variable
    for ip in ipaddress.IPv4Network(u'' + network):
        if str(ip) not in imcServersIp:
            # Create a connection handle
            handle = ImcHandle(ip=str(ip), username="123", password="123")
            try:
                # Timeout is 2 seconds, can be increased if needed
                handle.login(timeout=2)
            except imcexception.ImcException:
                # If an ImcException is raised, there is a CIMC in this IP
                print ("UCS Server found at " + str(ip))
                imcsupcontroller.AddServerRackAccountWithCredPolicy(
                    accountName=str(ip),
                    serverIP=str(ip),
                    policy=get_policy_name()
                )
            except:
                # All other exceptions means no CIMC in this IP
                pass
