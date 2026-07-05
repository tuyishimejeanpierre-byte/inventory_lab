from flask import Blueprint, jsonify, request

from services.openfood_service import OpenFoodService


external_bp = Blueprint("external", __name__)

openfood_service = OpenFoodService()


@external_bp.route("/search", methods=["GET"])
def search_product():

    barcode = request.args.get("barcode")

    if not barcode:
        return jsonify({"error": "barcode is required"}), 400

    product = openfood_service.search_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200