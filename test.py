# -*- coding: utf-8 -*-
import pandas as pd
import polyglot
import pprint
from locationEntityMatch import getEntityLocation
from polyglot_location_analysis import getPolyglotLocation, getLocation

polyglotLocation = getLocation("डिस्ट्रिक्ट कौशांबी उत्तर प्रदेश")

instance = polyglotLocation
curloc = []
for entity in instance:
    curloc.append(getEntityLocation(entity))
loc = curloc

print("====================")
print(loc)