"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, City, Country
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/countries', methods=['GET'])
def list_countries():

    countries = Country.query.all()

    return jsonify({'results': list(map(lambda country: country.serialize(), countries))}),200
    

@api.route('/countries/create', methods=['POST'])
def create_countries():

    json = request.get_json()
    if json is None:
        return jsonify({"error": "Nose ha enviado un JSON o no se ha especificado que se nos ha envbiado un JSON"}), 400

    name = json.get("name")
    country = Country(name=name)

    return jsonify(country.serialize()), 200