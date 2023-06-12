from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # main page
    path('', views.home_page, name='home_page'),

    # login, register
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register_page'),

    # admin page
    path('myadmin/', views.admin_view, name='myadmin_page'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('createItem', views.new_item_admin, name='new_item_admin'),
    path('myadmin/item/<int:item_id>/', views.item_details_admin, name='item_details_admin'),
    path('myadmin/remove/item/<int:item_id>/', views.remove_item_admin, name='remove_item_admin'),

    # shop
    path('shop/', views.shop, name='shop'),
    path('shop/search', views.shop, name='item_search'),

    # path('login/', auth_views.LoginView.as_view(template_name='ogani-master/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
