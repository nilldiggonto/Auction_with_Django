from django import forms

from .models import Billing_profile

# class DateInput(forms.DateInput):
#     input_type = 'date'

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing_profile
        fields = (
            'bil_address',
            'city',
            'bil_zip',
            
            'phone',
            'nid'
            
           
        )