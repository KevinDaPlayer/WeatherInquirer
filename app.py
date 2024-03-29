from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True)
