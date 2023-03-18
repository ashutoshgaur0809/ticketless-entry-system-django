from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    uemail = models.EmailField(max_length=255)
    upass = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name