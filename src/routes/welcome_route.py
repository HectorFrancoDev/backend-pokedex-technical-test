from flask import Blueprint, render_template

# Create a new blueprint for root route
welcome_bp = Blueprint("/", __name__)

# Route that returns a welcome message
@welcome_bp.route("/", methods=["GET"])
def get_all_pokemon():
    return render_template('index.html')
    