from django.urls import path
from shop import views
from .views import signupView, signinView, signoutView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
]