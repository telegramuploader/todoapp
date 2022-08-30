from urllib import request
from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='User'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.user_id)

class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return self.name
