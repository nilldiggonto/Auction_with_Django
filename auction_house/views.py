from django.shortcuts import render
from browser.models import Product,Category_post
from nilam_custom.models import Nilam_slider,Nilam_info_section,Nilam_footer_section
def home(request):
    template_name = 'homepage/index.html'
    queryset = Product.objects.filter(featured=True).order_by('-timestamp')
    slider  = Nilam_slider.objects.all()
    slider_info = Nilam_info_section.objects.all().last()
    slider_footer = Nilam_footer_section.objects.all().last()

    
    # queryset = queryset.objects.get(days_left>0)
    c_queryset = Category_post.objects.all()

    context = {
        'object_list':queryset,
        'cobject_list':c_queryset,
        'slider':slider,
        'slider_info':slider_info,
        'slider_footer':slider_footer,
        # 'page_request_var':page_request_var,
        # 'form':form,
       
    }
    return render(request,template_name,context)