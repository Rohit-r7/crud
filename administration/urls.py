from django.urls import path
from . import views
app_name = "administration"
urlpatterns = [
    path('home', views.index,name='quotespage'),
    path('log_out/',views.logout, name = 'logout'),
    path('approve/<int:uid>',views.approve, name = 'approve'),


   
]