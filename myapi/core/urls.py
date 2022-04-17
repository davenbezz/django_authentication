from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
]