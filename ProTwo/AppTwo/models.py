from django.db import models

# Create your models here.
class UserInfo(models.Model):
    fname = models.CharField(max_length=264)
    lname = models.CharField(max_length=264)
    email = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
