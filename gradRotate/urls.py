from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('accounts.urls')),
    path('form/', include('users.urls')),
    path('dashboard/', include('dashboard.urls'), name ="dashboard"),
    path('admin_interface/', include('interface.urls'), name = "admin_interface"),

]
