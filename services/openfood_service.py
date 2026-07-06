import requests


class OpenFoodService:
    BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

    def search_by_barcode(self, barcode):
        url = f"{self.BASE_URL}/{barcode}.json"

        headers = {
            "User-Agent": "InventoryManagement/1.0 (student project)"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                return None

            data = response.json()

            if data.get("status") != 1:
                return None

            product = data.get("product", {})

            return {
                "barcode": barcode,
                "product_name": product.get("product_name"),
                "brand": product.get("brands"),
                "ingredients": product.get("ingredients_text"),
            }

        except requests.RequestException:
            return None