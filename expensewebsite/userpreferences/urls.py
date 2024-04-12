from . import views
from django.urls import path

urlpatterns = [
     path('', views.index, name = 'preferences'),
     path('setbudget', views.setBudget, name = 'setbudget')
]
