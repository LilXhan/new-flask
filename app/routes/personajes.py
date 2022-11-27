from flask import Blueprint, render_template
from bson.objectid import ObjectId
import requests
from app.db import db

personaje_router = Blueprint("personaje_router", __name__)


def get_personajes():
    dict_personajes = []
    for x in range(1, 22):
        r = requests.get(f'https://rickandmortyapi.com/api/character?page={x}')
        r = r.json()
        for personaje in r['results']:
            person = {
                'id': personaje['id'],
                'name': personaje['name'],
                'status': personaje['status'],
                'species': personaje['species'],
                'gender': personaje['gender'],
                'img': personaje['image'],
                'location': personaje['location']['name']
            }
            dict_personajes.append(person)
            
    return dict_personajes

@personaje_router.route('/')
def index():
    result = get_personajes()
    db.api_rick_and_morty.insert_many(result)
    return render_template('index.html')


@personaje_router.route('/personaje')
def personajes():
    data = db.api_rick_and_morty.find()
    return render_template('personajes.html', data=data)


@personaje_router.route("/personaje/<id>", methods=['GET','POST'])
def detail_personaje(id):
    personaje = db.api_rick_and_morty.find_one({"_id": ObjectId(id)})
    personaje = dict(personaje)
    return render_template("detalle.html", personaje=personaje)