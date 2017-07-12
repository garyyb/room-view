from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.http import HttpResponse

import datetime
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
        ]
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
        if (l.is_in_use()): 
            data['num_classes']+=1
            temp = {
                    'id'        : l.pk,
                    'location'  : l.code,
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
    # TODO: Implement (ie, dynamically generate the 'data' dictionary below)
    # TODO: Remove test data.
    try:
        query = request.GET.__getitem__('query')
    except KeyError:
        return HttpResponse(400)
    
    data = {
            'num_classes'   : 0,
            'classes'       : [],
            }

    for room in Room.objects.filter(building__name__startswith=query):
        for lesson in Lesson.objects.filter(location__room_id=room.room_id):
            data['num_classes']+=1
            temp = {
                    'id'        : lesson.pk,
                    'location'  : lesson.code,
                    'start_time': lesson.start_time,
                    'end_time'  : lesson.end_time,
            }
            data['classes'].append(temp)


    data_type = request.META['HTTP_ACCEPT'].split(',')[0]

    if data_type == 'application/json':
        return JsonResponse(data)
    elif data_type == 'application/text':
        return HttpResponse(str(data))
    else:
        return HttpResponse(status=400)
