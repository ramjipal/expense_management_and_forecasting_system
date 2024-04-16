from django.urls import path, include
from . import views

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
     path('',views.predictExpense, name = "predict_expense")
]