from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Product_price,Category_post
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import PostForm,BidForm,PostUpdateForm
from django.http import HttpResponseRedirect,HttpResponse
from user_account.forms import ContactForm
from django.db.models import Max
from django.contrib import messages,auth
from billing_address.models import Billing_profile
from checkout.models import CheckouSystem
from nilam_custom.models import Nilam_regular_rule,Nilam_live_rule
# Create your views here.

def item_list(request):
    template_name = 'new_browser/item_list.html'
    queryset = Product.objects.filter(active=True).order_by('-timestamp')
    
    # queryset = queryset.objects.get(days_left>0)
    c_queryset = Category_post.objects.all()
    print(c_queryset)
    query = request.GET.get('q')
    print(query)
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)).distinct()

    paginator = Paginator(queryset,6)
    page_request_var = "page"
    page = request.GET.get(page_request_var) 
    queryset = paginator.get_page(page) 

    form = ContactForm(request.POST,None)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.user   = request.user
            instance.save()
            return redirect('browse:item_index')

    context = {
        'object_list':queryset,
        'cobject_list':c_queryset,
        'page_request_var':page_request_var,
        'form':form,
        'query':query,
       
    }
    return render(request,template_name,context)


#category list....show.....show...show...show...show...show...
def item_category(request):
    template_name = 'new_browser/category_list.html'
    c_queryset = Category_post.objects.all()

    context = {
        'object_list':c_queryset,
    }
    return render(request,template_name,context)

def category_post(request,slug):
    template_name   = 'new_browser/item_list.html'
    category = get_object_or_404(Category_post, slug=slug)
    #////////
    # queryset = Product.objects.filter(active=True)
    queryset = Product.objects.filter(p_category=category.id).filter(active=True)

    # c_queryset = Category_post.objects.all()
    # print(c_queryset)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)).distinct()

    paginator = Paginator(queryset,4)
    page_request_var = "page"
    page = request.GET.get(page_request_var) 
    queryset = paginator.get_page(page) 
    #//////////////////
    

    context = {
        'category': category,
        'object_list':queryset,
        # 'cobject_list':c_queryset,
        'page_request_var':page_request_var,
    }
    return render(request,template_name,context)


@login_required(login_url='/user/')
def item_create(request):
    template_name = 'new_browser/item_create.html'
    billing_query = Billing_profile.objects.filter(user=request.user).filter(active=True).last()
    c_queryset = Category_post.objects.all()
    print(billing_query)
    print(billing_query)
    print(billing_query)
    print(billing_query)
    

   


    # if request.method == 'POST':
    #     pass
        
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user   = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        
        'form':form,
        'billing':billing_query,
        'category':c_queryset,
    }
    return render(request,template_name,context)


