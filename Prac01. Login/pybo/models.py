from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


    #unique field : 중복허용x
    #signup에서 for문돌려서 확인