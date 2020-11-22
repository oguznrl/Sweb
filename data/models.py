from django.db import models

class NumberofData(models.Model):
    posted=models.IntegerField()
    login=models.IntegerField()
    users=models.CharField(max_length=50)
  