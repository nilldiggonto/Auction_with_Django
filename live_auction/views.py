from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import LiveForm
from .models import ProductLive,Product_price_live,Live_second_timer
from .forms import LiveBidForm,LiveUpdateForm,LiveSecondForm
from django.db.models import Max
from browser.models import Category_post
# from .forms import PostForm,BidForm,PostUpdateForm
from billing_address.models import Billing_profile
from checkout.models import CheckouSystem
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime,timedelta

from nilam_custom.models import Nilam_regular_rule,Nilam_live_rule

# Create your views here.
@login_required(login_url='/user/')
def live_auctionlist(request):
    template_name = 'live_auction/live-list.html'
    # queryset =
    
    queryset = ProductLive.objects.filter(active=True).order_by('-timestamp')
    context = {
        'object_list':queryset,
    }
    return render(request,template_name,context)





@login_required(login_url='/user/')
def live_auctionlist_user(request):
    template_name = 'new_browser/user_live_item.html'
    # queryset =
    
    user_posts = ProductLive.objects.filter(user=request.user).order_by('timestamp')
    context = {
        'user_posts':user_posts,
    }
    return render(request,template_name,context)




@login_required(login_url='/user/')
def live_auction_detail(request,slug):
    template_name = 'live_auction/live-detail.html'
    user = request.user
    instance = get_object_or_404(ProductLive,slug=slug)
    checkout = CheckouSystem.objects.filter(p_name=instance.title).last()
    regular_rule = Nilam_regular_rule.objects.all().last()
    live_rule = Nilam_live_rule.objects.all().last()

    # checkout = CheckouSystem.objects.filter(p_name=instance.title).last()
    
    second_alarm = Live_second_timer.objects.filter(live_title =instance.id).last()

    # second_alarm.live
    a_false = False
    # print(second_alarm.live)

    # try:
    if second_alarm is not None:

        
        a_false = second_alarm.live

    #         print(a_false)
    # except:
    #     pass
        



    




    



    post_form = LiveUpdateForm(request.POST or None,instance=instance)

    if post_form.is_valid():
        instance = post_form.save(commit=False)
        
        instance.active = False
        if instance.user == request.user:
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())


    

    days_left = instance.days_left()
    days_left = int(days_left)



    bidder_post = Product_price_live.objects.filter(user=request.user).filter(product_title_id=instance.id).order_by('-timestamp')



    instance_price = Product_price_live.objects.filter(product_title=instance.id).aggregate(Max('current_price'))
    try:
        current_price_test = Product_price_live.objects.filter(product_title=instance.id)
    except:
        pass



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



    new_instance_price = instance_price['current_price__max']
    if new_instance_price is None:
        new_instance_price = instance.stating_price
    else:
        new_instance_price = new_instance_price


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
        a = 'Bid or Auction'






    second_form = LiveSecondForm(request.GET or None)
    
    if second_form.is_valid():
                
            
            s_instance = second_form.save(commit=False)
            s_instance.live_title = ProductLive.objects.get(slug=slug)
            s_instance.live = True
            s_instance.end_timer =datetime.now()+timedelta(minutes=5)
            
            
            if request.user == instance.user:
                s_instance.save()
                return HttpResponseRedirect(s_instance.get_absolute_url())
            # return redirect('browse:bidder')
            
            return HttpResponseRedirect(s_instance.get_absolute_url())







    form = LiveBidForm(request.POST or None)
    if form.is_valid():
        
        
        instance = form.save(commit=False)
        instance.product_title = ProductLive.objects.get(slug=slug)
        instance.user   = request.user
        instance.current_price = 10
        instance.bid_price = instance.current_price
        print(instance.bid_price)
        if new_instance_price is not None:
            instance.current_price += new_instance_price 
        
        
        instance.save()
        # return redirect('browse:bidder')
        
        return HttpResponseRedirect(instance.get_absolute_url())


    
    

    



    context ={
        'object':instance,
        'form':form,
        'object_price': instance_price,
        'current_price': current_price,
        'current_price_user':current_price_user,
        'bidder_post':bidder_post,
        'days_left':days_left,
        'post_form':post_form,
        'checkout':checkout,
        'a': a,
        'second_form':second_form,
        'second_alarm':second_alarm,
        'a_false':a_false,
        'regular_rule':regular_rule,
        'live_rule':live_rule,
    }
    return render(request,template_name,context)



@login_required(login_url='/user/')
def  live_aution_create(request):
    template_name = 'live_auction/live-create.html'
    billing_query = Billing_profile.objects.filter(user=request.user).filter(active=True).last()
    c_queryset = Category_post.objects.all()


    # if request.method == 'POST':
    #     pass
        
    form = LiveForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user   = request.user
        instance.save()
        return redirect('live:live-list')

    context = {
        
        'form':form,
        'billing':billing_query,
        'category':c_queryset,

    }
    return render(request,template_name,context)



















@login_required(login_url='/user/')
def bidder_detail_live(request):
    
    user = request.user
    bidder_post = Product_price_live.objects.filter(user=request.user).order_by('-timestamp')

 
    template_name = 'browser/live_bid_detail.html'

    #contact
    
    return render(request, template_name, {'bidder_post':bidder_post,'user': user,})



@login_required(login_url='/user/')
def bidding_item_log_live(request):
    user = request.user
    bidder_post = Product_price_live.objects.filter(user=request.user).distinct('product_title')
    checkout = CheckouSystem.objects.filter(user=user)
    a ='aa'
    try:
        for c in checkout:
            a = c.p_name
            print(a)
    except:
        a = 'aa'

        
    
    # win_post   = Product_price.object.all().last()
    template_name = 'browser/live_bid_log.html'
    # print(bidder_post.count())

    context = {
        'bidder': bidder_post,
        'user':user,
        'bid_count': bidder_post.count(),
        'a':a,
    }
    return render(request,template_name,context)