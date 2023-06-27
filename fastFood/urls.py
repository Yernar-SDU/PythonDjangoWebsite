from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from fastFood import views

urlpatterns = [
    path('', views.home_page),
    path('register/', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('food_detail/<int:food_id>', views.food_details, name='food_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
