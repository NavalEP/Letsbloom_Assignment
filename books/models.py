from django.db import models
import datetime

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.title