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
        """Prueba que la ruta '/pokemon' devuelve todos los Pokémon correctamente."""
        # Configura el comportamiento simulado de la solicitud HTTP
        mock_requests_get.return_value.status_code = 200
        # Realiza una solicitud GET a la ruta '/pokemon'
        response = self.test_app.get("/pokemon")

        # Verifica que la solicitud sea exitosa (código de estado 200) y devuelve datos de Pokémon
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    @patch("src.server")
    def test_get_pokemon_by_name_success(self, mock_requests_get):
        """Prueba que la ruta '/pokemon/<name>' devuelve un Pokémon por su nombre correctamente."""
        # Configura el comportamiento simulado de la solicitud HTTP
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {
            "id": 1,
            "name": "bulbasaur",
            "types": ["grass", "poison"],
            "abilities": ["overgrow"],
            "sprites": {"front_default": "url-to-image"},
        }

        # Realiza una solicitud GET a la ruta '/pokemon/bulbasaur'
        response = self.test_app.get("/pokemon/bulbasaur")

        # Verifica que la solicitud sea exitosa (código de estado 200) y devuelve datos del Pokémon
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
