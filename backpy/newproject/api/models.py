from django.db import models

# Create your models here.
class user(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
        print(user)