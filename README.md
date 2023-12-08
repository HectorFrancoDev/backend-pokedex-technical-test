# Pokedex - Technical Test MISO (API Documentation)

This API provides access to data about Pokémon from the official Pokémon API.

---
- Author: Héctor Franco
- website: <https://hectorfranco.dev>
- email: <contact@hectorfranco.dev>
- Created on: Dec 10th 2023
___

## Endpoints

### GET /api/pokemon

* **Description:** Retrieves a list of all Pokémon.
* **Parameters:**
    * `limit`: (Optional) Number of Pokémon to retrieve (default: 20).
    * `offset`: (Optional) Number from looking for Pokemon.
* **Response:**
    * `results`: Array of objects containing basic Pokémon data:    name and URL (resource).

### GET /api/pokemon/<string:name>

* **Description:** Retrieves data for a specific Pokémon.
* **Parameters:**
    * `name`: The ID or the name of the Pokémon.
* **Response:**
    * Object containing detailed Pokémon information:
      id, name, types, abilities, sprites.

## Example Usage

### Get all Pokémon:

Get the first 20 Pokemon
```bash
curl -X GET http://localhost:5000/api/pokemon
```
Get the first 40 Pokemon
```bash
curl -X GET http://localhost:5000/api/pokemon?limit=40
```
Starts brining the list since the Pokemon #15 (15 to 35)
```bash
curl -X GET http://localhost:5000/api/pokemon?offset=15
```
Brings 10 Pokeomon starting at position #40 (40 to 50)
```bash
curl -X GET http://localhost:5000/api/pokemon?limit=10&offset=40
```
### Get an specific Pokémon:

```bash
curl -X GET http://localhost:5000/api/pokemon/1
```