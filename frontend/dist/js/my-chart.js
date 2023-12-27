// Sample data
var data = {
  labels: ["Label 1", "Label 2", "Label 3", "Label 4"],
  datasets: [
    {
      label: "Sample Data",
      backgroundColor: "rgba(239 ,68 ,68)", // Color for bars
      borderColor: "black", // Border color for bars
      borderWidth: 2, // Border width for bars
      data: [12, 19, 3, 5], // Actual data values
    },
  ],
};

// Chart configuration
var options = {
  scales: {
    y: {
      display: true,
      beginAtZero: true,
    },
  },
  maintainAspectRatio: false,
  devicePixelRatio: 4,
};

const ctx = document.getElementById("test2").getContext("2d");

// Create the bar chart
const myBarChart = new Chart(ctx, {
  type: "bar", // Specify the chart type
  data: data,
  options: options,
  responsive: true,
});
