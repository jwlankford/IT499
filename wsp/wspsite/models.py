from django.db import models

class OrderData(models.Model):
   responsibleParty = models.CharField(max_length=200)
   cases = models.CharField(max_length=200)

   def __str__(self):
       return f'{self.responsibleParty} : {self.cases}'
