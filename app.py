#from __future__ import unicode_literals

import pprint
import wikipedia
import json

from flask import Flask, request
from flask_restful import Resource, Api
from googleplaces import GooglePlaces, types, lang


wikipedia.set_lang("fr")

app = Flask(__name__)
api = Api(app)

API_KEY = 'AIzaSyAadpx8ImSags8ItAgCseBKfVRnTv046tA'
google_places = GooglePlaces(API_KEY)

#43.624378
#1.388731


class Wikipedia(Resource):
    def get(self, wiki_name):
        result = wikipedia.search(wiki_name)
        result = wikipedia.page(result[0])
        return {"result": result.content}


class GoogleApi(Resource):
    def get(self, longitude, latitude):
        query_result = google_places.nearby_search(
            lat_lng={"lat": float(latitude), "lng": float(longitude)},
            types=[types.TYPE_PREMISE, types.TYPE_SUBPREMISE, types.TYPE_CITY_HALL, types.TYPE_MUSEUM,
                   types.TYPE_NATURAL_FEATURE, types.TYPE_CEMETERY]

            )

        results = [[a.name, float(a.geo_location["lat"]), float(a.geo_location["lng"])] for a in query_result.places]
        return {"result": results}


api.add_resource(Wikipedia, '/wikipedia/<string:wiki_name>')
api.add_resource(GoogleApi, '/google_api/<string:longitude>&<string:latitude>')

"""
@app.route('/')
def hello_world():

    pp = pprint.PrettyPrinter(indent=4)

    \"\"\"
    query_result = google_places.nearby_search(
            lat_lng={"lat": 43.624378, "lng": 1.388731},
            radius=5000,
            types=[types.TYPE_CHURCH]
        )

    types.TYPE_AQUARIUM, types.TYPE_ART_GALLERY, types.TYPE_CEMETERY, types.TYPE_CHURCH,
    types.TYPE_EMBASSY, types.TYPE_HINDU_TEMPLE, types.TYPE_MOSQUE, types.TYPE_MUSEUM,
    types.TYPE_PARK, types.TYPE_STADIUM, types.TYPE_SYNAGOGUE, types.TYPE_UNIVERSITY,
    types.TYPE_ZOO, types.TYPE_CITY_HALL

    if query_result.has_attributions:
        print query_result.html_attributions

    for place in query_result.places:
        # Returned places from a query are place summaries.
        print place.name
        print place.geo_location
        print place.place_id

        # The following method has to make a further API call.
        place.get_details()

        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        pp.pprint(place.details)  # A dict matching the JSON response from Google.
        print place.local_phone_number
        print place.international_phone_number
        print place.website
        print place.url
    \"\"\"

    result = wikipedia.search("Basilique Saint-Sernin de Toulouse")

    result = wikipedia.page(result[0])

    #pp.pprint(result)

    return "<p>{0}</p>".format(repr(result.content))
"""


if __name__ == '__main__':
    app.run(debug=True)
