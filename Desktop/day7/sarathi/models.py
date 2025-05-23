from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=45)
    roll_no=models.IntegerField()
    email=models.EmailField()
    

    def __str__(self):
        return self.name


class Biodata(models.Model):
    dept=models.CharField(max_length=40)
    age=models.IntegerField()
    gender=models.CharField(max_length=40)
    mobile_no=models.IntegerField()
    stream=models.CharField(max_length=40)

