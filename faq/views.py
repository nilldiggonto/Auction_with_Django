from django.shortcuts import render,redirect
from .models import Faq,Faq_category
from user_account.forms import  ContactForm
# Create your views here.

def q_a_faq(request):
    f_category = Faq_category.objects.all()
    fa_q       = Faq.objects.all()


    form = ContactForm(request.POST,None)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.user   = request.user
            instance.save()
            return redirect('faq:faq')

       

    template_name = 'faq/q_a.html'
    context = {
        'f_category':f_category,
        'fa_q':fa_q,
        'form':form,
    }
    return render(request,template_name,context)
