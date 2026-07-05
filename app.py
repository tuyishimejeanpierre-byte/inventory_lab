from flask import Flask

from config import Config
from routes.inventory_routes import inventory_bp

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(inventory_bp)


@app.route("/")
def home():

    return {
        "message": "Inventory Management API running."
    }


if __name__ == "__main__":
    app.run(debug=True)