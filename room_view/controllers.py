from django.template.response import TemplateResponse
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse

import datetime
import math
from .models import Lesson, Room, Building

def index(request):
    return TemplateResponse(request, 'index.html', {})

def location(request, id):
    # TODO: Get timetable for the location.

    data = \
    {
        'location' : 'Test Building 1 Room 1',
        'free_periods' : \
        [
            (datetime.time(9), datetime.time(12)),
            (datetime.time(13, 30), datetime.time(15)),
            (datetime.time(17), datetime.time(0))
        ],
        'id' : id
    }

    return TemplateResponse(request, 'location.html', data)

################
# AJAX Queries #
################

# Return data for currently free rooms.
def free_now(request):
    # TODO: Implement (ie, dynamically generate the 'data' dictionary below)
    # TODO: Remove test data.

    data = {
            'num_classes'   : 0,
            'classes'       : [],

            }
    L = Lesson.objects.all()
    for l in L:
        if (l.happening_now()): 
            data['num_classes']+=1
            temp = {
                    'id'        : l.pk,
                    'location'  : str(l.location),
                    'start_time': l.start_time,
                    'end_time'  : l.end_time,
            }
            data['classes'].append(temp)

    # Everything after this should be fine.
    data_type = request.META['HTTP_ACCEPT'].split(',')[0]

    if data_type == 'application/json':
        return JsonResponse(data)
    elif data_type == 'application/text':
        return HttpResponse(str(data))
    else:
        return HttpResponse(status=400)

def room_query(request):
    # TODO: Implement the other request headers (building, duration, etc)
    lt = timezone.localtime(timezone.now())
    try:
        query  = request.GET.__getitem__('building').split(',')
        start_time = datetime.time(int(request.GET.__getitem__('hour')),int(request.GET.__getitem__('minute')))
        start_date = datetime.datetime.combine(lt,start_time)
        duration = datetime.timedelta(hours=int(request.GET.__getitem__('duration')))
    except KeyError:
        return HttpResponse(400)
    
    data = {
            'num_classes'   : 0,
            'classes'       : [],
            }

    for location in query:
        for room in Room.objects.filter(building__name=location):
            print(room)
            isFree = True
            nextLesson = None

            for lesson in room.lesson_set.all():
                if lesson.compare_day(start_date) == False: continue
                if lesson.is_happening(start_date):
                    isFree = False 
                    break
                #Keep track of the next lesson starting in the room
                if lesson.end_time >= start_time:
                    if nextLesson == None:
                        nextLesson = lesson
                    else:
                        if lesson.start_time < nextLesson.start_time:
                            nextLesson = lesson
            if isFree:
                st = datetime.time(23,59)
                if (nextLesson != None):
                    st = nextLesson.start_time
                
                timeDiff = datetime.datetime.combine(datetime.datetime.min,st) - datetime.datetime.combine(datetime.datetime.min, start_time)
                timeAvailable = datetime.time(math.floor(timeDiff.seconds/3600),math.floor((timeDiff.seconds%3600)/60))
    
                if (timeDiff < duration): continue
                data['num_classes']+=1
                temp = {
                        'id'        : room.pk,
                        'location'  : str(room),
                        'start_time': st,
                        'end_time'  : timeAvailable, 
                }
                data['classes'].append(temp)


    data_type = request.META['HTTP_ACCEPT'].split(',')[0]

    if data_type == 'application/json':
        return JsonResponse(data)
    elif data_type == 'application/text':
        return HttpResponse(str(data))
    else:
        return HttpResponse(status=400)

def enough_time_available(tA, tR):
    return datetime.combine(date.min, tA) > datetime.combine
