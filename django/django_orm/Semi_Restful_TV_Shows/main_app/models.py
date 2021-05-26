from django.db import models

# Create your models here.

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog description should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=225)
    network = models.CharField(max_length=225)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

def all_shows():
    all_shows  = Show.objects.all()
    return all_shows

def add_shows(title,network,release_date,desc):
    new_show = Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
    return new_show.id

def get_show(id):
    show = Show.objects.get(id=id)
    return show

def update_show(id,title,network,rd,desc):
    show = Show.objects.get(id=id)
    show.title = title
    show.network = network
    show.release_date = rd
    show.desc = desc
    show.save()

def delete_show(id):
    show = Show.objects.get(id=id)
    show.delete()
    
