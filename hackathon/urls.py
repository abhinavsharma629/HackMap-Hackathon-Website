from django.contrib import admin
from django.urls import path, include
from hackme.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hackme.urls')),
]
