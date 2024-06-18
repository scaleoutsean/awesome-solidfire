#!/usr/bin/env python3

######################################################################################
# Synopsis: solidfire-qos-policy-id-to-trident-qos.py                                #
# Gathers SolidFire QoS policies by IDs and saves to trident.conf. Because having    #
# Trident automatically apply the QoS policy ID to a volume or fallback to internal  #
# defaults is too damn hard.                                                         #
# More:                                                                              # 
# https://scaleoutsean.github.io/2024/06/19/trident-policy-sucker-for-solidfire-backends.html
#                                                                                    #
# Author: @scaleoutSean                                                              #
# https://github.com/scaleoutsean/awesome-solidfire                                  #
# License: the Apache License 2.0                                                    #
######################################################################################

# Modify MVIP, USER, and PASSWORD to match your environment or use startup arguments.

import argparse
import logging
import json
import os
from getpass import getpass
from solidfire.factory import ElementFactory
from solidfire import common
from solidfire.common import LOG
from solidfire.common import ApiServerError
from solidfire.common import SdkOperationError

MVIP = 'https://192.168.1.30'
USER = 'admin'
PASSWORD = ''


TRIDENT_SAMPLE = """{
    "version": 1,
    "storageDriverName": "solidfire-san",
    "backendName": "SF-PROD-192.168.1.34",
    "limitVolumeSize": "100000000000",
    "Endpoint": "https://trident:b00lsh33t@192.168.1.34/json-rpc/12.5",
    "SVIP": "192.168.103.34:3260",
    "TenantName": "demodemodemo",
    "Types": [{"Type": "bronze", "Qos": {"minIOPS": 200, "maxIOPS": 400, "burstIOPS": 600}},
              {"Type": "silver", "Qos": {"minIOPS": 401, "maxIOPS": 600, "burstIOPS": 1000}},
              {"Type": "gold", "Qos": {"minIOPS": 601, "maxIOPS": 990, "burstIOPS": 2000}}],
    "region": "prod"
}
"""

SOLIDFIRE_QOS_POLICY_SAMPLE = """{
  "id": 1,
  "result": {
    "qosPolicy": {
      "name": "goled",
      "qos": {
        "burstIOPS": 1000,
        "burstTime": 60,
        "curve": {
          "4096": 100,
          "8192": 160,
          "16384": 270,
          "32768": 500,
          "65536": 1000,
          "131072": 1950,
          "262144": 3900,
          "524288": 7600,
          "1048576": 15000
        },
        "maxIOPS": 800,
        "minIOPS": 100
      },
      "qosPolicyID": 1
      "volumeIDs": [
        2,
        172
      ]
    }
  }
}"""


def qos_policy_list(value):
    try:
        return [int(v) for v in value.split(',')]
    except ValueError:
        raise argparse.ArgumentTypeError('QoS policy ID must be an integer or comma-separated integers.')        

PARSER=argparse.ArgumentParser(description='Gather SolidFire QoS policies by IDs and save to trident.conf.')
PARSER.add_argument('-m', '--mvip', help='MVIP of the SolidFire cluster.', type=str, required=True)
PARSER.add_argument('-u', help='Username for the SolidFire API.', type=str, required=True)
PARSER.add_argument('-p', help='Password for the SolidFire API.', type=str, required=False)
PARSER.add_argument('-q', '--qos-policy-id', help='QoS policy ID to gather.', type=qos_policy_list, required=True)
PARSER.add_argument('-o', '--out-file-path-name', help='Output file path and name.', type=str, required=False, default=os.path.join(os.getcwd(), 'solidfire-backend.json.new'))
ARGS=PARSER.parse_args()
common.LOG.setLevel(logging.ERROR)
LOG.addHandler(logging.StreamHandler())

if ARGS.p is None:
    ARGS.p = getpass(prompt='Password: ')

if ARGS.qos_policy_id is None:
    LOG.error('At least one QoS policy ID is required.')
else:
    LOG.info("Gathering QoS policies from SolidFire cluster: %s", ARGS.mvip)
    qos_policy_list = ARGS.qos_policy_id
    LOG.info("QoS policies required: %s", qos_policy_list)    

sfe = ElementFactory.create(
        ARGS.mvip,
        ARGS.u,
        ARGS.p,
        print_ascii_art=False)

qos_policy_list = ARGS.qos_policy_id
qos_items = []
for pol_id in qos_policy_list:
    print("Getting QoS policy ID " + str(pol_id))
    try:
        params = { 'qosPolicyID': pol_id }
        qpl = sfe.invoke_sfapi(method="GetQoSPolicy", parameters=params)['qosPolicy']
        qos_items.append(qpl)
    except:
        LOG.error("Unable to obtain policy ID " + str(pol_id) + " from SolidFire cluster. Please check if the policy ID exists.")

print("Found", len(qos_items) , "QoS policies.")

list_o_types= []
for q in qos_items:
    qos_item = {}
    qos_item['Type'] = q['name']    
    qos_vals = {
        "minIOPS": q['qos']['minIOPS'],
        "maxIOPS": q['qos']['maxIOPS'],
        "burstIOPS": q['qos']['burstIOPS']
    }
    qos_item['Qos'] = qos_vals
    list_o_types.append(qos_item)  

print("\n\n== QoS-generated Types Only ===\n\n")
print('"Types":', json.dumps(list_o_types))
print("\nNOTE: don't forget the , at the end of the list of types if you're adding this to existing SolidFire back-end configuration file!")

print("\n\nTRIDENT SAMPLE CONFIG BEFORE:\n")
t_before = json.loads(TRIDENT_SAMPLE)
# t_before['Types'] = list_o_types
print(json.dumps(t_before, indent=4))

print("\n\nTRIDENT SAMPLE CONFIG AFTER:\n")
t_after = t_before
t_after['Types'] = list_o_types
print(json.dumps(t_after, indent=4))

with open(ARGS.out_file_path_name, 'w') as f:
    f.write(json.dumps(t_before, indent=4))
    os.chmod(ARGS.out_file_path_name, 0o600)
    print("\n\nWrote Trident configuration (600 file permissions mode) to: ", ARGS.out_file_path_name)

print("\nPlease *remember* to copy the new back-end JSON file without *changing* the permissions of the original file. \nsolidfire-backend.json.new is protected with 0600 because there may be a SolidFire password in it, but your own configuration file may need different permissions.")   
print("\nYou may want to remove solidfire-backend.json.new as soon as you do not need it.")
print("\nYou may also modify the script to run from job scheduler and periodically update the original file if you're sure everything checks out.")
print("\nDone!")

