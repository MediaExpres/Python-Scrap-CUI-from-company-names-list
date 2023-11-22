# Import the modules
from googlesearch import search
import csv

# Define the input and output files
input_file = "nume_companii_TV_straine.csv"
output_file = "nume_companii_TV_straine_cu_web.csv"

# Define the function to search for any https link that has a word in a list of names using Google
def search_link(name):
    # Construct the Google search query
    query = name + " site:.com OR site:.net OR site:.ro OR site:.org OR site:.tv OR site:.eu"
    # Use the search function to get the Google search results
    results = search(query, num=10, stop=10, pause=2)
    # Loop through the results
    for result in results:
        # Check if the result is a https link and contains the name
        if result.startswith("https://") and name.lower() in result.lower():
            # Return the result
            return result
    # If no result is found, return None
    return None

# Open the input file and read the list of names
with open(input_file, "r") as input:
    reader = csv.reader(input)
    # Skip the header row
    next(reader)
    # Create a list of names
    names = [row[0] for row in reader]

# Create a list of links
links = []
# Loop through the list of names
for name in names:
    # Search for the link using the function
    link = search_link(name)
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