import unittest
from unittest.mock import patch

from CLI.cli import view_inventory


class TestCLI(unittest.TestCase):

    @patch("CLI.cli.requests.get")
    def test_view_inventory(self, mock_get):

        mock_get.return_value.json.return_value = [
            {"id": 1, "product_name": "Milk"}
        ]

        result = view_inventory()

        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()