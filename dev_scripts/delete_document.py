import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="96fb482b-5536-4c86-883a-f317260ed77b",
    password="qYcIYWgIBfFT"
)

delete_doc = discovery.delete_document('d597b7e4-3b37-4886-b950-cb1271dc4d96', '68870f75-195a-4695-96d3-537951f77a92', '354af21a-cc94-4673-8ce9-55817a155125')
print(json.dumps(delete_doc, indent=2))
