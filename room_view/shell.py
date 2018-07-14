from .models import Lesson, Room, Building
from django.utils import timezone
import sys 

b = Building.objects.get(pk=1)
print(b)

