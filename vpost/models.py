from django.db import models

class Vpost(models.Model):
    text=models.TextField()
    cover=models.ImageField(upload_to='post_pic/')
    def __str__(self):
        return self.text