from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)  #定义类型，字符串，最长255
    img_url = models.URLField() #类型，网址
    rate = models.IntegerField()  #类型，数字
