from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class Billing_profile(models.Model):

    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete='DO_NOTHING',null=True,blank=True,default=1)
    bil_address = models.CharField(max_length=200)
    city        = models.CharField(max_length=120)
    bil_zip     = models.IntegerField(default=1215)
    phone       = models.CharField(max_length=14,null=True,blank=True)
    nid         = models.BigIntegerField(verbose_name='NID no', default='543')
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.bil_address

    def get_absolute_url(self):
        return reverse("billing:update", kwargs={"id": self.id})

    def get_admin_address_absolute_url(self):
        return reverse("nilam_admin:active_add", kwargs={"id": self.id})
    
    
    
