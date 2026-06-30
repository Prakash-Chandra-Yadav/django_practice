from django.db import models


# Create your models here.
class message(models.Model):
    text = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return self.text
