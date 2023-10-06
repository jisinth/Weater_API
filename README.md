# Real-time Weather Data Processing

This is a Python Flask web application that fetches real-time weather data from the WeatherAPI and displays it in a web dashboard. The application also includes a line chart that shows temperature variations over time.

## Features

- Fetches weather data (temperature, humidity, wind speed, weather condition) from the WeatherAPI.
- Stores the weather data in an SQLite database for historical tracking.
- Displays real-time weather data in a web dashboard.
- Includes a line chart to visualize temperature changes over time.
- Scheduled data fetching to keep data up-to-date.

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

- Python 3.x
- Flask
- SQLite3
- Chart.js
- Moment.js

You can install Python packages listed in the `requirements.txt` file using `pip`:


pip install -r requirements.txt


## Setup and Usage

1. Clone the repository:


git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard


2. Replace `'YOUR_API_KEY'` in `app.py` with your actual WeatherAPI key.

3. Run the Flask application:

python app.py


4. Access the web dashboard in your browser at `http://localhost:5000`.

## Screenshots

![Dashboard Screenshot](/screenshots/dashboard.png)

![Chart Screenshot](/screenshots/chart.png)

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or want to contribute code, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Make sure to replace placeholders like 'YOUR_API_KEY', and customize the README to include specific details about your project. You can also add screenshots or any other relevant information.

Don't forget to include the LICENSE file if you choose to use a specific license for your project.