@login_required(login_url='/user/')
def item_detail(request,slug):
    template_name = 'new_browser/item_detail.html'
    user = request.user
    instance = get_object_or_404(Product,slug=slug)
    checkout = CheckouSystem.objects.filter(p_name=instance.title).last()
    regular_rule = Nilam_regular_rule.objects.all().last()
    live_rule = Nilam_live_rule.objects.all().last()


    
    
    post_form = PostUpdateForm(request.POST or None,instance=instance)

    if post_form.is_valid():
        instance = post_form.save(commit=False)
        
        instance.active = False
        if instance.user == request.user:
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(type(instance.days_left))
    # print(instance.days_left())
    days_left = instance.days_left()
    days_left = int(days_left)
    # print(days_left)
    # print(days_left)
    # print(days_left)
    # print(days_left)
    # print(days_left)
    # print(days_left)
    # print(days_left)
    # print(days_left)

    bidder_post = Product_price.objects.filter(user=request.user).filter(product_title_id=instance.id).order_by('-timestamp')
    print(instance.title)
    # instance_price = get_object_or_404(Product_price,id=2)
    # test_price = Product_price.objects.filter(id = instance.id)
    # print(test_price)
    # test_ins = get_object_or_404(Product_price or None)
    
    instance_price = Product_price.objects.filter(product_title=instance.id).aggregate(Max('current_price'))
    try:
        current_price_test = Product_price.objects.filter(product_title=instance.id)
    except:
        pass
    print(instance_price)
    print(instance_price)
    print(instance_price)
    try:
        current_price_user = current_price_test.last()
        print(current_price_user)
    except:
        pass
    


    
    
    try:
        
        current_price = current_price_test.latest('current_price')
        # current_price_user = current_price_test.latest('user')

        print(current_price.current_price)
        print(current_price.current_price)
        print(current_price_user.user)

        print(current_price)
        print(current_price)

      
    except:
        current_price = 'Nothing'

   
    # if  instance_price is not None:
    #     print('hlw')
    #     instance_price = instance.stating_price


    # else:
    #     instance_price = Product_price.objects.filter(product_title=instance.id).aggregate(Max('current_price'))

    #     print(instance_price)
     
    new_instance_price = instance_price['current_price__max']
    if new_instance_price is None:
        new_instance_price = instance.stating_price
    else:
        new_instance_price = new_instance_price
    # print(new_instance_price)
    # print(instance.stating_price)
    # print(instance_price)
    # print(current_price)
    try:
        if request.user == instance.user:
            a = 'Your Item posted'
        elif current_price.current_price == new_instance_price and request.user ==current_price_user.user:
            a = 'You are winning'
            print(a)
        
        else:
            a = 'You should bid'
            print(a)
    except:
        a = 'If you want you can Bid'

 



    form = BidForm(request.POST or None)
    if form.is_valid():
        
        
        instance = form.save(commit=False)
        instance.product_title = Product.objects.get(slug=slug)
        instance.user   = request.user
        instance.bid_price = instance.current_price
        print(instance.bid_price)
        if new_instance_price is not None:
            instance.current_price += new_instance_price 
        
        
        instance.save()
        # return redirect('browse:bidder')
        messages.success(request,'You Just Bid!!')
        
        return HttpResponseRedirect(instance.get_absolute_url())
        # return HttpResponseRedirect(instance.get_absolute_url())


    # try:
    #     test_user = Product_price.objects.filter(user=request.user)
    # except:
    #     pass

    # print(test_user.user)

    # if(days_left<0):

    #     if request.method == 'POST':
    #         #get from values
    #         user = request.POST['username']
    #         p_name = request.POST['p_name']

    #         email = request.POST['email']
    #         address = request.POST['address']
    #         city = request.POST['city']
    #         phone = request.POST['phone']
    #         zip_c = request.POST['phone']
    #         card_name = request.POST['card_name']
    #         card_no = request.POST['card_no']
    #         # phone = request.POST['password2']

    #         check_out = CheckouSystem.objects.create(user=user,p_name=p_name, email=email,
    #                    address=address,city=city,phone=phone,zip_c=zip_c,card_name=card_name,
    #                    card_no=card_no)
    #         check_out.save()
                       
    #         return redirect('browse:account')



    

    

    context = {
        
        'object':instance,
        'object_price': instance_price,
        'form':form,
        'user':user,
        'a': a,
        'days_left':days_left,
        'current_price': current_price,
        'current_price_user':current_price_user,
        'bidder_post':bidder_post,
        'post_form':post_form,
        'checkout':checkout,
        'regular_rule':regular_rule,
        'live_rule':live_rule,

    }
    return render(request,template_name,context)



@login_required(login_url='/user/')
def userprofile(request):
    user = request.user
    user_posts = Product.objects.filter(user=request.user).order_by('-timestamp')
    template_name = 'new_browser/user_item.html'
    # form = PostUpdateForm(request.POST or None)
    # if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user   = request.user
    #         instance.save()
    #         return redirect('browse:account')
    return render(request, template_name, {'user_posts':user_posts,'user': user})


# def bidder_detail(request,pk):

@login_required(login_url='/user/')
def bidder_detail(request):
    
    user = request.user
    bidder_post = Product_price.objects.filter(user=request.user).order_by('-timestamp')

    # bidder_post = bidder_post['user']
    # test  = Product_price.objects.filter(user=request.user)
    # test_one = test.latest('timestamp')
    # test_two = test_one('current_price')



    # instance = Product_price.objects.all()
    # for s in instance:
    #     print(s.product_title)
    

    # print(instance.product_title)
    # instance_price = Product_price.objects.filter(product_title=instance.id).aggregate(Max('current_price'))
    # print(instance)



    



   
    
    # current_price_test = Product_price.objects.filter(user=request.user)
    # current_price = current_price_test['current_price']
    # print(test_one)

    template_name = 'browser/bid_detail.html'

    #contact
    form = ContactForm(request.POST,None)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.user   = request.user
            instance.save()
            return redirect('browse:bidder')
    return render(request, template_name, {'bidder_post':bidder_post,'user': user,'form':form})



def contact_page(request):
        template_name = 'new_browser/_contact.html'
        form = ContactForm(request.POST,None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user   = request.user
            instance.save()
            messages.success(request,'Your message sent!!')
            return redirect('browse:contact')
        context = {
            'form':form,
        }
        return render(request,template_name,context)



@login_required(login_url='/user/')
def bidding_item_log(request):
    user = request.user
    bidder_post = Product_price.objects.filter(user=request.user).distinct('product_title')
    checkout = CheckouSystem.objects.filter(user=user)
    a = 'aa'
    try:
        for c in checkout:
            a = c.p_name
            print(a)
    except:
        a = 'aa'

        
    
    # win_post   = Product_price.object.all().last()
    template_name = 'browser/bid_log.html'
    print(bidder_post.count())

    context = {
        'bidder': bidder_post,
        'user':user,
        'bid_count': bidder_post.count(),
        'a':a,
    }
    return render(request,template_name,context)


        

