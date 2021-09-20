from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import MyLoginView, MySignupView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login_page'),
    path('register/', MySignupView.as_view(), name='register_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
