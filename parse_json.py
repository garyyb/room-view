import json


locs = set()
tmp = []

with open('classes.json') as data_file:    
    data = json.load(data_file)
    for entry in data:
        tmp.append(entry["loc"])

    for l in tmp:
        s = ' '.join(l.split(' ')[:-2])
        if (s not in locs):
            print(s)
            locs.add(s)
            #for entry in data:
            #    if s in entry["loc"]:
            #        room = entry["loc"].replace(s,"")
            #        entry["room"] = room
            #        entry["bld."] = s
            #        print(entry)
            #break



