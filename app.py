import requests
import sqlite3
import matplotlib.pyplot as plt
import schedule
import time
from flask import Flask, render_template

# Flask application
app = Flask(__name__, static_url_path='/static')

# Replace 'YOUR_API_KEY' with your actual WeatherAPI key
api_key = 'bcd79ab4b6264ae2aff62903230609'
city_name = 'Chennai'

# Define the API endpoint
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no'

# Initialize global variables for weather data
timestamps = []
temperatures = []
humidity = 0
wind_speed = 0
weather_condition = ""

# Function to fetch and update weather data
def fetch_and_update_weather_data():
    global timestamps, temperatures, humidity, wind_speed, weather_condition
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Extract the relevant weather data
            temperature_celsius = data['current']['temp_c']
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_kph']
            weather_condition = data['current']['condition']['text']

            # Connect to the SQLite database (or create it if it doesn't exist)
            conn = sqlite3.connect('weather_data.db')
            cursor = conn.cursor()

            # Define the table schema
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature_celsius REAL,
                    humidity INTEGER,
                    wind_speed_kph REAL,
                    weather_condition TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Insert weather data into the database
            cursor.execute('''
                INSERT INTO weather (temperature_celsius, humidity, wind_speed_kph, weather_condition)
                VALUES (?, ?, ?, ?)
            ''', (temperature_celsius, humidity, wind_speed, weather_condition))

            # Commit the changes and close the database connection
            conn.commit()
            conn.close()

            # Append data to global variables for visualization
            timestamps.append(data['current']['last_updated'])
            temperatures.append(temperature_celsius)

            print("Weather data fetched and updated.")
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Schedule the fetch_and_update_weather_data function to run every hour
schedule.every(1).hour.do(fetch_and_update_weather_data)

# Function to create a line chart of temperature over time
def create_temperature_chart():
    # Connect to the SQLite database
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Retrieve all weather data from the database
    cursor.execute('SELECT * FROM weather')
    data = cursor.fetchall()

    # Extract timestamps and temperature data
    chart_timestamps = [row[5] for row in data]  # Choose different variable names
    chart_temperatures = [row[1] for row in data]  # Choose different variable names

    # Create a line chart for temperature over time
    plt.figure(figsize=(10, 6))
    plt.plot(chart_timestamps, chart_temperatures, marker='o', linestyle='-', color='b')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Close the database connection
    conn.close()

# Route for the web-based dashboard
@app.route('/')
def weather_dashboard():
    global timestamps, temperatures, humidity, wind_speed, weather_condition  # Declare them as global
    return render_template('web.html', timestamps=timestamps, temperatures=temperatures,
                           humidity=humidity, wind_speed=wind_speed, weather_condition=weather_condition)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
