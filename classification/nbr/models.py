from django.db import models

class Hello(models.Model):
    pic=models.ImageField(upload_to='prfiles')
class Pest(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    about=models.TextField()
    precautions=models.TextField()
    safty=models.TextField()
