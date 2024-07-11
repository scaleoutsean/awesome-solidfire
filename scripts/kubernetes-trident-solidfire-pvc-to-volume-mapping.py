#!/usr/bin/env python3

######################################################################################
# Synopsis:                                                                          #
# kubernetes-trident-solidfire-pvc-to-volume-mapping.py maps Kubernetes/Trident      #
#   volume names to SolidFire names and IDs  to help with  storage monitoring and    # 
#   management in Kubernetes environments.                                           #
#                                                                                    #
# Author: @scaleoutSean                                                              #
# https://github.com/scaleoutsean/awesome-solidfire                                  #
# License: the Apache License Version 2.0                                            #
# (c) 2024 scaleoutSean                                                              #
######################################################################################

'''
- This is just a sample not meant for production use
- For production use the script would require error handling, logging, and continuous validation, especially before/after NetApp Trident updates
- The SolidFire API is unlikely to change at this point, so I'd be less concerned about changes in that area
- The script can be enhanced to gather information from a pair of Kubernetes-on-SolidFire clusters for use in DR/BC scenarios
- The script uses "sample inputs" from my lab, so that it can be tried without connecting to actual Kubernetes or SolidFire clusters
- If you can't get access to Trident, ask the admin to run *and sanitize* 'tridentctl -o json' output for you and upload output to S3 bucket
- You may use the SolidFire Python SDK to connect to the SolidFire cluster, or use the REST API directly
- More: https://scaleoutsean.github.io/2024/06/01/pvc-volume-relationships-in-solidfire-trident-part-1.html
'''

import json
import pprint

