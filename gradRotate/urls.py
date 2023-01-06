from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import (
handler400, handler403, handler404, handler500
)



urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('accounts.urls')),
    path('form/', include('users.urls')),
    path('dashboard/', include('dashboard.urls'), name ="dashboard"),
    path('admin_interface/', include('interface.urls'), name = "admin_interface"),

]

handler400 = 'accounts.views.bad_request'
handler403 = 'accounts.views.bad_request'
handler404 = 'accounts.views.bad_request'
