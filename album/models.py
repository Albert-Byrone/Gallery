from django.db import models
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        return Location.objects.all()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name=value)

    def __str__(self):
        return self.name

class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    

class Image(models.Model):
    name = models.CharField(max_length = 60)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=id).all()
        return image


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name

    