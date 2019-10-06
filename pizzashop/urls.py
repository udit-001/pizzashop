from django.contrib import admin
from django.urls import include, path


from accounts.views import profile, verify

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('address/', include('addresses.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
]

admin.site.site_header = "Pizzaitalia Admin"
admin.site.site_title = "Pizzaitalia Admin"
