#!/usr/bin/env python3
###############################################################################
#                                                                             #
# Synopsis:                                                                   #
# Show node and slot location of disks in a SolidFire cluster                 #
#                                                                             #
# Similar command for SolidFire CLI (Python):                                 #
# sfcli drive list | jq '.drives | .[] | {id: .drive_id, node: .node_id}'     #
#                                                                             #
# Use case: node evacuation from the cluster (erase old SSDs, etc.)           #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

from solidfire.factory import ElementFactory

# reco: create read-only cluster admin account for reporting (read-only) scripts
sfe = ElementFactory.create('192.168.1.34', 'admin', 'admin', verify_ssl=False, print_ascii_art=False)

node_list = sfe.list_active_nodes().to_json()['nodes']
drive_list = sfe.list_drives().to_json()['drives']
for node in node_list:
    for drive in drive_list:
        if drive['nodeID'] == node['nodeID']:
            print("Drive", drive['driveID'], "is in chassis slot", drive['chassisSlot'], "of node", node['nodeID'])
