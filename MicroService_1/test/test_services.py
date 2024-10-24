import unittest
from app import app

class TestMicroservice1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_upload_csv(self):
        with open('test_coordinates.csv', 'rb') as f:
            response = self.app.post('/upload_csv', data={'file': f})
            self.assertEqual(response.status_code, 200)