# SolidFire volumes, obtained with ListActiveVolumes or ListVolumes
sv = {'volumes': [{'access': {}, 'accountID': 1, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-02-27T17:04:09Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.data.1', 'lastAccessTime': '2024-03-30T15:49:50Z', 'lastAccessTimeIO': '2024-03-30T14:40:59Z', 'minFifoSize': 0, 'name': 'data', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000001f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000001', 'sliceCount': 1, 'status': 'active', 'totalSize': 2000683008, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': 'e6b28e75-c21c-4bad-8a2e-056bcec14e4c', 'volumeID': 1, 'volumePairs': [], 'volumeUUID': '4b31894c-b3d4-4dbc-a438-d60aa96f7c49'}, {'access': {}, 'accountID': 1, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-02-27T17:04:20Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.log.2', 'lastAccessTime': '2024-03-30T15:49:50Z', 'lastAccessTimeIO': '2024-03-30T14:40:59Z', 'minFifoSize': 0, 'name': 'log', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 100}, 'qosPolicyID': 1, 'scsiEUIDeviceID': '7763776200000002f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000002', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '6dc2588d-bedf-4a64-a958-e8377c38f551', 'volumeID': 2, 'volumePairs': [], 'volumeUUID': '8721d0a3-735a-4cad-9502-15b09827f710'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:46Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume11.36', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume11', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000024f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000024', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': '4b6968bf-dd91-4036-afff-d35eca4b526c', 'volumeID': 36, 'volumePairs': [], 'volumeUUID': '43bade00-2097-4a15-a0fc-b7a41ec1cd13'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:46Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume12.37', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume12', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000025f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000025', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': '24d779e0-9019-4511-ae33-50dd3b755e2e', 'volumeID': 37, 'volumePairs': [], 'volumeUUID': '8e0cf0c5-7fcd-4654-a9a3-b5058061cfab'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:47Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume13.38', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume13', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000026f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000026', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': '9aaf5292-c4b5-42a7-a068-6fe804baacfa', 'volumeID': 38, 'volumePairs': [], 'volumeUUID': '5886837e-fcb1-496b-8259-679c31cc2c6e'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:47Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume14.39', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume14', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000027f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000027', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': '8b46eb77-af08-4547-a34e-48f62c55fa63', 'volumeID': 39, 'volumePairs': [], 'volumeUUID': '01d17bce-4e5b-4ece-bfa3-84bd444cf0b9'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:48Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume15.40', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume15', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000028f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000028', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': 'e3a885c7-f94e-4fcf-8c63-69cfe7a5d6c2', 'volumeID': 40, 'volumePairs': [], 'volumeUUID': 'dcdacd57-4cc2-40bf-b9cb-28bc45f02445'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:48Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume16.41', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume16', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000029f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000029', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': '89cca7c3-8467-4eca-9afe-1c974a799a88', 'volumeID': 41, 'volumePairs': [], 'volumeUUID': '11e671da-712f-4e51-8a59-0e6480c74983'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:48Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume17.42', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume17', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '776377620000002af47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000002a', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': 'bb1f75e5-3ce2-4040-931c-9320dadd44d3', 'volumeID': 42, 'volumePairs': [], 'volumeUUID': '41ff8e62-9cce-46f3-9616-870f20f3550b'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:49Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume18.43', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume18', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '776377620000002bf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000002b', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': 'c0ffd08d-9d14-4f3b-8445-3dc5be1cdd89', 'volumeID': 43, 'volumePairs': [], 'volumeUUID': '7bdbcca8-4f82-4686-8139-a6998200d0f7'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:49Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume19.44', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume19', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '776377620000002cf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000002c', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': '384774fa-b29b-46fb-b7c9-a62c58eb5cfc', 'volumeID': 44, 'volumePairs': [], 'volumeUUID': 'be6b9bf7-5653-4e42-b57e-3fcbce5a5c0d'}, {'access': {}, 'accountID': 6, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-09-02T16:11:49Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.volume20.45', 'lastAccessTime': '2023-09-02T16:50:49Z', 'lastAccessTimeIO': '2023-09-02T16:50:49Z', 'minFifoSize': 0, 'name': 'volume20', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '776377620000002df47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000002d', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [1], 'volumeConsistencyGroupUUID': 'befc31de-560f-435e-8809-a978159c7ecf', 'volumeID': 45, 'volumePairs': [], 'volumeUUID': '3c43ca92-7477-4fde-a307-741e97604ad5'}, {'access': {}, 'accountID': 8, 'attributes': {'docker-name': 'pvc-ba3213cd-01bc-4920-b1c7-708ed89e5730', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"23.07.0-custom+e2344922b27d1aec8c2574153962ef7ea49e390d","backendUUID":"f069f7c4-759a-4758-9b90-564d290e76a4","platform":"kubernetes","platformVersion":"v1.25.14-rc1+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2023-09-15T08:00:17Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-ba3213cd-01bc-4920-b1c7-708ed89e5730.59', 'lastAccessTime': '2023-10-06T01:00:50Z', 'lastAccessTimeIO': '2023-10-06T01:00:50Z', 'minFifoSize': 0, 'name': 'pvc-ba3213cd-01bc-4920-b1c7-708ed89e5730', 'purgeTime': '', 'qos': {'burstIOPS': 400, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 200, 'minIOPS': 100}, 'scsiEUIDeviceID': '776377620000003bf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000003b', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': 'cc9e9aa0-e194-4eb6-a25e-0d816553c2c1', 'volumeID': 59, 'volumePairs': [], 'volumeUUID': '006c0fe4-70fd-4db9-8472-9ba485fff2c0'}, {'access': {}, 'accountID': 10, 'attributes': {}, 'blockSize': 4096, 'createTime': '2023-12-12T01:19:47Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.win1101.108', 'minFifoSize': 0, 'name': 'win1101', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '776377620000006cf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000006c', 'sliceCount': 1, 'status': 'active', 'totalSize': 5000658944, 'volumeAccessGroups': [3], 'volumeConsistencyGroupUUID': 'df76efa2-4c67-4ddf-8ea8-befda645415b', 'volumeID': 108, 'volumePairs': [], 'volumeUUID': '1451c03e-34fc-4557-9a08-1921be9ffef2'}, {'access': {}, 'accountID': 11, 'attributes': {'docker-name': 'pvc-8d31e43b-f942-4cf8-94db-a08762c745ee', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0-custom+unknown","backendUUID":"8f1221e5-ff50-40b9-afba-85ec352e219a","platform":"kubernetes","platformVersion":"v1.28.3","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-21T09:25:11Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-8d31e43b-f942-4cf8-94db-a08762c745ee.111', 'minFifoSize': 0, 'name': 'pvc-8d31e43b-f942-4cf8-94db-a08762c745ee', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 801, 'minIOPS': 401}, 'scsiEUIDeviceID': '776377620000006ff47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000006f', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': 'b5b3a6ab-2063-40d8-b8e0-d3ef0bee6082', 'volumeID': 111, 'volumePairs': [], 'volumeUUID': 'f345b08c-d3f8-49ec-927c-555136310ca5'}, {'access': {}, 'accountID': 11, 'attributes': {'docker-name': 'pvc-14a51322-16c8-4b95-a7e4-28d9963450b3', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0-custom+unknown","backendUUID":"b3680925-a9c1-4552-a1b4-1e4a0a273e8e","platform":"kubernetes","platformVersion":"v1.28.3","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-21T09:59:01Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-14a51322-16c8-4b95-a7e4-28d9963450b3.112', 'minFifoSize': 0, 'name': 'pvc-14a51322-16c8-4b95-a7e4-28d9963450b3', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000070f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000070', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '97d68042-b080-459d-8c28-e1f63e8ba49b', 'volumeID': 112, 'volumePairs': [], 'volumeUUID': '129538aa-94a8-4daf-aed4-22a435f666be'}, {'access': {}, 'accountID': 11, 'attributes': {'docker-name': 'pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0-custom+unknown","backendUUID":"b3680925-a9c1-4552-a1b4-1e4a0a273e8e","platform":"kubernetes","platformVersion":"v1.28.3","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-21T10:30:48Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c.113', 'minFifoSize': 0, 'name': 'pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000071f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000071', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '39b5003f-53e2-4ceb-9dd6-8e6dc5ec6742', 'volumeID': 113, 'volumePairs': [], 'volumeUUID': 'f2136efe-d887-43bf-957a-258abe462d96'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-fc799089-9559-4d97-84c8-d98e9dfbf884', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-22T08:06:58Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-fc799089-9559-4d97-84c8-d98e9dfbf884.115', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-fc799089-9559-4d97-84c8-d98e9dfbf884', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000073f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000073', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '6d262796-9d51-4607-ba24-ba42650939c2', 'volumeID': 115, 'volumePairs': [], 'volumeUUID': 'fd679d0c-2e5d-4b8e-a48a-391132f25bde'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-a7b61fe0-7e9d-40f4-bc06-9c1623adade4', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-22T08:07:54Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-a7b61fe0-7e9d-40f4-bc06-9c1623adade4.116', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-a7b61fe0-7e9d-40f4-bc06-9c1623adade4', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000074f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000074', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '9324577c-7be1-4917-9659-be670bdd82b1', 'volumeID': 116, 'volumePairs': [], 'volumeUUID': 'f4799aea-48b5-4781-b2af-6ddb4de50bcc'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-9812208f-72f5-41d8-9348-4fb42db8e6af', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-22T08:08:17Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-9812208f-72f5-41d8-9348-4fb42db8e6af.117', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-9812208f-72f5-41d8-9348-4fb42db8e6af', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000075f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000075', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '99cef758-8298-40ef-843d-0638d214787d', 'volumeID': 117, 'volumePairs': [], 'volumeUUID': '3044eddf-750f-4801-af54-7617fa6d2965'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-bd1254e7-4102-4b58-960c-70be158c75fc', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-22T14:55:35Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-bd1254e7-4102-4b58-960c-70be158c75fc.120', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-bd1254e7-4102-4b58-960c-70be158c75fc', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000078f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000078', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '6c00bc4e-b0f0-4521-9ebf-3fce9bbd0993', 'volumeID': 120, 'volumePairs': [], 'volumeUUID': '0f4000e2-757e-4bca-858e-538b1286b526'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-58d35404-479b-4c5d-a67b-d96521f63ce2', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T06:00:36Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-58d35404-479b-4c5d-a67b-d96521f63ce2.121', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-58d35404-479b-4c5d-a67b-d96521f63ce2', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000079f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000079', 'sliceCount': 1, 'status': 'active', 'totalSize': 8589934592, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': 'd1a5475d-e907-4244-9fe0-95416020dbc0', 'volumeID': 121, 'volumePairs': [], 'volumeUUID': '9324a4d9-958d-45fd-aec4-e4321e06402c'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-afc3936c-9cd4-47bb-bdf1-b1c46fd910ad', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T06:00:36Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-afc3936c-9cd4-47bb-bdf1-b1c46fd910ad.122', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-afc3936c-9cd4-47bb-bdf1-b1c46fd910ad', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '776377620000007af47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000007a', 'sliceCount': 1, 'status': 'active', 'totalSize': 8589934592, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': 'e4d0d8b5-9fdb-4d1f-b4f3-827ce902c3b5', 'volumeID': 122, 'volumePairs': [], 'volumeUUID': 'c62e14c9-c480-4a7d-8eb5-49a118a91434'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-c47a3f9f-4628-4e3b-8a86-313ec02f49b4', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T06:01:23Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-c47a3f9f-4628-4e3b-8a86-313ec02f49b4.123', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-c47a3f9f-4628-4e3b-8a86-313ec02f49b4', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '776377620000007bf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000007b', 'sliceCount': 1, 'status': 'active', 'totalSize': 8589934592, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '59aeb521-aa78-4af5-a9df-f8caa33fa835', 'volumeID': 123, 'volumePairs': [], 'volumeUUID': 'e0aca613-c85f-4337-ac4d-8f6392aff50e'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-515bccf3-577b-4149-9633-9da86913c933', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T06:01:58Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-515bccf3-577b-4149-9633-9da86913c933.124', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-515bccf3-577b-4149-9633-9da86913c933', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '776377620000007cf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000007c', 'sliceCount': 1, 'status': 'active', 'totalSize': 8589934592, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '324bda03-9c85-4c2f-abdf-ea1a717ba7d0', 'volumeID': 124, 'volumePairs': [], 'volumeUUID': '2f197686-6e34-4911-9ec0-cc6f10f227fc'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-910cc289-64b8-4cc9-a411-524fd713d950', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T06:09:38Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-910cc289-64b8-4cc9-a411-524fd713d950.125', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-910cc289-64b8-4cc9-a411-524fd713d950', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '776377620000007df47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000007d', 'sliceCount': 1, 'status': 'active', 'totalSize': 8589934592, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '861267e0-9580-4ade-9cc8-b4df62bfa329', 'volumeID': 125, 'volumePairs': [], 'volumeUUID': '5cbbf1d6-ca1e-410e-bf67-2b577c6ac636'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-a9531e89-7900-4265-9910-030142b4646a', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T07:12:47Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-a9531e89-7900-4265-9910-030142b4646a.127', 'lastAccessTime': '2024-04-16T09:41:20Z', 'lastAccessTimeIO': '2024-04-16T09:41:20Z', 'minFifoSize': 0, 'name': 'pvc-a9531e89-7900-4265-9910-030142b4646a', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '776377620000007ff47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000007f', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '224d2a5b-a763-4cf8-888b-c1a29857244d', 'volumeID': 127, 'volumePairs': [], 'volumeUUID': '7d393b37-d745-41cd-be51-84c5ddca64b3'}, {'access': {}, 'accountID': 12, 'attributes': {'docker-name': 'pvc-4bf6f5e2-bd1c-4908-88d0-62ecd66f6d33', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0","backendUUID":"6ebdc64a-76bd-4e2e-969f-64bcd575e288","platform":"kubernetes","platformVersion":"v1.28.7+k3s1","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-03-23T09:05:11Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-4bf6f5e2-bd1c-4908-88d0-62ecd66f6d33.133', 'lastAccessTime': '2024-04-16T09:41:30Z', 'lastAccessTimeIO': '2024-04-16T09:37:10Z', 'minFifoSize': 0, 'name': 'pvc-4bf6f5e2-bd1c-4908-88d0-62ecd66f6d33', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '7763776200000085f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000085', 'sliceCount': 1, 'status': 'active', 'totalSize': 1073741824, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '441cfcc2-1832-4f38-bef5-19011f82e500', 'volumeID': 133, 'volumePairs': [], 'volumeUUID': '239db833-7906-4e24-a8f9-abe4c42ac7f9'}, {'access': {}, 'accountID': 13, 'attributes': {'SfQosId': 1}, 'blockSize': 4096, 'createTime': '2024-03-30T07:14:58Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.win1.134', 'lastAccessTime': '2024-05-31T17:03:28Z', 'lastAccessTimeIO': '2024-05-31T17:03:28Z', 'minFifoSize': 0, 'name': 'win1', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 100}, 'qosPolicyID': 1, 'scsiEUIDeviceID': '7763776200000086f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000086', 'sliceCount': 1, 'status': 'active', 'totalSize': 2000683008, 'volumeAccessGroups': [4], 'volumeConsistencyGroupUUID': '8d7b9cef-4722-4b71-b2e9-a4f31a5b7bb8', 'volumeID': 134, 'volumePairs': [], 'volumeUUID': 'f4c64677-995a-4ed0-bf60-7de5d4610292'}, {'access': {}, 'accountID': 13, 'attributes': {}, 'blockSize': 4096, 'createTime': '2024-03-30T07:15:14Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': False, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.win2.135', 'lastAccessTime': '2024-05-31T17:03:28Z', 'lastAccessTimeIO': '2024-05-31T17:03:28Z', 'minFifoSize': 0, 'name': 'win2', 'purgeTime': '', 'qos': {'burstIOPS': 3000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 1500, 'minIOPS': 100}, 'qosPolicyID': 2, 'scsiEUIDeviceID': '7763776200000087f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000087', 'sliceCount': 1, 'status': 'active', 'totalSize': 20000538624, 'volumeAccessGroups': [4], 'volumeConsistencyGroupUUID': '7960deec-9b58-4bad-b9d2-c3769e6a1f0b', 'volumeID': 135, 'volumePairs': [], 'volumeUUID': '078d5287-91c4-4165-9c7a-4626f00dca8a'}, {'access': {}, 'accountID': 13, 'attributes': {'SfQosId': 1}, 'blockSize': 4096, 'createTime': '2024-03-30T15:48:37Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.sqldb.136', 'lastAccessTime': '2024-05-31T17:03:28Z', 'lastAccessTimeIO': '2024-05-31T17:03:28Z', 'minFifoSize': 0, 'name': 'sqldb', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 100}, 'qosPolicyID': 1, 'scsiEUIDeviceID': '7763776200000088f47acc0100000000', 'scsiNAADeviceID': '6f47acc1000000007763776200000088', 'sliceCount': 1, 'status': 'active', 'totalSize': 5000658944, 'volumeAccessGroups': [4], 'volumeConsistencyGroupUUID': '037c2c49-d6cc-4a0b-9b82-4cb287634c33', 'volumeID': 136, 'volumePairs': [], 'volumeUUID': '52707066-3f85-44a6-a2a2-ebb8e7bc0ba0'}, {'access': {}, 'accountID': 11, 'attributes': {'docker-name': 'pvc-d793176f-2484-48ea-9255-f70215a7c5f7', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0-custom+unknown","backendUUID":"b3680925-a9c1-4552-a1b4-1e4a0a273e8e","platform":"","platformVersion":"","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-04-09T07:46:53Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-d793176f-2484-48ea-9255-f70215a7c5f7.139', 'minFifoSize': 0, 'name': 'pvc-d793176f-2484-48ea-9255-f70215a7c5f7', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 100}, 'qosPolicyID': 1, 'scsiEUIDeviceID': '776377620000008bf47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000008b', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': '780a6da0-39f3-4c79-ad86-45b8fcfd1c86', 'volumeID': 139, 'volumePairs': [], 'volumeUUID': '189a81ed-1916-4a04-9842-5f65892db894'}, {'access': {}, 'accountID': 11, 'attributes': {'docker-name': 'pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1', 'fstype': 'xfs', 'provisioning': '', 'trident': '{"version":"24.02.0-custom+unknown","backendUUID":"b3680925-a9c1-4552-a1b4-1e4a0a273e8e","platform":"","platformVersion":"","plugin":"solidfire-san"}'}, 'blockSize': 4096, 'createTime': '2024-06-01T10:10:44Z', 'currentProtectionScheme': {}, 'deleteTime': '', 'enable512e': True, 'enableSnapMirrorReplication': False, 'fifoSize': 5, 'iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1.157', 'minFifoSize': 0, 'name': 'pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1', 'purgeTime': '', 'qos': {'burstIOPS': 1000, 'burstTime': 60, 'curve': {'1048576': 15000, '131072': 1950, '16384': 270, '262144': 3900, '32768': 500, '4096': 100, '524288': 7600, '65536': 1000, '8192': 160}, 'maxIOPS': 800, 'minIOPS': 601}, 'scsiEUIDeviceID': '776377620000009df47acc0100000000', 'scsiNAADeviceID': '6f47acc100000000776377620000009d', 'sliceCount': 1, 'status': 'active', 'totalSize': 2147483648, 'volumeAccessGroups': [], 'volumeConsistencyGroupUUID': 'd3b1189e-6952-4f3b-a6be-37bc8a20896f', 'volumeID': 157, 'volumePairs': [], 'volumeUUID': '92b542f8-0877-4ccb-9ad2-e78bd17a88b4'}]}

# tridentctl get volumes -o json -n trident | jq .items
# some KVs have been dropped for brevity
tv_json = '''[
  {
    "name": "pvc-14a51322-16c8-4b95-a7e4-28d9963450b3",
    "internalName": "pvc-14a51322-16c8-4b95-a7e4-28d9963450b3",
    "backend": "",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "state": "",
    "accessInformation": {
      "iscsiTargetPortal": "192.168.105.30:3260",
      "iscsiTargetIqn": "iqn.2010-01.com.solidfire:wcwb.pvc-14a51322-16c8-4b95-a7e4-28d9963450b3.112",
      "iscsiInterface": "default",
      "iscsiUsername": "tridentk2"
    }
  },
  {
    "name": "pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c",
    "internalName": "pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c",
    "backend": "",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "state": "",
    "accessInformation": {
      "iscsiTargetPortal": "192.168.105.30:3260",
      "iscsiTargetIqn": "iqn.2010-01.com.solidfire:wcwb.pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c.113",
      "iscsiInterface": "default",
      "iscsiUsername": "tridentk2"
    }
  },
  {
    "name": "pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1",
    "internalName": "pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1",
    "backend": "",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "state": "",
    "accessInformation": {
      "iscsiTargetPortal": "192.168.105.30:3260",
      "iscsiTargetIqn": "iqn.2010-01.com.solidfire:wcwb.pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1.157",
      "iscsiInterface": "default",
      "iscsiUsername": "tridentk2"
    }
  },
  {
    "name": "pvc-d793176f-2484-48ea-9255-f70215a7c5f7",
    "internalName": "pvc-d793176f-2484-48ea-9255-f70215a7c5f7",
    "backend": "",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "state": "",
    "accessInformation": {
      "iscsiTargetPortal": "192.168.105.30:3260",
      "iscsiTargetIqn": "iqn.2010-01.com.solidfire:wcwb.pvc-d793176f-2484-48ea-9255-f70215a7c5f7.139",
      "iscsiInterface": "default",
      "iscsiUsername": "tridentk2"
    }
  },
  {
    "name": "pvc-fec78b61-a216-4825-a709-a24069cfadc7",
    "internalName": "velero-vol-136-202404090816z",
    "backend": "",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "state": "",
    "accessInformation": {
      "iscsiTargetPortal": "192.168.105.30:3260",
      "iscsiTargetIqn": "iqn.2010-01.com.solidfire:wcwb.velero-vol-136-202404090816z.140",
      "iscsiInterface": "default",
      "iscsiUsername": "tridentk2"
    }
  }
]'''

# tridentctl get backend -o json -n trident | jq .items 
# some KVs have been dropped for brevity
tb_json = '''[
  {
    "name": "solidfire_192.168.105.30",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "EndPoint": "https://<REDACTED>@192.168.1.30/json-rpc/11.0",
    "tenantName": "tridentk2",
    "state": "online",
    "online": true,
    "userState": "normal",
    "stateReason": null,
    "volumes": "pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1"
  },
  {
    "name": "solidfire_192.168.105.30",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "EndPoint": "https://<REDACTED>@192.168.1.30/json-rpc/11.0",
    "tenantName": "tridentk2",
    "state": "online",
    "online": true,
    "userState": "normal",
    "stateReason": null,
    "volumes": "pvc-14a51322-16c8-4b95-a7e4-28d9963450b3"
  },
  {
    "name": "solidfire_192.168.105.30",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "EndPoint": "https://<REDACTED>@192.168.1.30/json-rpc/11.0",
    "tenantName": "tridentk2",
    "state": "online",
    "online": true,
    "userState": "normal",
    "stateReason": null,
    "volumes": "pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c"
  },
  {
    "name": "solidfire_192.168.105.30",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "EndPoint": "https://<REDACTED>@192.168.1.30/json-rpc/11.0",
    "tenantName": "tridentk2",
    "state": "online",
    "online": true,
    "userState": "normal",
    "stateReason": null,
    "volumes": "pvc-d793176f-2484-48ea-9255-f70215a7c5f7"
  },
  {
    "name": "solidfire_192.168.105.30",
    "backendUUID": "b3680925-a9c1-4552-a1b4-1e4a0a273e8e",
    "EndPoint": "https://<REDACTED>@192.168.1.30/json-rpc/11.0",
    "tenantName": "tridentk2",
    "state": "online",
    "online": true,
    "userState": "normal",
    "stateReason": null,
    "volumes": "pvc-fec78b61-a216-4825-a709-a24069cfadc7"
  }
]
'''


def trident_to_solidfire():
    tv = json.loads(tv_json)
    tb = json.loads(tb_json)
    ksd_list = []
    for t_vol in tv:
        for s_vol in sv['volumes']:
            if t_vol['internalName'] == s_vol['name']:
                print("Found match:", t_vol['internalName'])
                ksd = {k: v for k, v in t_vol.items() if k in ['name', 'internalName', 'accessInformation']}
                ksd['sf_vol_id'] = s_vol['volumeID']
                ksd['sf_vol_name'] = s_vol['name']
                ksd['sf_iqn'] = s_vol['iqn']
                ksd['sf_fifo_min'] = s_vol['minFifoSize']
                ksd['sf_fifo'] = s_vol['fifoSize']
                ksd['sf_size'] = s_vol['totalSize']
                # for sf_account, we could call GetAccountByID to get the account name from ID, but that response contains Trident account's initiatorSecret and targetSecret. 
                # this demo script keeps it simple and sticks to account ID without account names.
                ksd['sf_account'] = s_vol['accountID']
                # add other properties if needed
                ksd_list.append(ksd)
                break
    return ksd_list


def cli_output(ksd_list):    
    print("\nKubernetes to SolidFire storage mapping\n")
    for vol in ksd_list:
        print(f"\nVolume: {vol['name']}\n")        
        pprint.pp(vol,indent=4)


def main():
    ksd_list = trident_to_solidfire()
    cli_output(ksd_list)
    # use ksd_list information to set up replication, QoS, storage-side snapshots, SolidFire's backup-to-S3, etc.
main()


# Output with above JSON data. 
# In real life we'd probably send this to our observability/logging platform or SFC (https://scaleoutsean.github.io/2024/05/29/sfc-v2.html) and observe/alert with Grafana or Kibana
'''
Found match: pvc-14a51322-16c8-4b95-a7e4-28d9963450b3
Found match: pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c
Found match: pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1
Found match: pvc-d793176f-2484-48ea-9255-f70215a7c5f7

Kubernetes to SolidFire storage mapping


Volume: pvc-14a51322-16c8-4b95-a7e4-28d9963450b3

{   'name': 'pvc-14a51322-16c8-4b95-a7e4-28d9963450b3',
    'internalName': 'pvc-14a51322-16c8-4b95-a7e4-28d9963450b3',
    'accessInformation': {   'iscsiTargetPortal': '192.168.105.30:3260',
                             'iscsiTargetIqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-14a51322-16c8-4b95-a7e4-28d9963450b3.112',
                             'iscsiInterface': 'default',
                             'iscsiUsername': 'tridentk2'},
    'sf_vol_id': 112,
    'sf_vol_name': 'pvc-14a51322-16c8-4b95-a7e4-28d9963450b3',
    'sf_iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-14a51322-16c8-4b95-a7e4-28d9963450b3.112',
    'sf_fifo_min': 0,
    'sf_fifo': 5,
    'sf_size': 2147483648,
    'sf_account': 11}

Volume: pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c

{   'name': 'pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c',
    'internalName': 'pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c',
    'accessInformation': {   'iscsiTargetPortal': '192.168.105.30:3260',
                             'iscsiTargetIqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c.113',
                             'iscsiInterface': 'default',
                             'iscsiUsername': 'tridentk2'},
    'sf_vol_id': 113,
    'sf_vol_name': 'pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c',
    'sf_iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-4fb5d7f5-4d98-429e-ab36-1b2118b7e55c.113',
    'sf_fifo_min': 0,
    'sf_fifo': 5,
    'sf_size': 2147483648,
    'sf_account': 11}

Volume: pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1

{   'name': 'pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1',
    'internalName': 'pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1',
    'accessInformation': {   'iscsiTargetPortal': '192.168.105.30:3260',
                             'iscsiTargetIqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1.157',
                             'iscsiInterface': 'default',
                             'iscsiUsername': 'tridentk2'},
    'sf_vol_id': 157,
    'sf_vol_name': 'pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1',
    'sf_iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-a5f21571-e002-493f-b2dc-df01f40c1fa1.157',
    'sf_fifo_min': 0,
    'sf_fifo': 5,
    'sf_size': 2147483648,
    'sf_account': 11}

Volume: pvc-d793176f-2484-48ea-9255-f70215a7c5f7

{   'name': 'pvc-d793176f-2484-48ea-9255-f70215a7c5f7',
    'internalName': 'pvc-d793176f-2484-48ea-9255-f70215a7c5f7',
    'accessInformation': {   'iscsiTargetPortal': '192.168.105.30:3260',
                             'iscsiTargetIqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-d793176f-2484-48ea-9255-f70215a7c5f7.139',
                             'iscsiInterface': 'default',
                             'iscsiUsername': 'tridentk2'},
    'sf_vol_id': 139,
    'sf_vol_name': 'pvc-d793176f-2484-48ea-9255-f70215a7c5f7',
    'sf_iqn': 'iqn.2010-01.com.solidfire:wcwb.pvc-d793176f-2484-48ea-9255-f70215a7c5f7.139',
    'sf_fifo_min': 0,
    'sf_fifo': 5,
    'sf_size': 2147483648,
    'sf_account': 11}
'''