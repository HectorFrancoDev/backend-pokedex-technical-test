import unittest
from unittest.mock import patch
from flask import Flask
from src.server import Server


class TestServerClass(unittest.TestCase):
    
    def setUp(self) -> None:
        """Configuración inicial para las pruebas."""
        
        self.server = Server()
    
    def test_constructor(self):
        """Prueba que el constructor inicialice correctamente la aplicación Flask."""
        self.assertIsInstance(self.server.app, Flask)

    @patch("src.server.CORS")
    def test_cors_activation(self, mock_cors):
        """Prueba que CORS se activa durante la inicialización."""
        self.server.__init__()  # Vuelve a inicializar para activar CORS
        mock_cors.assert_called_once_with(self.server.app)

    @patch("src.server.Flask.run")
    def test_run_method(self, mock_run):
        """Prueba que el método run de Flask se llama correctamente."""
        self.server.run()
        mock_run.assert_called_once_with(debug=True)


if __name__ == "__main__":
    unittest.main()
