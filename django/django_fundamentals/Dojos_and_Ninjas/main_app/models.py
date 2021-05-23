from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255,default="old dojo")

class Ninja(models.Model):
    dojo=models.ForeignKey(Dojo,related_name="dojos",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

def dojos_obj():
    dojos = Dojo.objects.all()
    return dojos

def Ninjas_obj():
    ninjas = Ninja.objects.all()
    return ninjas

def create_dojo(input):
    new_dojo=Dojo.objects.create(name=input['name'],city=input['city'],state=input['state'])
    return new_dojo

def create_ninja(input):
    new_ninja = Ninja.objects.create(dojo=Dojo.objects.get(name=input['dojo']),first_name=input['fname'],last_name=input['lname'])
    return new_ninja