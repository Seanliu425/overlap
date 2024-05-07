import requests
from difflib import SequenceMatcher

def fuzzy_match(address1, address2):
    # Calculate similarity score between two addresses using SequenceMatcher
    return SequenceMatcher(None, address1.lower(), address2.lower()).ratio()

def get_businesses_at_address(address, api_key):
    # Use Geocoding API to get latitude and longitude for the address
    geocoding_endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    geocoding_params = {
        "address": address,
        "key": api_key
    }
    geocoding_response = requests.get(geocoding_endpoint, params=geocoding_params)
    geocoding_data = geocoding_response.json()
    
    if geocoding_response.status_code == 200 and geocoding_data.get('results'):
        input_address = geocoding_data['results'][0]['formatted_address']
        location = geocoding_data['results'][0]['geometry']['location']
        
        # Use Nearby Search API to find businesses near the specified location
        nearby_search_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        nearby_search_params = {
            "location": f"{location['lat']},{location['lng']}",
            "radius": 500,  # Search within a radius of 500 meters
            "key": api_key
        }
        response = requests.get(nearby_search_endpoint, params=nearby_search_params)
        data = response.json()
        
        if response.status_code == 200 and data.get('results'):
            relevant_results = []
            for result in data['results']:
                formatted_address = result.get('vicinity', '').lower()
                # Exclude results with formatted address exactly "Chicago"
                if formatted_address != "chicago" and fuzzy_match(input_address, formatted_address) > 0.8:
                    business_info = {
                        "name": result.get('name'),
                        "formatted_address": formatted_address,
                        "types": result.get('types'),
                        "place_id": result.get('place_id')
                    }
                    relevant_results.append(business_info)
            if relevant_results:
                return [relevant_results[0]]  # Return the most relevant result
    return None

# Example usage
address = "1145 W Wilson Ave, Chicago, IL"
api_key = "YOUR_API_KEY"
businesses = get_businesses_at_address(address, api_key)
if businesses:
    print("Business at this address:")
    business = businesses[0]  # Get the only result in the list
    print("Name:", business.get('name'))
    print("Formatted Address:", business.get('formatted_address'))
    print("Types:", business.get('types'))
    print("Place ID:", business.get('place_id'))
else:
    print("No businesses found at this address.")
