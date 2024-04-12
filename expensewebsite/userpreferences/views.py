from django.shortcuts import render, redirect, HttpResponse
import os
import json
from django.conf import settings
from .models import UserPreference, Budget
from django.contrib import messages


# Create your views here.


def index(request):
    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    exists = UserPreference.objects.filter(user=request.user).exists()
    user_preferences = None
    if exists:
        user_preferences = UserPreference.objects.get(user=request.user)
    if request.method == 'GET':

        return render(request, 'preferences/index.html', {'currencies': currency_data,
                                                          'user_preferences': user_preferences})
    else:

        currency = request.POST['currency']
        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreference.objects.create(user=request.user, currency=currency)
        messages.success(request, 'Changes saved')
        return render(request, 'preferences/index.html', {'currencies': currency_data, 'user_preferences': user_preferences})

def setBudget(request):
    if request.method == "POST":
        budget_amt = request.POST.get('budget')
        print("________________________")
        print(budget_amt)
        print(request.user)
        
        # Check if the user already has a budget record
        user_budget, created = Budget.objects.get_or_create(user=request.user)
        
        # Update or create the budget record
        user_budget.budget = budget_amt
        user_budget.save()
        
        messages.success(request, "Budget saved")
        
    return redirect("preferences")
        
        
    
