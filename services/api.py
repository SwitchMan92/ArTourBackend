import wikipedia
from flask import Flask
from flask_restful import Resource, Api
from googleplaces import GooglePlaces, types


app = Flask(__name__)

API_KEY = ""
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

        data = list()

        for result in query_result.places:
            data.append({
                    "name": result.name,
                    "details": result.get_details(),
                    "latitude": float(result.geo_location["lat"]),
                    "longitude": float(result.geo_location["lng"])
                })
        return data
