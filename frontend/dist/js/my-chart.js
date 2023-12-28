// Sample data
var data = {
  labels: ["Label 1", "Label 2", "Label 3", "Label 4"],
  datasets: [
    {
      backgroundColor: "#b6c4cc", // Color for bars
      borderRadius: 10,
      // borderWidth: 2, // Border width for bars
      data: [12, 19, 3, 5], // Actual data values
    },
  ],
};

// Chart configuration
var options = {
  scales: {
    x: {
      grid: {
        display: false,
      },
    },
    y: {
      grid: {
        display: false,
      },
    },
  },
  plugins: {
    title: {
      display: true,
      text: "Average Salaries in 10 Canadian Cities",
      color: "#1c1c1c",
      font: {
        size: 20,
        weight: "bold",
        family: "'Inter', 'sans-serif'",
        lineHeight: "1.75rem",
      },
      align: "start",
      padding: {
        top: 0,
        bottom: 20,
      },
    },
  },
  maintainAspectRatio: false,
};

let ctx = document.getElementById("test2").getContext("2d");

// Create the bar chart
const myBarChart = new Chart(ctx, {
  type: "bar", // Specify the chart type
  data: data,
  options: options,
  responsive: true,
});

ctx = document.getElementById("test3").getContext("2d");

// Create the bar chart
new Chart(ctx, {
  type: "bar", // Specify the chart type
  data: data,
  options: options,
  responsive: true,
});
