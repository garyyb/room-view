
import sys
import json

s = set() 
with open('tmp.json') as data_file:    
        data = json.load(data_file)
        for l in data:
            s.add(l['loc'])
        for b in s:
            print(b)

