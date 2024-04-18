from django.shortcuts import render
from expenses.models import Expense
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta
from django.http import JsonResponse
# Create your view

def getExpenseDataFrame(user):
     user_expense = Expense.objects.filter(owner = user).order_by('date')
     expense_data = list(user_expense.values('date', 'amount'))
     expense_dataframe = pd.DataFrame(expense_data)
     return expense_dataframe


     
def predictExpense(request):
     period_expense = 0
     data = getExpenseDataFrame(request.user)
     def find_moving_average():
          df = data.copy()
          df['50_MA'] = df['amount'].ewm(span=10, adjust=False).mean()
          df['200_MA'] = df['amount'].ewm(span=15, adjust=False).mean()
          df['MA_Diff'] = df['50_MA'] - df['200_MA']
          df['day'] = df['date'].apply(lambda x: x.weekday())
          last_expense_date = df['date'].iloc[-1]
          last_expense = df[df['date'] == last_expense_date]
          df['Next_day_expense'] = df['amount'].shift(-1)
          df.dropna(inplace=True)
          df.reset_index(drop = True, inplace = True)
          # print(df)
          return df, last_expense_date, last_expense
     if len(data)>=1:#the data should be greater than 200 for better accuracy
          curr_date = datetime.today()
          nxt_mnth = curr_date.replace(day=28) + timedelta(days=4)
     
          # subtracting the days from next month date to 
          # geting last date of current Month
          last_month_date = nxt_mnth - timedelta(days=nxt_mnth.day)
          remain_days = (last_month_date - curr_date).days
          period_expense = 0
          for i in range(remain_days):
               df, last_expense_date, last_expense = find_moving_average()
               X = df[['50_MA', '200_MA', 'MA_Diff', 'day']]
               y = df['Next_day_expense']
               X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
               model = LinearRegression()
               model.fit(X_train, y_train)
               if not last_expense.empty:
                    pred_Next_exp = model.predict(last_expense[['50_MA', '200_MA', 'MA_Diff', 'day']])
                    period_expense += pred_Next_exp[0]
                    next_expense_date =  last_expense_date + timedelta(days = 1)
                    new_data_list = [next_expense_date, pred_Next_exp[0]]
                    new_data_df = pd.DataFrame([{'date': new_data_list[0], 'amount': new_data_list[1]}])
                    data.loc[len(data)] = new_data_df.iloc[0]
                    del df
          
          
     
     
     return JsonResponse({'predicted_expense':round(period_expense)})