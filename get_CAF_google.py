# Import the modules
import csv
import requests
from bs4 import BeautifulSoup

# Define the input and output files
input_file = "nume_companii_cablu.csv"
output_file = "CAF_CABLU.csv"

# Define the base URL for Google Search
base_url = "https://www.google.com/search?q="

# Define the query term for Cifra Afaceri
query_term = "Cifra de afaceri (CA) "

# Create an empty list to store the results
results = []

# Open the input file and read the company names
with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        # Get the company name
        company = row[0]
        # Construct the full query URL
        query_url = base_url + company + "+" + query_term
        # Make a request to the query URL
        response = requests.get(query_url)
        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        # Find the first element that contains the Cifra Afaceri
      
        element = soup.find(string=lambda t: query_term in t)

        # If the element is found, extract the Cifra Afaceri
        if element:
            cifra_afaceri = element.strip()
        # Otherwise, assign a default value
        else:
            cifra_afaceri = "N/A"
        # Append the company name and the Cifra Afaceri to the results list
        results.append([company, cifra_afaceri])

# Open the output file and write the results
with open(output_file, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(["Company", "Cifra Afaceri"])
    # Write the results
    writer.writerows(results)
