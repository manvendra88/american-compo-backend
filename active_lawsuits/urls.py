from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ActiveLawsuitsView.as_view()),
    path('all', views.AllActiveLawsuitsView.as_view())
]