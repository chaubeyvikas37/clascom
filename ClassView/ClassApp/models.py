from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    fname = models.CharField(max_length=50)


