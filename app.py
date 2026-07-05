from flask import Flask

from config import Config
from routes.inventory_routes import inventory_bp
from routes.external_routes import external_bp




app = Flask(__name__)

app.register_blueprint(external_bp)

app.config.from_object(Config)

app.register_blueprint(inventory_bp)


@app.route("/")
def home():

    return {
        "message": "Inventory Management API running."
    }


if __name__ == "__main__":
    app.run(debug=True)