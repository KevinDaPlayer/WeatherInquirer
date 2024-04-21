from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

Weather_APIKEY = '779701edbbc768ee1f879cc1b8d2baaf'

@app.route('/')
def HelloWorld():
    return '你好世界'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error':'Missing city parameter'})
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_APIKEY}&units=metric'

    response = requests.get(url)
    print("Response from OpenWeatherMap:", response.json())
    return jsonify(response.json())

@app.route('/weather-coord', methods=['GET'])
def get_weather_by_coord():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Weather_APIKEY}&units=metric'

    response = requests.get(url)
    print("Response from OpenWeatherMap:", response.json())
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
