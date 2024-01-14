from .import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),

    path('user',views.user, name='user'),
    path('admindashboard',views.admindashboard, name='admindashboard'),

    #path('user_details',views.user_details, name='user_details'),

    path('login1',views.login_action, name='login'),
    path('registration',views.user_add, name='login'),


]
