# Import the modules
import csv
import requests
from bs4 import BeautifulSoup
import json

# Define the input and output files
input_file = "nume_companii_TV_straine.csv"
output_file = "nume_companii_TV_straine_cu_web.csv"

# Define the function to search for a company's website using Google
def search_website(company):
    # Construct the Bing search query
    query = company + " site:.com"
    # Use the search_web tool to get the Bing search results
    results = requests.get("https://www.bing.com/search?q=" + query).text
    # Parse the results using JSON
    soup = BeautifulSoup(results, "html.parser")
    results = soup.find_all("li", class_="b_algo")
    # Find the first result that has a .com domain
    for result in results:
        link = result.find("a")["href"]
        if link.endswith(".com/") or link.endswith(".com"):
            # Return the website link
            return link
    # If no website is found, return None
    return None

# Open the input file and read the company names
with open(input_file, "r") as input:
    reader = csv.reader(input)
    # Skip the header row
    next(reader)
    # Create a list of company names
    companies = [row[0] for row in reader]

# Create a list of websites
websites = []
# Loop through the company names
for company in companies:
    # Search for the website using the function
    website = search_website(company)
    # Append the website to the list
    websites.append(website)

# Open the output file and write the websites
with open(output_file, "w") as output:
    writer = csv.writer(output)
    # Write the header row
    writer.writerow(["Company", "Website"])
    # Write the company and website pairs
    for i in range(len(companies)):
        writer.writerow([companies[i], websites[i]])
