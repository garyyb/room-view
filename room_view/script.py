from .models import Building, Room, Lesson
import json


buildings = []
rooms = set()


with open('buildings') as d:
    blds = d.readlines()
    #add buildings
    for s in blds:
        s = s.rstrip()
        b = Building(name=s)
        b.save()

with open('data.json') as d:
    data = json.load(d)
    #add rooms
    for i, entry in enumerate(data):
        name = entry["bld."] + entry["room"]
        if (name not in rooms):
            b = Building.objects.get(name=entry["bld."])
            room_name = entry["room"].lstrip(' ').replace('  ',' ')
            r = b.room_set.create(room_id=room_name)
            rooms.add(name)
            r.save()

    print("hi")
    #add lesson
    for entry in data:
        room_name = entry["room"].lstrip(' ').replace('  ',' ')
        #Filter through all rooms with that room name
        tmp = Room.objects.filter(room_id=room_name)
        print("Adding: " + entry["code"]);
        for rm in tmp:
            if (rm.building.name == entry["bld."]): r = rm 
            #Add the lesson to the room
            l = r.lesson_set.create(code=entry["code"],start_time=entry["start"],end_time=entry["end"],type=entry["type"],day=entry["day"])
            l.save()


        
