import pandas as pd

def get_businesses_at_address(address, api_key):
    # Implementation of get_businesses_at_address function from the previous code snippet
    pass

# Function to process addresses in the CSV file
def process_addresses(input_csv, output_csv, api_key):
    # Read input CSV file into DataFrame
    df = pd.read_csv(input_csv)
    
    # Add a new column for business information
    df['Business Information'] = ""
    
    # Process each address
    for index, row in df.iterrows():
        address = row['Address']
        businesses = get_businesses_at_address(address, api_key)
        if businesses:
            business_info = ", ".join([f"{b['name']} ({b['formatted_address']})" for b in businesses])
            df.at[index, 'Business Information'] = business_info
    
    # Save DataFrame with updated information to output CSV file
    df.to_csv(output_csv, index=False)

# Example usage
input_csv = "input_addresses.csv"
output_csv = "output_addresses.csv"
api_key = "YOUR_API_KEY"
process_addresses(input_csv, output_csv, api_key)
