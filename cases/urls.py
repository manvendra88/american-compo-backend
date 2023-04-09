from django.urls import path 
from . import views

urlpatterns = [
    path('', views.CaseView.as_view()),
]