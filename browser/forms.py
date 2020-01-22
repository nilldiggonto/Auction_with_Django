from django import forms

from .models import Product,Product_price

# class DateInput(forms.DateInput):
#     input_type = 'date'

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'p_category',
            'title',
            'description',
            
            'image',
            'price',
            'stating_price'
           
        )
        widgets= {
            'description':forms.Textarea(attrs={'placeholder':'Describe Your Item as detailed as possible','rows':4, 'cols':10}),
        }
        # widgets = {
        #     'day': DateInput()
        # }
    def clean_description(self,*args,**kwargs):
        description = self.cleaned_data.get('description')
        description_len = len(description)
        if description_len < 150:
            raise forms.ValidationError('Description should be bigger than 150 words')
        

        return description






class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =(
            'active',
        )
        widgets = {'active': forms.HiddenInput()}


class BidForm(forms.ModelForm):
    # current_price = forms.CharField(label='',max_length=3,widget=forms.NumberInput())

    class Meta:
        model = Product_price
        fields = (
            'current_price',
           
        )
        labels = {
            'current_price':(''),
        }
        widgets = {
            'current_price': forms.NumberInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Bid your price.',
                'max_length':3,
            }),
        }

    def clean_current_price(self,*args,**kwargs):
        current_price = self.cleaned_data.get('current_price')
        current_price = int(current_price)
        if current_price > 100:
            raise forms.ValidationError('Can not be more than 100$')
        elif current_price < 5:
            raise forms.ValidationError('Can not be Less than 5$')

        return current_price