from django.urls import  path

from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('result/', views.result_user, name='result'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('about/', views.about_view, name= 'about'),
   path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
]
