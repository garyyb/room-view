from django.template.response import TemplateResponse
from django.http import JsonResponse

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
            'code'       : 'TEST1234',
            'start_time' : '12:00',
            'end_time'   : '15:00',
            'type'       : 'Lecture',
            'day'        : 'Monday'
        },
        {
            'location': 'test_location 103',
            'code': 'MATH0000',
            'start_time': '09:00',
            'end_time': '10:00',
            'type': 'Tutorial',
            'day': 'Tuesday'
        }
        ]
    }

    return JsonResponse(data)