from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="income"),
    path('add-income', views.add_income, name="add-income"),
    path('edit-income/<int:id>', views.income_edit, name="income-edit"),
    path('income-delete/<int:id>', views.delete_income, name="income-delete"),
    path('search-income', csrf_exempt(views.search_income),
         name="search_income"),
    
    path('income_source_summary', csrf_exempt(views.income_source_summary),
         name="income_source_summary"),
    path('get_income_by_date', views.get_income_by_date,
         name="get_income_by_date"),
    path('get_income_by_month', views.get_income_by_month,
         name="get_income_by_month"),
    path('incomestats', views.stats_view,
         name="incomestats")
    
]
