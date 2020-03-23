# -*- coding: utf-8 -*-
import pandas as pd
import polyglot
import pprint
from locationEntityMatch import getEntityLocation
from polyglot_location_analysis import getPolyglotLocation, getLocation

filename = "dataset.csv"
transcriptdf = pd.read_csv(filename)
del transcriptdf['locations']
transcript = transcriptdf["Transcript"].tolist()

n = len(transcript)
polyglotLocation = [None]*n
for i in range(n):
    instance = transcript[i]
    polyglotLocation[i] = getLocation(instance) #prints location identified as well
    print("====================")

outdf = pd.DataFrame(polyglotLocation, transcript[:n])
outdf.to_csv('polyglotLocation.csv')

loc = [None]*n
for i in range(n):
    instance = polyglotLocation[i]
    curloc = []
    for entity in instance:
        curloc.append(getEntityLocation(entity))
    loc[i] = curloc

print("====================")
print(loc)

outdf = pd.DataFrame(loc, transcript[:n])
print(outdf)
outdf.insert(0,"polyglot",polyglotLocation)
print(outdf)

outdf.to_csv('matchedLocation.csv')



########################################################################


polyglotLocation = getLocation(instance) #prints location identified as well
instance = polyglotLocation
curloc = []
# for entity in instance:
#     curloc.append(getEntityLocation(entity))
# loc = curloc
# return loc
