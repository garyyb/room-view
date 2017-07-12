from django.contrib import admin

from .models import Lesson, Building, Room

admin.site.register(Lesson)
admin.site.register(Building)
admin.site.register(Room)
