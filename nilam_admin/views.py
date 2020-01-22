from django.shortcuts import render,get_object_or_404,redirect
from browser.models import Product,Category_post,Product_price
from user_account.models import Contact_admin
from user_account.forms import Contact_seen
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from live_auction.models import ProductLive,Product_price_live
from django.contrib.auth.models import User
from billing_address.models import Billing_profile
# Create your views here.

#user model here
@staff_member_required
def user_view(request):
    template_name = 'nilam_admin/user/user_info.html'
    user_all = User.objects.all()
    context = {
        'user_all':user_all,

    }
    return render(request,template_name,context)


@staff_member_required
def user_active_view(request):
    template_name = 'nilam_admin/user/active_user.html'
    user_all = Billing_profile.objects.all()
    context = {
        'user_all':user_all,

    }
    return render(request,template_name,context)


def active_address(request,id):
    template_name = 'nilam_admin/user/profile.html'
    instance = get_object_or_404(Billing_profile,id=id)
    all_product = Product.objects.filter(user=instance.user).count()

    # form = BillingForm(request.POST or None,instance=instance)
    context ={
        'billing':instance,
        'all_product':all_product,

    }
    return render(request,template_name,context)




@staff_member_required
def dashboard(request):
    template_name = 'nilam_admin/home.html'
    total_item = Product.objects.all().count()
    t_live_item = ProductLive.objects.all().count()
    user_all = User.objects.all().count()
    context = {
        'total_item':total_item,
        't_live_item':t_live_item,
        'user_all': user_all,
    }
    return render(request,template_name,context)

@staff_member_required
def product_view(request):
    template_name = 'nilam_admin/product.html'
    product_list = Product.objects.all().order_by('-timestamp')
    context = {
        'product_list':product_list,

    }
    return render(request,template_name,context)



@staff_member_required
def live_product_view(request):
    template_name = 'nilam_admin/product.html'
    product_list = ProductLive.objects.all().order_by('-timestamp')
    context = {
        'product_list':product_list,
        'live' : 'Live',
    }
    return render(request,template_name,context)




@staff_member_required
def product_detail(request,slug):
    instance = get_object_or_404(Product,slug=slug)
    template_name = 'nilam_admin/product_detail.html'
    days_left = instance.days_left()
    days_left = int(days_left)
    print(instance.id)
    context = {
        'product':instance,
        'days_left':days_left,
    }
    return render(request,template_name,context)



@staff_member_required
def live_product_detail(request,slug):
    instance = get_object_or_404(ProductLive,slug=slug)
    template_name = 'nilam_admin/product_detail.html'
    days_left = instance.days_left()
    days_left = int(days_left)
    # print(instance.id)
    context = {
        'product':instance,
        'days_left':days_left,
    }
    return render(request,template_name,context)






@staff_member_required
def product_category(request):
    template_name ='nilam_admin/product_category.html'
    category_list = Category_post.objects.all()

    context = {
        'category_list':category_list,
    }
    return render(request,template_name,context)

#admin_contact
@staff_member_required
def contact_admin_all(request):
    template_name = 'nilam_admin/message.html'
    message_list = Contact_admin.objects.all()
    message_count = Contact_admin.objects.filter(active=False)
    m_count = 0
    if message_count is not None:
        m_count = message_count.count()
    print(m_count)
    for message in message_list:
        print(message.description)

    context = {
        'message_list': message_list,
    }
    return render(request,template_name,context)
@staff_member_required
def contact_admin_read(request):
    template_name = 'nilam_admin/message.html'
    message_list = Contact_admin.objects.filter(active=True)

    context = {
        'message_list': message_list,
        
    }
    return render(request,template_name,context)


@staff_member_required
def contact_admin_unread(request):
    template_name = 'nilam_admin/message.html'
    message_list = Contact_admin.objects.filter(active=False)

    context = {
        'message_list': message_list,
    }
    return render(request,template_name,context)

@staff_member_required
def contact_admin_detail(request,slug): 
    template_name = 'nilam_admin/message_detail.html'
    message_list = get_object_or_404(Contact_admin,slug=slug)

    contact_read = Contact_seen(request.POST or None,instance=message_list)

    if contact_read.is_valid():
        instance = contact_read.save(commit=False)
        
        instance.active = True
        
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'obj': message_list,
        'form':contact_read
    }
    return render(request,template_name,context)



##################################
#            BID                 #
##################################
@staff_member_required
def all_bid(request):
    bid_list = Product_price.objects.all().order_by('-timestamp')
    template_name = 'nilam_admin/bid/all_bid.html'
    context = {
        'bid_list': bid_list,
    }
    return render(request,template_name,context)


#live bid
@staff_member_required
def all_live_bid(request):
    bid_list = Product_price_live.objects.all().order_by('-timestamp')
    template_name = 'nilam_admin/bid/all_bid.html'
    context = {
        'bid_list': bid_list,
    }
    return render(request,template_name,context)


@staff_member_required
def winning_bid(request):
    bid_list = Product.objects.all()
    template_name = 'nilam_admin/bid/bid_item.html'
    context = {
        'bid_list': bid_list,
    }
    return render(request,template_name,context)

#all live product
@staff_member_required
def all_premium(request):
    bid_list = ProductLive.objects.all()
    template_name = 'nilam_admin/bid/bid_item.html'
    context = {
        'bid_list': bid_list,
    }
    return render(request,template_name,context)


@staff_member_required
def bid_win_loss(request,slug):
    instance = get_object_or_404(Product,slug=slug)

    bid_list = Product_price.objects.filter(product_title_id=instance.id).distinct('user')
    win_bid = Product_price.objects.filter(product_title_id=instance.id).last()

    template_name = 'nilam_admin/bid/bid_win_los.html'
    # days_left = instance.days_left()
    # days_left = int(days_left)
    # print(instance.id)
    context = {
        'bid_list':bid_list,
        'win_bid':win_bid,
        # 'days_left':days_left,
    }
    return render(request,template_name,context)


@staff_member_required
def bid_detail(request,pk):
    instance = get_object_or_404(Product_price,pk=pk)
    template_name = 'nilam_admin/bid/bid_detail.html'
    # days_left = instance.days_left()
    # days_left = int(days_left)
    # print(instance.id)
    context = {
        'bid':instance,
        
        # 'days_left':days_left,
    }
    return render(request,template_name,context)

