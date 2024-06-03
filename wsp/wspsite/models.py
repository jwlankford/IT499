from django.db import models

class ScrapedData(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)