from services.api import api, Wikipedia, GoogleApi


def load_resources():
    api.add_resource(Wikipedia, '/wikipedia/<string:wiki_name>')
    api.add_resource(GoogleApi, '/google_api/<float:longitude>&<float:latitude>')
