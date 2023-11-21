import csv
import requests
from bs4 import BeautifulSoup
import time

def find_website(company):
    # Function to find the website of a company using web scraping

    search_url = f"https://www.google.com/search?q={company} website"
    
    try:
        # Send an HTTP request to Google and get the HTML response
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the first search result link (assuming it's the company's website)
        result = soup.find('div', {'class': 'BNeawe UPmit AP7Wnd'})
        if result:
            return result.text

    except requests.RequestException as e:
        print(f"Error finding website for {company}: {e}")
    
    return None

def main(input_csv, output_csv):
    # Read the input CSV file
    with open(input_csv, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Assuming the first row contains headers
        companies = [row[0] for row in reader]  # Assuming company names are in the first column

    # Find websites for each company
    results = []
    for company in companies:
        website = find_website(company)
        results.append({'Company': company, 'Website': website})

        # Introduce a delay between requests to avoid rate limits
        time.sleep(2)  # Adjust the delay time as needed

    # Write results to a new CSV file
    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['Company', 'Website'])
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    input_csv = "nume_companii_TV_straine.csv]"  # Replace with the path to your input CSV file
    output_csv = "output_companii_TV_straine_with_websites.csv"  # Replace with the desired output CSV file path

    main(input_csv, output_csv)
