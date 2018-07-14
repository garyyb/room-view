import json
import sys


locs = set()
tmp = []

with open('tmp.json') as data_file:    
    data = json.load(data_file)

    with open('blds') as idk:
        blds = idk.readlines()
        for s in blds:
            s = s.rstrip()
            for entry in data:
                if s in entry["loc"]:
                    room = entry["loc"].replace(s,"")
                    entry["room"] = room
                    entry["bld."] = s
                    print(entry)
                    data.remove(entry)



