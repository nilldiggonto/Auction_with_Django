from django.db import models
from django.conf import settings
from django.urls import reverse
from browser.utils import unique_slug_generator
from  django.db.models.signals import pre_save,post_save
from django.utils.text import  slugify
# Create your models here.


class Contact_admin(models.Model):
    # user                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='DO_NOTHING')
    title                   = models.CharField(max_length=120)
    email                   = models.EmailField()
    
    description             = models.TextField()
    slug                    = models.SlugField(unique=True,blank=True,null=True)
    active                  = models.BooleanField(default=False)
    
    timestamp               = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("nilam_admin:detail", kwargs={"slug": self.slug})
    



def contact_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(contact_presave_receiver,sender=Contact_admin)

    
    
    
