
     fetch("/monthSpendBudget")
       .then((res) => res.json())
       .then((results) => {
         console.log('results', results);
         const monthly_expense = results.monthly_expense;
         const budget = results.budget;
         document.getElementById('budget').innerHTML = budget;
         document.getElementById('total_spend').innerHTML = monthly_expense;
         document.getElementById('remaining').innerHTML = budget - monthly_expense;
       });
