from django.urls import path
from .views import UserCreateView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register')
]
