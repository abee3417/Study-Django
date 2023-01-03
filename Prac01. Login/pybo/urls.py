from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login-func/', views.login_func, name='login_func'),
    path('signup-func/', views.signup_func, name='signup_func'),
]