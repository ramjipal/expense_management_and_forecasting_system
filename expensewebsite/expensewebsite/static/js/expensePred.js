fetch('/predict_expense')
     .then((res) => res.json())
     .then((results) => {
          const pred_expense = results.predicted_expense;
          document.getElementById('predicted_expense').innerHTML = pred_expense;
     });
