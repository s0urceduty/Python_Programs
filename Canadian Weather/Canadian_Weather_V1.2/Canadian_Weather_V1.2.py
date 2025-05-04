# Canadian_Weather V1.2

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

# Cities for each province
province_cities = {
    "British Columbia": ["Vancouver", "Kelowna", "Nanaimo"],
    "Alberta": ["Edmonton", "Calgary", "Red Deer"],
    "Saskatchewan": ["Regina", "Saskatoon", "Moose Jaw"],
    "Manitoba": ["Winnipeg", "Brandon", "Thompson"],
    "Ontario": ["Toronto", "Ottawa", "Hamilton"],
    "Quebec": ["Montreal", "Quebec City", "Sherbrooke"],
    # ... add cities for other provinces
}

# Calculate average temperature for each province
province_avg_temps = {}
for province, cities in province_cities.items():
    total_temp = 0
    count = 0

    for city in cities:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}")
        data = response.json()

        # Check for errors in the API response
        if "error" in data:
            print(f"Error fetching weather data for {city}. Message: {data['error']['message']}")
            continue

        total_temp += data["current"]["temp_c"]
        count += 1

    province_avg_temps[province] = total_temp / count if count != 0 else None

# Create a base map
m = folium.Map(location=[56.1304, -106.3468], zoom_start=4)  # Coordinates for Canada

# Add red markers for each province capital with its province's average temperature
for capital, coords in provinces.items():
    province_name = next((name for name, cities in province_cities.items() if capital in cities), None)
    avg_temp = province_avg_temps.get(province_name, "Data not available")
    folium.Marker(
        coords,
        popup=f"{capital}<br>Average Temperature: {avg_temp if isinstance(avg_temp, str) else f'{avg_temp:.2f}°C'}",
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


