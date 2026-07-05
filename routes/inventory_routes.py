from flask import Blueprint
from flask import jsonify

from services.inventory_service import InventoryService


inventory_bp = Blueprint(
    "inventory",
    __name__
)

inventory_service = InventoryService()


@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():

    inventory = inventory_service.get_inventory()

    return jsonify(inventory), 200

@inventory_bp.route("/inventory/<int:product_id>", methods=["GET"])
def get_product(product_id):

    product = inventory_service.get_product(product_id)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200