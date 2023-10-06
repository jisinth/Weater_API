// Get timestamps and temperatures from Flask template variables
var timestamps = JSON.parse('{{ timestamps | tojson | safe }}');
var temperatures = JSON.parse('{{ temperatures | tojson | safe }}');

// Create a line chart for temperature over time
var ctx = document.getElementById('temperatureChart').getContext('2d');
var temperatureChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: timestamps,
        datasets: [{
            label: 'Temperature (°C)',
            data: temperatures,
            borderColor: 'blue',
            borderWidth: 2,
            pointRadius: 5,
            pointBackgroundColor: 'blue',
            fill: false
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: 'Temperature Over Time'
            },
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'hour',
                        displayFormats: {
                            hour: 'h:mm A'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Timestamp'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature (°C)'
                    }
                }
            }
        }
    }
});

// Example: Add event listeners or perform AJAX requests, if needed
