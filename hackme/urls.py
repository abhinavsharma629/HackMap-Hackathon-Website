from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main,name='main'),
    path('form', views.form, name='form'),
    path('form1', views.form1, name='form1'),
    path('detail/<details>', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)