# account/urls.py
from django.urls import path, include
from account import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('handlesignup/', views.handlesignup, name="handlesignup"),
    path('handlelogin/', views.handlelogin, name="handlelogin"),
    path('handlelogout/', views.handlelogout, name="handlelogout"),
    path('changepass', views.ChangePassword.as_view(), name="changepass")

]
