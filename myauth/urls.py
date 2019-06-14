from django.urls import path
from . import views

app_name = 'myauth'
urlpatterns = [
    path('', views.index, name='主页'),
    path('login/', views.login, name='登录'),
    path('logout/', views.logout, name='登出')
]
