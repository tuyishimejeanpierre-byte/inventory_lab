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