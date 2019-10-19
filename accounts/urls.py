from django.urls import path, re_path
from . import views
from django.contrib.auth import login, logout
from django.views.generic import DetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('display/', views.display, name='display'),
    path('logout/', views.loggedout, name='logout'),
    path('', views.register, name='register'),
    path('rules/', views.rules, name='rules'),
    #path('timer/', views.timer),
    path('about/', views.about_us, name='about_us'),
    path('anscheck/', views.anscheck, name='anscheck'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
