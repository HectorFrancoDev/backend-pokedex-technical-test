import unittest
from unittest.mock import patch
from flask import Flask
from src.server import Server


class TestServerClass(unittest.TestCase):
    
    def setUp(self) -> None:
        """Initial setup for the tests."""
        self.server = Server()
    
    def test_constructor(self):
        """Test that the constructor initializes the Flask application correctly."""
        self.assertIsInstance(self.server.app, Flask)

    @patch("src.server.CORS")
    def test_cors_activation(self, mock_cors):
        """Test that CORS is activated during initialization."""
        self.server.__init__()  # Activate CORS
        mock_cors.assert_called_once_with(self.server.app)

    @patch("src.server.Flask.run")
    def test_run_method(self, mock_run):
        """Test that the Flask run method is called correctly."""
        self.server.run()
        mock_run.assert_called_once_with(debug=True)


if __name__ == "__main__":
    unittest.main()
