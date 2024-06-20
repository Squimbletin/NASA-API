from flask import Flask, jsonify, render_template
import requests
from Keys import apiKey
from Keys import mapsKey

apiLink = "https://ssd-api.jpl.nasa.gov/fireball.api?limit=20"


def create_app():
    app = Flask(__name__, template_folder='templates')

    @app.route('/map')
    def map():
        #Coords to goto On map
        coords = "0,0"
        response = requests.get(apiLink)
        data = response.json()

        # Extract the first entry
        first_entry = data["data"][0]

        # Create a dictionary with the desired fields
        result = {
            "timestamp": first_entry[0],
            "energy": first_entry[1],
            "impact_e": first_entry[2],
            "latitude": first_entry[3],
            "latitude_direction": first_entry[4],
            "longitude": first_entry[5],
            "longitude_direction": first_entry[6],
            "altitude": first_entry[7],
            "velocity": first_entry[8]
        }

        coords = first_entry[3] + "," + first_entry[5]
        print(coords)
        mapLink = "https://maps.googleapis.com/maps/api/staticmap?center=0&zoom=1&size=1000x600&markers="+ coords + "&key=" + mapsKey
        print(mapLink)
        return render_template('map.html', map_url=mapLink)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
