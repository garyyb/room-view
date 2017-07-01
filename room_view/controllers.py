from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.http import HttpResponse

def index(request):
    return TemplateResponse(request, 'index.html', {})

# Return data for currently free rooms.
def free_now(request):
    # TODO: Implement (ie, dynamically generate the 'data' dictionary below)
    # TODO: Remove test data.

    data = \
    {
        'num_classes' : 2,
        'classes'     : \
        [
        {
            'location'   : 'test_location G01',
            'start_time' : '12:00',
            'end_time'   : '15:00',
        },
        {
            'location': 'test_location 103',
            'start_time': '09:00',
            'end_time': '10:00',
        }
        ]
    }

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

    data = \
        {
            'num_classes': 2,
            'classes': \
                [
                    {
                        'location': 'Test Building 1 Room 1',
                        'start_time': '12:00',
                        'end_time': '15:00',
                    },
                    {
                        'location': 'Test Building 1 Room 2',
                        'start_time': '09:00',
                        'end_time': '10:00',
                    }
                ]
        }

    data_type = request.META['HTTP_ACCEPT'].split(',')[0]

    if data_type == 'application/json':
        return JsonResponse(data)
    elif data_type == 'application/text':
        return HttpResponse(str(data))
    else:
        return HttpResponse(status=400)