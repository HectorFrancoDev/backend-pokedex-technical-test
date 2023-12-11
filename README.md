# Pokedex - Technical Test MISO
---
- Author: Héctor Franco
- website: <https://hectorfranco.dev>
- email: <contact@hectorfranco.dev>
- Last edit: Dec 10th 2023
- Postman Documentation: [Postman API Production](https://documenter.getpostman.com/view/31664787/2s9Ykhg4W4)
- Server on Production mode: <https://backend-pokedex-technical-test.onrender.com/>
___

## Setup and run
Before executing this server, you must setup correctly the project. Follow the steps down below to configure the server.

### Create environment
```bash
$bash: python3 -m venv venv
```
### Activate environment

#### Mac users
```bash
$bash: source venv/bin/activate
```
#### Windows users
```bash
cmd: .\venv\scripts\activate
```
### Install dependencies
```bash
$bash pip install -r requirements.txt 
```

### Create .env file
Create an **.env** file at the root of the project with the environment variable. See __.env.example file__ 

### Run server
```bash
$bash: python3 app.py
```

After that, a local server will start running on http://127.0.0.1:5000

___

## API Documentation

This API provides access to data about Pokémon from the official Pokémon API.

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
    * `JSON`: Object containing detailed Pokémon information:
      id, name, types, abilities, sprites.

### Example Usage

#### Get all Pokémon:

Get the first 20 Pokemon
```bash
$bash: curl -X GET http://localhost:5000/api/pokemon
```
Get the first 40 Pokemon
```bash
$bash: curl -X GET http://localhost:5000/api/pokemon?limit=40
```
Starts brining the list since the Pokemon #15 (15 to 35)
```bash
$bash: curl -X GET http://localhost:5000/api/pokemon?offset=15
```
Brings 10 Pokeomon starting at position #40 (40 to 50)
```bash
$bash: curl -X GET http://localhost:5000/api/pokemon?limit=10&offset=40
```
#### Get an specific Pokémon:

```bash
$bash: curl -X GET http://localhost:5000/api/pokemon/1
```
___

## Unit Tests
Unit tests can be found at *src.tests*. Here are the steps to running them.

### Install pytest or unittest
```bash
$bash: pip3 install pytest
```
Unittest should be installed before and can be execute as a module
### Execute the Unit Tests
#### pytest
```bash
$bash: pytest
```
#### Unittest
```bash
$bash: python3 -m unittest
```
