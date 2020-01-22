from django.shortcuts import render,redirect
from .models import CheckouSystem
# Create your views here.
def checkout(request):
    template_name = 'billing/address_view.html'
    context = {


    }
    return render(request,template_name,context)


def checkout_create(request):
        

        if request.method == 'POST':
            #get from values
            user = request.POST['username']
            p_name = request.POST['p_name']

            email = request.POST['email']
            address = request.POST['address']
            city = request.POST['city']
            phone = request.POST['phone']
            zip_c = request.POST['phone']
            card_name = request.POST['card_name']
            card_no = request.POST['card_no']
            # phone = request.POST['password2']

            check_out = CheckouSystem.objects.create(user=user,p_name=p_name, email=email,
                       address=address,city=city,phone=phone,zip_c=zip_c,card_name=card_name,
                       card_no=card_no,active=True)
            if check_out.active == False:
                check_out.save()
                        
                return redirect('browse:bid-log')
            else:
                return redirect('browse:bid-log')

