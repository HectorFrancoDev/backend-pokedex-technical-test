import unittest
from flask import Flask
from unittest.mock import patch, Mock
from src.server import Server
from src.routes.pokemon_route import pokemon_bp


class PokemonBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        """Initial configuration for the Unit Tests Set."""
        self.server = Server()
        self.app = self.server.app
        self.test_app = self.app.test_client()

    @patch("src.server")
    def test_get_all_pokemon_success(self, mock_requests_get):
        """Test that the '/pokemon' route returns all Pokémon."""
        # Set up the simulated behavior of the HTTP request
        mock_requests_get.return_value.status_code = 200
        # Make a GET request to the '/pokemon' route
        response = self.test_app.get("/pokemon")

        # Verify that the request is successful (status code 200) and returns Pokémon data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    @patch("src.server")
    def test_get_pokemon_by_name_success(self, mock_requests_get):
        """Test that the '/pokemon/<name>' route returns a Pokémon by its name successfully."""
        # Set up the simulated behavior of the HTTP request
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {
            "id": 1,
            "name": "bulbasaur",
            "types": ["grass", "poison"],
            "abilities": ["overgrow"],
            "sprites": {"front_default": "url-to-image"},
        }

        # Make a GET request to the '/pokemon/bulbasaur' route
        response = self.test_app.get("/pokemon/bulbasaur")

        # Verify that the request is successful (status code 200) and returns Pokémon data
        self.assertEqual(response.status_code, 200)
        expected_json = {
            "id": 1,
            "name": "bulbasaur",
            "types": ["grass", "poison"],
            "abilities": ["overgrow"],
            "sprites": {"front_default": "url-to-image"},
        }
        self.assertEqual(response.json, expected_json)


if __name__ == "__main__":
    unittest.main()
