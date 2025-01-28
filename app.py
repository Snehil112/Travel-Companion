import os
from flask import Flask,request,jsonify, render_template
import requests


app = Flask(__name__)
#API keys for weather and flicker API
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]
FLICKR_API_KEY = os.environ["FLICKR_API_KEY"]

#To get the weather data for the specified city
@app.route('/get_weather')
def get_weather():
    city = request.args.get('city')
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(weather_url)
    return jsonify(response.json())

#To get the photos from flicker based on specified tags
@app.route('/get_photos')
def get_photos():
    tags = request.args.get('tags')

    flickr_url = f'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={FLICKR_API_KEY}&tags={tags}&format=json&nojsoncallback=1'
    response = requests.get(flickr_url)
    return jsonify(response.json())

#Render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
