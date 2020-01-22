from django import forms

from .models import ProductLive,Product_price_live,Live_second_timer

# class DateInput(forms.DateInput):
#     input_type = 'date'

class LiveForm(forms.ModelForm):
    class Meta:
        model = ProductLive
        fields = (
            'p_category',
            'title',
            'description',
            
            'image',
            'image2',
            'image3',
            'image4',
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

class LiveUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductLive
        fields =(
            'active',
        )
        widgets = {'active': forms.HiddenInput()}



class LiveSecondForm(forms.ModelForm):
    class Meta:
        model = Live_second_timer
        fields =(
            'live',
        )
        widgets = {'live': forms.HiddenInput()}

    # def clean(self):
    #     if 'newsletter_sub' in self.data:





class LiveBidForm(forms.ModelForm):
    # current_price = forms.CharField(label='',max_length=3,widget=forms.NumberInput())

    class Meta:
        model = Product_price_live
        fields = (
            'current_price',
           
        )
        labels = {
            'current_price':(''),
        }
        widgets = {'current_price': forms.HiddenInput()}
        # widgets = {
        #     'current_price': forms.NumberInput(attrs={
                 
        #         'required': True, 
        #         'placeholder': 'Bid your price.',
        #         'minlength': 1,
        #         'maxlength': 2,
                
        #     }),
        #}
    

    