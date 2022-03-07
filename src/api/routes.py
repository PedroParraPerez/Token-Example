"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, City, Country
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# Como vamos a repetir en muchas rutas la funcion de get_json en las rutas de creación, creamos una funcion aparte y la llamamos en todas las rutas

def get_json():
    json = request.get_json()
    if json is None:
        raise APIException("No se ha enviado un JSON o no se ha especificado que nos ha enviado un JSON")
    return json

def get_name(json):
    name = json.get("name")
    if name is None:
        raise APIException("El nombre es obligatorio")
    return name


@api.route('/countries', methods=['GET'])
def list_countries():

    countries = Country.query.all()

    return jsonify({'results': list(map(lambda country: country.serialize(), countries))}),200
    
# Creamos un pais con el Fetch del Home CreateCountry utilizando la variable pais que indica el pais
@api.route('/countries/create', methods=['POST'])
def create_countries():

    json = get_json()

    name = json.get("name")
    country = Country(name=name)
    country.save()

    return jsonify(country.serialize()), 200




#Creamos las ciudades igual que los paises SIN UN PAIS ASIGNADO
@api.route('/cities/create', methods=['POST'])
def create_cities():

    json = get_json()

    name = json.get("name")
    city = City(name=name)
    city.save()

    return jsonify(city.serialize()), 200




# CREAMOS LAS CIUDADES CON UN PAIS YA ASIGNADO FUNCIONA PERFECTO ASIGNANDOLE UN PAIS EN CONCRETO
@api.route('/countries/<int:country_id>/cities/create', methods=['POST'])
def create_city_in_country(country_id):
    json = get_json()
    name = get_name(json)

    country = Country.query.get(country_id)
    city = City(name=name)

    country.cities.append(city)
    country.save()

    return jsonify(city.serialize()), 200



# Si queremos mostrar las ciudades de un pais necesitamos poder pedirlo, pero no las quiero todas
# El endpoint es asi, por que primero le digo que pais es exactamente es y despues le digo que ciudad es
@api.route('/countries/<int:country_id>/cities', methods=['GET'])
def list_cities_in_country(country_id):   #Le pasamos el parametro de Country_id para elegir 1 solo pais
    
    country = Country.query.get(country_id)

    return jsonify({'results': list(map(lambda city: city.serialize(), country.cities))}),200 #Ponemos country.cities por que primero se fija en el pais y despues en la ciudad