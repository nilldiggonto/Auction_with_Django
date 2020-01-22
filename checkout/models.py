from django.db import models
from django.conf import settings
from browser.models import Product
# Create your models here.
class CheckouSystem(models.Model):
    user        = models.CharField(max_length=15,blank=True,null=True)
    p_name      = models.CharField(max_length=120,null=True,blank=True)
    email       = models.EmailField()
    address     = models.CharField(max_length=120)
    city        = models.CharField( max_length=50)
    phone       = models.CharField(max_length=14)
    zip_c       = models.IntegerField()
    card_name   = models.CharField(max_length=120)
    card_no     = models.IntegerField()
    active      = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.p_name)

        
    



