from django import forms

from .models import Contact_admin

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_admin
        fields = (
            'title',
            'email',
            'description',
          
           
        )
        widgets= {
            'description':forms.Textarea(attrs={'placeholder':'Write your problem','rows':4, 'cols':10}),
        }


class Contact_seen(forms.ModelForm):
    class Meta:
        model = Contact_admin
        fields = (
            'active',
        )
        widgets = {'active': forms.HiddenInput()}
