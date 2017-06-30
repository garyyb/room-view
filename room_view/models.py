from django.db import models

class lesson(models.Model):
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
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    )

    location = models.CharField(max_length=128)
    code = models.CharField(max_length=8)
    start_time = models.TimeField()
    end_time = models.TimeField()
    type = models.CharField(choices=TYPE_OPTIONS)
    day = models.CharField(choices=DAY_OPTIONS)
