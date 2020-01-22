from django.db import models
import os,random
from datetime import datetime, timedelta
from .utils import unique_slug_generator
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

    return 'browser/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)




class Category_post(models.Model):
    c_title         = models.CharField(max_length=120)
    slug            = models.SlugField(unique=True,blank=True,null=True)
    image           = models.ImageField(upload_to=upload_image_path, null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.c_title

    def get_absolute_url(self):
        return reverse("browse:category", kwargs={"slug": self.slug})
    







class Product(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='DO_NOTHING')
    p_category              = models.ForeignKey(Category_post,on_delete='DO_NOTHING',verbose_name="Category")
    title                   = models.CharField(max_length=120,verbose_name="Title",unique=True)
    # day                     = models.DateTimeField(blank=True, null=True)
    slug                    = models.SlugField(unique=True,blank=True)
    description             = models.TextField(verbose_name="Description")
    price                   = models.DecimalField(decimal_places=2, max_digits=10,default=33.33,verbose_name="Market Price")
    stating_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33,verbose_name="Starter Price")
    # current_price           = models.DecimalField(decimal_places=2, max_digits=10,default=33.33)

    image                   = models.ImageField(upload_to=upload_image_path, verbose_name="Image")
    featured                = models.BooleanField(default=False)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True,editable=True)
    end_date                = models.DateTimeField(default=datetime.now()+timedelta(days=5),null=True,blank=True)


    



   


   

    # def get_absolute_url(self):
    #     return reverse("product_detail", kwargs={"slug": self.slug})
    
    def get_absolute_url(self):
        return reverse("browse:item_detail", kwargs={"slug": self.slug})

    def get_admin_absolute_url(self):
        return reverse("nilam_admin:product_detail", kwargs={"slug":self.slug})

    def win_get_absolute_url(self):
        return reverse("nilam_admin:bid_win_loss", kwargs={"slug": self.slug})
    

    def days_left(self):
        return (self.end_date.date() - date.today()).days

    def item_post(self):
        a = self.days_left()
        a = int(a)
        # b = False
        if a>0 :
            return True
        return False
    

    def __str__(self):
        return self.title

        ############ Ending Product Section ################



    


    ######## Starting Product Price Section ##########
class Product_price(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='DO_NOTHING', null=True, blank=True, default=1)
    product_title           = models.ForeignKey(Product,on_delete='DO_NOTHING',null=True,blank=True)
    bid_price               = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    
    current_price           = models.DecimalField(decimal_places=2, max_digits=10,null=True,blank=True)
    timestamp               = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_title)

    def get_absolute_url(self):
        return Product.get_absolute_url(self.product_title)

    def admin_bid_abosolute_url(self):
        return reverse("nilam_admin:bid_detail", kwargs={"pk":self.pk})
    


# def product_price_postsave(sender,created,instance,*args,**kwargs):
#     if  created:
#         current_price=instance.current_price
        
#         current_price = 400.00
#         instance.save()
        
# post_save.connect(product_price_postsave,sender=Product_price)


def category_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify('category-' + instance.c_title)
pre_save.connect(category_presave_receiver,sender=Category_post)



   



def product_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_presave_receiver,sender=Product)




