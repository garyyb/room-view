from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.http import HttpResponse

def index(request):
    return TemplateResponse(request, 'index.html', {})

# Return data for currently free rooms.
def free_now(request):
    # TODO: Implement
    # TODO: Remove test response.

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

    try:
        data_type = request.GET.__getitem__('dataType')
    except KeyError:
        return HttpResponse(status=400)

    if data_type == 'json':
        return JsonResponse(data)
    elif data_type == 'text':
        return HttpResponse(str(data))
    else:
        return HttpResponse(status=400)
