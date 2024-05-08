import unittest
from flask import Flask, jsonify
from app1 import app


class TestHelloBartek(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_bartek(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello Bartek!")

    def test_hello_bartek_specific_method(self):
        response = self.app.get("/", method="GET")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello Bartek!")

    def test_hello_bartek_specific_query_param(self):
        response = self.app.get("/?name=John")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello Bartek!")

    def test_hello_bartek_specific_header(self):
        headers = {"Content-Type": "application/json"}
        response = self.app.get("/", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello Bartek!")


if __name__ == "__main__":
    unittest.main()
