from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("login",views.login,name="login"),
    path("index2",views.index2,name="index2"),
    path("signout",views.signout,name="signout"),
    path("signup",views.signup,name="signup"),
]
