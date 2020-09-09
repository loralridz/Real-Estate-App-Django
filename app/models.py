from django.db import models
from datetime import datetime
from PIL import Image

# Create your models here.
class Contact(models.Model):

	fname = models.CharField(max_length=200,default="")
	sname = models.CharField(max_length=200,default="")
	email = models.EmailField(max_length=200,default="")
	message = models.TextField()

	def __str__(self):
		return self.fname


class Property(models.Model):

    title = models.CharField(max_length=200,default="")
    address = models.CharField(max_length=200,default="")
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    photo_main = models.ImageField(default='default.jpg', upload_to='property_main_pic')
    photo_1 = models.ImageField(upload_to='property_pics', blank=True)
    photo_2 = models.ImageField(upload_to='property_pics', blank=True)
    photo_3 = models.ImageField(upload_to='property_pics', blank=True)
    photo_4 = models.ImageField(upload_to='property_pics', blank=True)
    photo_5 = models.ImageField(upload_to='property_pics', blank=True)
    is_sold = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

# pip install  pillow

