from flask import Flask
from Keys import apiKey
import requests

apiLink = "https://ssd-api.jpl.nasa.gov/fireball.api?limit=20"

def create_app():
    app = Flask("abc")

    @app.route('/')
    def Home():
        response = requests.get(apiLink)
        response_json = response.json()
        return response_json
    return app
app = create_app