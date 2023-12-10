from flask import Blueprint, request, jsonify
import os
import requests
from ..models import Pokemon


# ENDPOINT URL
URL = os.environ.get("ENDPOINT", "")

# Crea el blueprint para la API
pokemon_bp = Blueprint("/api", __name__)


# La ruta que devuelve todos los Pokémon
@pokemon_bp.route("/pokemon", methods=["GET"])
def get_all_pokemon():
    """Get and list all Pokémons available

    Returns:
        JSON: Returns the data in JSON format
    """
    query = request.args.to_dict(flat=False)

    # Realiza la solicitud HTTP a la API de PokeAPI
    response = requests.get(URL, params=query)

    # Si la solicitud fue exitosa
    if response.status_code == 200:
        # Devuelve los datos de todos los Pokémon
        return jsonify(response.json().get("results", [])), 200
    else:
        # Devuelve un mensaje de error
        return {"error": "No se pudo obtener los Pokémones"}, 404


# La ruta que devuelve un Pokémon por su ID o nombre
@pokemon_bp.route("/pokemon/<string:name>", methods=["GET"])
def get_pokemon_by_name(name):
    """Get an specific Pokémon by ID or name:
       ID, name, types, abilities, sprites

    Args:
        name (string): The name or the ID to search

    Returns:
        Pokemon: Returns the data in JSON format
    """

    # Realiza la solicitud HTTP a la API de PokeAPI
    response = requests.get(f"{URL}/{name.strip()}")

    # Si la solicitud fue exitosa
    if response.status_code == 200:
        # Devuelve los datos del Pokémon
        id = response.json()["id"]
        name = response.json()["name"]
        types = response.json()["types"]
        abilities = response.json()["abilities"]
        sprites = response.json()["sprites"]

        pokemon = Pokemon(id, name, types, abilities, sprites)

        return jsonify(pokemon.to_json()), 200

    else:
        # Devuelve un mensaje de error
        return {"error": f"No se encontró el Pokémon {name}"}, 404
