from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    title = models.CharField(max_length=500)
    completed = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.title