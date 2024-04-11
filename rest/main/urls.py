from django.urls import path
from . import views

urlpatterns = [
    path('', views.HumanAPIView.as_view(), name='human')
]