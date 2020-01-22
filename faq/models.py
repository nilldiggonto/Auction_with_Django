from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

from django.urls import reverse
from browser.utils import unique_slug_generator
from  django.db.models.signals import pre_save,post_save

# Create your models here.


class Faq_category(models.Model):
    title                   = models.CharField(max_length=120,verbose_name='category')
    slug                    = models.SlugField(unique=True,blank=True,null=True)
    active                  = models.BooleanField(default=True)
    timestamp               = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)



class Faq(models.Model):
    a_list          = models.ForeignKey(Faq_category,on_delete='DO_NOTHING',null=True,blank=True,verbose_name="faq_category")
    title           = models.CharField(max_length=120,verbose_name='Question')
    slug            = models.SlugField(unique=True,blank=True,null=True)

    answer          = models.TextField()
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)




def faq_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(faq_presave_receiver,sender=Faq)



def faq_cat_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(faq_cat_presave_receiver,sender=Faq_category)