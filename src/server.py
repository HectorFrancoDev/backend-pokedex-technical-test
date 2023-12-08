from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .routes import pokemon_bp

class Server:
    def __init__(self):
        """Constructor method __init__
        """
        # Load the environment variables
        load_dotenv()
        # Create Flask app
        self.app = Flask(__name__)
        CORS(self.app)
        # Blueprint 
        self.blueprints()

    def blueprints(self):
        """_summary_
        
        """
        self.app.register_blueprint(pokemon_bp, url_prefix='/api')

    def run(self):
        """_summary_
        """
        self.app.run(debug=True)
