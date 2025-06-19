import googlemaps
import os

class GoogleMapsAgent:
    def __init__(self):
        self.client = googlemaps.Client(key=os.environ["GOOGLE_MAPS_API_KEY"])

    def find_hospitals(self, disease: str, location: str, radius=5000):
        query = f"find hospital for {disease} in {location}"
        places = self.client.places(query=query, location=location, radius=radius, type='hospital')
        results = places.get('results', [])
        return results
    
    def get_address(self, latitude, longitude):
        geocode_result = self.client.reverse_geocode((latitude, longitude))
        address = geocode_result[0]['formatted_address']
        return address