from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('booking/', views.booking,name='booking'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login,name='login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)