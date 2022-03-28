import unittest
import requests


class APITest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:9000"

    def test_base_method(self):
        response = requests.get(self.base_url)
        self.assertEqual(500, response.status_code)

    def test_get_method(self):
        json_response = {
            "bin": "469346",
            "brand": "VISA",
            "type": "",
            "category": "",
            "issuer": "",
            "alpha_2": "US",
            "alpha_3": "USA",
            "country": "United States",
            "latitude": "37.0902",
            "longitude": "-95.7129",
            "bank_phone": "",
            "bank_url": ""
        }
        response = requests.get("http://localhost:9000/cards/469346469346469346")
        self.assertEqual(200, response.status_code)
        self.assertEqual(json_response, response.json())

    def test_get_method_with_str(self):
        response = requests.get("http://localhost:9000/cards/str93463333242122")
        self.assertEqual(500, response.status_code)

    def test_get_method_with_min(self):
        response = requests.get("http://localhost:9000/cards/4")
        self.assertEqual(500, response.status_code)

    def test_get_method_with_max(self):
        response = requests.get("http://localhost:9000/cards/4232333222223312322222222")
        self.assertEqual(500, response.status_code)


if __name__ == "__main__":
    unittest.main()
