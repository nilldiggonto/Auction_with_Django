from django.shortcuts import render,get_object_or_404,redirect
from .models import Billing_profile
from django.shortcuts import render,get_object_or_404,redirect
from .forms import BillingForm
from django.contrib.auth.decorators import login_required
from browser.models import Product

# Create your views here.
def billing(request):
    template_name = 'billing/address.html'
    # queryset    = Billing_profile.objects.all()
    form = BillingForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user   = request.user
        instance.save()
        return redirect('billing:address')

    context = {
        'form' : form,
    }
    return render(request,template_name,context)


def billing_address(request):
    template_name = 'billing/address_list.html'
    user = request.user
    billing_query = Billing_profile.objects.filter(user=request.user).filter(active=True).last()
    all_product = Product.objects.filter(user=user).count()

    context = {
        'billing':billing_query,
        'all_product':all_product,
    }
    return render(request,template_name,context)

def billing_edit(request,id):
    template_name = 'billing/address.html'
    instance = get_object_or_404(Billing_profile,id=id)
    form = BillingForm(request.POST or None,instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user   = request.user
        instance.save()
        return redirect('billing:address')
    context = {
        'form' : form,
        'instance':instance,
        'update': 'Update'

    }
    return render(request,template_name,context)




