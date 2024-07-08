from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)

API_KEY = '60a4986124d04d66a90195315240707'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        return redirect(f'/weather/{zipcode}')
    return render_template('index.html')

@app.route('/weather/<zipcode>')
def weather(zipcode):
    if not zipcode:
        return jsonify({'error': 'Zip code parameter is required'}), 400

    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={zipcode}&aqi=no'
    response = requests.get(url)

    if response.status_code == 404:
        return jsonify({'error': 'City not found'}), 404
    elif response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve data'}), response.status_code

    data = response.json()

    weather_info = {
        'city': data['location']['name'],
        'temperature': data['current']['temp_c'],
        'condition': data['current']['condition']['text'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph']
    }

    return render_template('index.html', weather=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
