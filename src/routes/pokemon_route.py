from flask import Blueprint, request, jsonify
import os
import requests
from ..models import Pokemon


# ENDPOINT URL
URL = os.environ.get("ENDPOINT", "")

# Create the Blueprint /api route
pokemon_bp = Blueprint("/api", __name__)


# Returns all the Pokemon
@pokemon_bp.route("/pokemon", methods=["GET"])
def get_all_pokemon():
    """Get and list all Pokémons available

    Returns:
        JSON: Returns the data in JSON format
    """
    query = request.args.to_dict(flat=False)

    # Make the HTTPS request to the Pokedex ENDPOINT
    response = requests.get(URL, params=query)

    # If the request succeed
    if response.status_code == 200:
        # Returns the Pokemon list in JSON form
        return jsonify(response.json().get("results", [])), 200
    else:
        # Returns an error in JSON format
        return {"error": "No se pudo obtener los Pokémones"}, 404


# Returns an specific Pokemon information
@pokemon_bp.route("/pokemon/<string:name>", methods=["GET"])
def get_pokemon_by_name(name):
    """Get an specific Pokémon by ID or name:
       ID, name, types, abilities, sprites

    Args:
        name (string): The name or the ID to search

    Returns:
        Pokemon: Returns the data in JSON format
    """

    # Make the HTTPS request to the Pokedex ENDPOINT
    response = requests.get(f"{URL}/{name.strip()}")

    # If the request succeed
    if response.status_code == 200:
        id = response.json()["id"]
        name = response.json()["name"]
        types = response.json()["types"]
        abilities = response.json()["abilities"]
        sprites = response.json()["sprites"]

        # Instance a Pokemon() object
        pokemon = Pokemon(id, name, types, abilities, sprites)

        # Returns the Pokemon info in JSON format
        return jsonify(pokemon.to_json()), 200

    else:
        # Returns an error in JSON format
        return {"error": f"No se encontró el Pokémon {name}"}, 404
