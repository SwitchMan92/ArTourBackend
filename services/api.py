import wikipedia
from flask import Flask
from flask_restful import Resource, Api
from googleplaces import GooglePlaces, types


app = Flask(__name__)

API_KEY = 'AIzaSyAadpx8ImSags8ItAgCseBKfVRnTv046tA'
google_places = GooglePlaces(API_KEY)

wikipedia.set_lang("fr")


api = Api(app)


class Wikipedia(Resource):
    def get(self, wiki_name):
        result = wikipedia.search(wiki_name)
        result = wikipedia.page(result[0])
        return {"result": result.content}


class GoogleApi(Resource):
    def get(self, longitude, latitude):
        query_result = google_places.nearby_search(
            lat_lng={"lat": latitude, "lng": longitude},
            types=[types.TYPE_PREMISE, types.TYPE_SUBPREMISE, types.TYPE_CITY_HALL, types.TYPE_MUSEUM,
                   types.TYPE_NATURAL_FEATURE, types.TYPE_CEMETERY]

            )

        results = [[a.name, a.get_details(), float(a.geo_location["lat"]), float(a.geo_location["lng"])] for a in query_result.places]
        return {"result": results}
