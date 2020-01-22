from django.db import models
import os,random
from datetime import datetime, timedelta
from browser.utils import unique_slug_generator
from  django.db.models.signals import pre_save,post_save
from django.urls import reverse
from django.conf import settings
import math
from datetime import date
from django.utils.text import  slugify
# Create your models here.


#Recreating default file name and path
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext  = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,2141512411)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)

    return 'slider/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)



class Nilam_slider(models.Model):
    title                   = models.CharField(max_length=50,verbose_name="Title")
    # day                     = models.DateTimeField(blank=True, null=True)
    slug                    = models.SlugField(unique=True,blank=True,editable=False)
    description             = models.CharField(max_length=120)
    # current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)

    image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image")
    featured                = models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True,editable=True)


    def __str__(self):
        return self.title



class Nilam_info_section(models.Model):
    title                   = models.CharField(max_length=50,verbose_name="Title")
    # day                     = models.DateTimeField(blank=True, null=True)
    #slug                    = models.SlugField(unique=True,blank=True,editable=False)
    #description             = models.CharField(max_length=120)
    # current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)

    image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image")
    #featured                = models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True,editable=True)


    def __str__(self):
        return self.title



class Nilam_footer_section(models.Model):
    title                   = models.CharField(max_length=50,verbose_name="Title")
    # day                     = models.DateTimeField(blank=True, null=True)
    #slug                    = models.SlugField(unique=True,blank=True,editable=False)
    #description             = models.CharField(max_length=120)
    # current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)

    image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image")
    #featured                = models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True,editable=True)


    def __str__(self):
        return self.title



class Nilam_regular_rule(models.Model):
    title                   = models.CharField(max_length=50,verbose_name="Title")
    # day                     = models.DateTimeField(blank=True, null=True)
    #slug                    = models.SlugField(unique=True,blank=True,editable=False)
    description             = models.TextField()
    # current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)

    # image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image")
    #featured                = models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True,editable=True)


    def __str__(self):
        return self.title






class Nilam_live_rule(models.Model):
    title                   = models.CharField(max_length=50,verbose_name="Title")
    # day                     = models.DateTimeField(blank=True, null=True)
    #slug                    = models.SlugField(unique=True,blank=True,editable=False)
    description             = models.TextField()
    # current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)

    # image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image")
    #featured                = models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True,editable=True)


    def __str__(self):
        return self.title




def slider_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slider_presave_receiver,sender=Nilam_slider)
    

    

    

