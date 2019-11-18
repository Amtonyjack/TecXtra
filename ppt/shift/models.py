from django.db import models
from django.db.models import Max

class Marks(models.Model):
    DEPT_SEC = models.CharField(max_length=50)
    NAME = models.CharField(max_length=50)
    PRESENTATION = models.IntegerField()
    QUERIES = models.IntegerField()
    COMMUNICATION = models.IntegerField()
    AUDIENCE = models.IntegerField()
    TOTAL =models.IntegerField()

    def __str__(self):
        return self.DEPT_SEC
