from django.urls import path
from . import views
app_name = 'passwordGenerator'
urlpatterns = [
    # Password Generator URLs
    path('choosepassword', views.passhome, name='passhome'),
    path('generatedpassword/', views.password, name='password'),
]
