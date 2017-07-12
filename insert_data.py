import json, datetime, sqlite3

with open("classes.json", 'r') as fp:
    data = json.load(fp)
    conn = sqlite3.connect("db.sqlite3")



    sql = ''' INSERT INTO room_view_building('name')
      VALUES(?) '''
    row = ["Matthews"]
    cur.execute(sql, row)

 
    sql = ''' INSERT INTO room_view_room('room')
      VALUES(?) '''
    for key, entry in enumerate(data):
        if (entry['loc'][:9] != "Matthews Theatr"[:9]): continue
        room_entry = [1,entry[]
    cur = conn.cursor()
    # print(cur.fetchall())
    print(cur.description)
    for key, entry in enumerate(data):
        """
        new_entry = {
            'model' : 'room_view.lesson',
            'pk'    : key,
            'fields': {
                'location'   : entry['loc'],
                'code'       : entry['code'],
                'start_time' : datetime.time(int(entry['start'].split(':')[0]), int(entry['start'].split(':')[1])),
                'end_time'   : datetime.time(int(entry['end'].split(':')[0]), int(entry['end'].split(':')[1])),
                'type'       : entry['type'],
                'day'        : entry['day']
            }
        }
        """
        lesson_entry = [entry['loc'], entry['code'],
               entry['start'], entry['end'],
               entry['type'], entry['day']]

        cur.execute(sql, row)

    conn.commit()
