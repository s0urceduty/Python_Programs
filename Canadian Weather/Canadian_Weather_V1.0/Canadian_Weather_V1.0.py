# Canadian_Weather V1.0

# 🌤️ Displaying the average provincial temperature and the current temperatures for cities in Canada.

# Copyright (C) 2023,  Sourceduty - All Rights Reserved.
# This software is free and open-source; anyone can redistribute it and/or modify it.

import folium
import requests

# Your WeatherAPI Key
API_KEY = "e5db39ef26874046bc9214533230111"

# List of cities in Canada for weather data
cities = ["Toronto", "Vancouver", "Montreal", "Calgary", "Edmonton", "Ottawa", "Quebec City"]

# List of province capitals with their coordinates
provinces = {
    "Victoria": [48.4284, -123.3656],  # British Columbia
    "Edmonton": [53.5461, -113.4938],  # Alberta
    "Regina": [50.4452, -104.6189],    # Saskatchewan
    "Winnipeg": [49.8951, -97.1384],   # Manitoba
    "Toronto": [43.6532, -79.3832],    # Ontario
    "Quebec City": [46.8139, -71.2082],# Quebec
    "Fredericton": [45.9636, -66.6431],# New Brunswick
    "Halifax": [44.6488, -63.5752],    # Nova Scotia
    "Charlottetown": [46.2382, -63.1311], # Prince Edward Island
    "St. John's": [47.5615, -52.7126]  # Newfoundland and Labrador
}

# Create a base map
m = folium.Map(location=[56.1304, -106.3468], zoom_start=4)  # Coordinates for Canada

# Fetch weather data and calculate average temperature for each province
province_temps = {}
for capital in provinces.keys():
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={capital}")
    data = response.json()

    # Check for errors in the API response
    if "error" in data:
        print(f"Error fetching weather data for {capital}. Message: {data['error']['message']}")
        continue

    temp = data["current"]["temp_c"]
    province_temps[capital] = temp

# Calculate the average provincial temperature
avg_temp = sum(province_temps.values()) / len(province_temps)

# Add red markers for each province capital with average temperature
for capital, coords in provinces.items():
    folium.Marker(
        coords,
        popup=f"{capital}<br>Average Temperature: {avg_temp:.2f}°C",
        icon=folium.Icon(color="red"),
    ).add_to(m)

# Fetch weather data and add blue markers for selected cities
for city in cities:
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}")
    data = response.json()

    # Check for errors in the API response
    if "error" in data:
        print(f"Error fetching weather data for {city}. Message: {data['error']['message']}")
        continue

    temp = data["current"]["temp_c"]
    description = data["current"]["condition"]["text"]
    lat, lon = data["location"]["lat"], data["location"]["lon"]

    # Add blue marker to the map for weather data
    folium.Marker(
        [lat, lon],
        popup=f"{city}<br>Temperature: {temp}°C<br>Description: {description}",
        icon=folium.Icon(color="blue", icon="cloud"),
    ).add_to(m)

# Save the map to an HTML file
m.save("canada_weather_map.html")
