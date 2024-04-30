import requests

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
        location = geocoding_data['results'][0]['geometry']['location']
        
        # Use Nearby Search API to find businesses near the specified location
        nearby_search_endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        nearby_search_params = {
            "location": f"{location['lat']},{location['lng']}",
            "radius": 10,  # Search within a radius of 500 meters
            "key": api_key
        }
        response = requests.get(nearby_search_endpoint, params=nearby_search_params)
        data = response.json()
        
        if response.status_code == 200 and data.get('results'):
            businesses = []
            for result in data['results']:
                # Exclude results with formatted address exactly "Chicago"
                if result.get('vicinity', '').lower() != "chicago":
                    business_info = {
                        "name": result.get('name'),
                        "formatted_address": result.get('vicinity'),
                        "types": result.get('types'),
                        "place_id": result.get('place_id')
                    }
                    businesses.append(business_info)
            return businesses
    return None

# Example usage
address = "700 S State St"
api_key = "AIzaSyB-3J6J6A4LL6IjnqEStMCnterQpmxT844"
businesses = get_businesses_at_address(address, api_key)
if businesses:
    print("Businesses at this address:")
    for business in businesses:
        print("Name:", business.get('name'))
        print("Formatted Address:", business.get('formatted_address'))
        print("Types:", business.get('types'))
        print("Place ID:", business.get('place_id'))
        print()
else:
    print("No businesses found at this address.")
