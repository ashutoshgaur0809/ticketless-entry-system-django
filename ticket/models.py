from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    uemail = models.EmailField(max_length=255)
    upass = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name
    
# Create your models here.
class Booking(models.Model):
    id=models.AutoField(primary_key=True)
    placename = models.CharField(max_length=255)
    number_of_visitors = models.IntegerField(max_length=255)
    time_slot = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.placename