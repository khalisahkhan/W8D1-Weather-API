# W8D1-Weather-API

The Weather API  will retrieve the current weather information for a specified zip code using the weatherAPI.com service. Ot a;;pws users to get the weather details such as temperature, weather condition, humidity and wind speed bu providing a zip code.

# Endpoint and Functionality
Endpoint: '/weather/<zipcode>'
Method: GET

# Request
Query Parameter: zip code of city

# Response Format
The endpoint returns a JSON object with the following information:
'city': name of the city
'temperature': current temperature
'condition': weather condition
'humidity': humidity percentage
'wind speed': wind speed in kph

# Running the API server
1. Clone the repository
2. Install dependencies:
    pip install Flask request
    source venv/bin/activate
3. Obtain API key from WeatherAPI.com
4. Run the application