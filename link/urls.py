from django.urls import path
from .views import UrlListView, UrlCreateView, UrlRedirectView

urlpatterns = [
    path('', UrlListView.as_view(), name='home'),
    path('create/', UrlCreateView.as_view(), name='create-url'),
    path('<str:url>/', UrlRedirectView.as_view(), name='redirect-url'),
]
