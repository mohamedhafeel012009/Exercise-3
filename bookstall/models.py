from django.db import models

class student(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    author=models.CharField(max_length=100)

def __str__(self):
    return self.title