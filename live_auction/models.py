from django.db import models
import os,random
from datetime import datetime, timedelta
from browser.utils import unique_slug_generator
from  django.db.models.signals import pre_save,post_save
from django.urls import reverse
from django.conf import settings
import math
global str
from django.utils.text import  slugify
import math
from datetime import date
from browser.models import Category_post
from django.core.exceptions import ValidationError
# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext  = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,2141512411)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)

    return 'live/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)



class ProductLive(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p_category              = models.ForeignKey(Category_post,on_delete=models.CASCADE,verbose_name="Category")
    title                   = models.CharField(max_length=120,verbose_name="Title")
    # day                     = models.DateTimeField(blank=True, null=True)
    slug                    = models.SlugField(unique=True,blank=True,editable=False)
    description             = models.TextField(verbose_name="Description")
    price                   = models.DecimalField(decimal_places=2, max_digits=10,default=33.33,verbose_name="Market Price")
    stating_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33,verbose_name="Starter Price")
    current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)
 
    image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image_1")
    image2                  = models.ImageField(upload_to=upload_image_path, verbose_name="Image_2",null=True,blank=True)
    image3                  = models.ImageField(upload_to=upload_image_path, verbose_name="Image_3",null=True,blank=True)
    image4                  = models.ImageField(upload_to=upload_image_path, verbose_name="Image_4",null=True,blank=True)

    live                    = models.BooleanField(default=True)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True)
    end_date                = models.DateTimeField(default=datetime.now()+timedelta(days=1),null=True,blank=True)

    

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("live:live-detail", kwargs={"slug": self.slug})
    
    def get_admin_absolute_url(self):
        return reverse("nilam_admin:live_detail", kwargs={"slug": self.slug})
    


    def days_left(self):
        return (self.end_date.date() - date.today()).days

    def item_post(self):
        a = self.days_left()
        a = int(a)
        # b = False
        if a>0 :
            return True
        return False
    



class Product_price_live(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=1)
    product_title           = models.ForeignKey(ProductLive,on_delete=models.CASCADE,null=True,blank=True)
    bid_price               = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    
    current_price           = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)
    timestamp               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_title)



    # def clean_current_price(self,*args,**kwargs):
    #     current_price = self.cleaned_data.get('current_price')
    #     current_price = int(current_price)
    #     if current_price > 100:
    #         raise ValidationError("Enter the correct name for this field")
    #     elif current_price < 5:
    #         raise ValidationError("Enter the correct name for this field")

    #     return current_price



    def get_absolute_url(self):
        return ProductLive.get_absolute_url(self.product_title)
        



class Live_second_timer(models.Model):
    live_title              = models.ForeignKey(ProductLive,on_delete=models.CASCADE)
    timestamp               = models.DateTimeField(auto_now_add=True)
    live                    = models.BooleanField(default=False)
    end_timer               =  models.DateTimeField(default=datetime.now()+timedelta(minutes=5),null=True,blank=True)

    def __str__(self):
        return str(self.live_title)


    def get_absolute_url(self):
        return ProductLive.get_absolute_url(self.live_title)
    



def productlive_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(productlive_presave_receiver,sender=ProductLive)
    

    
