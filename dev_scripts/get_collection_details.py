import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="b114f157-15a8-4e7e-8bb3-54a13177d957",
    password="TjKl3OCR63Kq"
)

collection = discovery.get_collection('20b1ffbe-8873-4468-98a0-4d5f5523948d', '21951d44-14fe-4515-9aff-634041b0fe78')
print(json.dumps(collection, indent=2))
