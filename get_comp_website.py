# Import the modules
import csv
import requests
from bs4 import BeautifulSoup

# Define the input and output files
input_file = "nume_companii_TV_straine.csv"
output_file = "output_companii_cu_web.csv"

# Define the function to scrape any https link that has a word in a list of names from a web page
def scrape_link(name, url):
    # Send a request to the web page and get the response
    response = requests.get(url)
    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all the links in the web page
    links = soup.find_all("a", href=True)
    # Loop through the links
    for link in links:
        # Get the link's href attribute
        href = link["href"]
        # Check if the link is a https link and contains the name
        if href.startswith("https://") and name.lower() in href.lower():
            # Return the link
            return href
    # If no link is found, return None
    return None

# Open the input file and read the list of names
with open(input_file, "r") as input:
    reader = csv.reader(input)
    # Skip the header row
    next(reader)
    # Create a list of names
    names = [row[0] for row in reader]

# Define the web page to scrape from
web_page = "https://www.google.com/search?q=list+of+people+by+name"

# Create a list of links
links = []
# Loop through the list of names
for name in names:
    # Scrape the link using the function
    link = scrape_link(name, web_page)
    # Append the link to the list
    links.append(link)

# Open the output file and write the links
with open(output_file, "w") as output:
    writer = csv.writer(output)
    # Write the header row
    writer.writerow(["Name", "Link"])
    # Write the name and link pairs
    for i in range(len(names)):
        writer.writerow([names[i], links[i]])
