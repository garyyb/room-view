from django.db import models
from django.utils import timezone
import sys


class Building(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Room(models.Model):
    room_id = models.CharField(max_length=32,default="")
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_id


class Lesson(models.Model):
    TYPE_OPTIONS = (
        ('Clinical', 'Clinical'),
        ('Laboratory', 'Laboratory'),
        ('Lecture', 'Lecture'),
        ('Lecture Sequence 1 of 2', 'Lecture Sequence 1 of 2'),
        ('Lecture Sequence 2 of 2', 'Lecture Sequence 2 of 2'),
        ('Other', 'Other'),
        ('Project', 'Project'),
        ('Seminar', 'Seminar'),
        ('Studio', 'Studio'),
        ('Tutorial', 'Tutorial'),
        ('Tutorial 1 of 2', 'Tutorial 1 of 2'),
        ('Tutorial 2 of 2', 'Tutorial 2 of 2'),
        ('Tutorial-Laboratory', 'Tutorial-Laboratory')
    )

    DAY_OPTIONS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    )

    location = models.ForeignKey(Room)
    code = models.CharField(max_length=8)
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(max_length=32, choices=TYPE_OPTIONS)
    day = models.CharField(max_length=16, choices=DAY_OPTIONS)

    def __str__(self):
        return self.code +" "+ self.day + ": " + str(self.start_time) + "-" + str(self.end_time)


    def is_in_use(self):
        lt = (timezone.localtime(timezone.now()))     
        time = lt.time()
        dayStr = (self.DAY_OPTIONS)[lt.weekday()][0]
        return (dayStr == self.day and self.start_time <= time and time <= self.end_time)


        

