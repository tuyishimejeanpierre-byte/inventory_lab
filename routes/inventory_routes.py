from flask import Blueprint
from flask import jsonify

from services.inventory_service import InventoryService
from flask import Blueprint, jsonify, request

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
@inventory_bp.route("/inventory", methods=["POST"])
def add_product():

    data = request.get_json()

    product = inventory_service.add_product(
        barcode=data["barcode"],
        product_name=data["product_name"],
        brand=data["brand"],
        quantity=data["quantity"],
        buying_price=data["buying_price"],
        selling_price=data["selling_price"]
    )

    return jsonify(product), 201