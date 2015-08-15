from django.db import models



class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    text = models.CharField(max_length=50)
    details = models.CharField(max_length=50)

