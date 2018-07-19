import pprint
import wikipedia
import json

from flask import Flask, request
from googleplaces import GooglePlaces, types, lang


wikipedia.set_lang("fr")

app = Flask(__name__)

API_KEY = 'AIzaSyAadpx8ImSags8ItAgCseBKfVRnTv046tA'
google_places = GooglePlaces(API_KEY)

#43.624378
#1.388731

@app.route("/get_wiki", methods=["GET"])
def get_wiki():
    wiki_name = request.args.get("search")
    result = wikipedia.search(wiki_name)
    result = wikipedia.page(result[0])

    return "<p>{0}</p>".format(repr(result.content))

@app.route("/get_places", methods=["GET"])
def get_places():
    longitude = float(request.args.get("long"))
    latitude = float(request.args.get("lat"))
    radius = float(request.args.get("radius"))
    types_param = request.args.get("types")

    query_result = google_places.nearby_search(
        lat_lng={"lat": latitude, "lng": longitude},
        radius=5000,
        types=[types.TYPE_CHURCH]
    )

    results = [[a.name, float(a.geo_location["lat"]), float(a.geo_location["lng"])] for a in query_result.places]

    return json.dumps(results)

@app.route('/')
def hello_world():

    pp = pprint.PrettyPrinter(indent=4)

    """
    query_result = google_places.nearby_search(
            lat_lng={"lat": 43.624378, "lng": 1.388731},
            radius=5000,
            types=[types.TYPE_CHURCH]
        )

    types.TYPE_AQUARIUM, types.TYPE_ART_GALLERY, types.TYPE_CEMETERY, types.TYPE_CHURCH,
    types.TYPE_EMBASSY, types.TYPE_HINDU_TEMPLE, types.TYPE_MOSQUE, types.TYPE_MUSEUM,
    types.TYPE_PARK, types.TYPE_STADIUM, types.TYPE_SYNAGOGUE, types.TYPE_UNIVERSITY,
    types.TYPE_ZOO,

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
    """

    result = wikipedia.search("Basilique Saint-Sernin de Toulouse")

    result = wikipedia.page(result[0])

    #pp.pprint(result)

    return "<p>{0}</p>".format(repr(result.content))


if __name__ == '__main__':
    app.run()
