from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('user/',include('user_account.urls')),
    path('explore/',include('browser.urls')),
    path('billing/',include('billing_address.urls')),
    path('live/',include('live_auction.urls')),
    path('checkout/',include('checkout.urls')),
    path('api/',include('live_auction.api.urls')),
    path('nilam/admin/',include('nilam_admin.urls')),
    path('faq/',include('faq.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
