import requests

class PostcodeAPIClient:
    BASE_URL = "https://api.postcodes.io/postcodes"

    def get_postcode(self, latitude, longitude):
        """Captura el código postal más cercano a las coordenadas dadas"""
        response = requests.get(f"{self.BASE_URL}?lon={longitude}&lat={latitude}")
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 200 and data['result']:
                return data['result'][0]['postcode']
            else:
                return None
        else:
            raise Exception(f"API error: {response.status_code}, {response.text}")
