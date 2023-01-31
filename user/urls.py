
from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('', views.index,name='signup'),
    path('home', views.homepage,name='homepage'),
    path('userlogin', views.login_user,name='loginuser'),
    path('log_out/',views.logout, name = 'logout'),
    path('quote', views.quote,name='quote'),
    path('viewquote', views.view_quote,name='viewquote'),


   
]