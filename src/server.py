from flask import Flask
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv
from .routes import pokemon_bp
from .routes import welcome_bp


class Server:
    def __init__(self):
        """Constructor method __init__"""
        # Load the environment variables
        load_dotenv()
        # Create Flask app
        self.app = Flask(__name__)
        # Activate CORS
        CORS(self.app)
        # Load Blueprints
        self.blueprints()

    def blueprints(self) -> None:
        """Load all the Blueprints"""
        self.app.register_blueprint(welcome_bp, url_prefix="/")
        self.app.register_blueprint(pokemon_bp, url_prefix="/api")

    def run(self) -> None:
        """Runs the Flask server."""

        # Uncomment this line to run at localhost
        # self.app.run(debug=True)

        # Leave this uncommented to run it at Production mode
        http_server = WSGIServer(("", 5000), self.app)
        http_server.serve_forever()
