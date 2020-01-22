from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.
def login_user(request):

    template_name = 'new_user_account/login.html'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are logged In!!')
            return redirect('home')
        else:
            messages.error(request,'Please try again!!')
            return redirect('login')
            
    else:
        return render(request,template_name)


def register_user(request):
    template_name = 'new_user_account/register.html'
    if request.method == 'POST':
        #get from values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if the password match
        if password == password2:
              if User.objects.filter(username = username).exists():
                    messages.error(request,'The username is taken')
                    return redirect('register')
              else:
                    if User.objects.filter(email = email).exists():
                        messages.error(request,'The email is taken')
                        return redirect('register')

                    else:
                       user = User.objects.create_user(username=username,password=password, email=email,
                       first_name=first_name,last_name=last_name)
                       #login after register
                       #auth.login(request,user)
                       #messages.success(request,'You are now logged in')
                       #return redirect('index')
                       user.save()
                       messages.success(request,'Registration Successful. Logged in now!')
                       return redirect('login')

                    
        else:
              messages.error(request, 'Password do not Match')
              return redirect('register')



    else:
        return render(request,template_name)


def logout_user(request):
    logout(request)
    messages.success(request,'You are logged Out!!')
    return redirect('home')


@login_required(login_url='/user/')
def contact_page(request):
        template_name = 'browser/_contact.html'
    # if request.method == 'POST':
    #     pass
        
        form = ContactForm(request.POST,None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user   = request.user
            instance.save()
            return redirect('browse:item_index')

        context = {
            
            'form':form,
        }
        return render(request,template_name,context)


