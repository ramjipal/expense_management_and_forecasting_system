const rend_d = (data, labels) => {
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: labels,
      datasets: [
        {
          label: "",
          data: data,
          backgroundColor: [
            "rgba(235, 99, 132, 0.4)",
            "rgba(54, 162, 235, 0.4)",
            "rgba(255, 206, 86, 0.4)",
            "rgba(75, 192, 92, 0.4)",
            "rgba(153, 102, 255, 0.4)",
            "rgba(255, 159, 44, 0.4)",
            "rgba(25, 159, 34, 0.4)",
            "rgba(255, 19, 94, 0.4)",
            "rgba(55, 59, 67, 0.4)",
            "rgba(285, 359, 74, 0.4)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Income per Source",
      },
    },
  });
};

const getSourceIncome = () => {
  console.log("fetching");
  fetch("/income/income_source_summary")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const source_data = results.income_source_data;
      const [labels, data] = [
        Object.keys(source_data),
        Object.values(source_data),
      ];
      rend_d(data, labels);
    });
};


// -------------------------------------------------------------------------------
const rend_line = (data, labels) => {
  var cty = document.getElementById("line").getContext("2d");
  var myChart = new Chart(cty, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "date Income",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132)",
            "rgba(54, 162, 235)",
            "rgba(255, 206, 86)",
            "rgba(75, 192, 192)",
            "rgba(153, 102, 255)",
            "rgba(255, 159, 64)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: "Income Trend",
      },
    },
  });
};

const getDateIncome = () => {
  console.log("fetching");
  fetch("/income/get_income_by_date")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const date_wise_income = results.income_by_date;
      const [labels, data] = [
        Object.keys(date_wise_income),
        Object.values(date_wise_income),
      ];
      rend_line(data, labels);
    });
};

//-------------------------------------------------------------------

const rend_bar = (data, labels) => {
  var ctz = document.getElementById("bar").getContext("2d");
  var myChart = new Chart(ctz, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Monthly income",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 0.4)",
            "rgba(54, 162, 235, 0.4)",
            "rgba(255, 206, 86, 0.4)",
            "rgba(75, 192, 192, 0.4)",
            "rgba(153, 102, 255, 0.4)",
            "rgba(255, 159, 64, 0.4)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true
    },
  });
};

const getMonthIncome = () => {
  console.log("fetching");
  fetch("/income/get_income_by_month")
    .then((res) => res.json())
    .then((results) => {
      console.log("results", results);
      const month_wise_income = results.income_by_month;
      const [labels, data] = [
        Object.keys(month_wise_income),
        Object.values(month_wise_income),
      ];
      rend_bar(data, labels);
    });
};


document.addEventListener('DOMContentLoaded', function() {
  getSourceIncome();
  getDateIncome();
  getMonthIncome();
  console.log("calling function");
});
