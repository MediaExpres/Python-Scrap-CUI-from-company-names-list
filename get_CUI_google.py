# Import the libraries
from googlesearch import search
import csv

# Open the CSV file with company names
with open('nume_companii_cablu.csv', 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)
    # Skip the header row
    next(reader)
    # Open a new CSV file to write the output
    with open('output.csv', 'w') as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)
        # Write the header row
        writer.writerow(['Company Name', 'CUI'])
        # Loop through each row in the input file
        for row in reader:
            # Get the company name
            company_name = row[0]
            # Search for the company CUI using Google
            query = company_name + " CUI"
            results = search(query, num=1, stop=1)
            # Try to get the first result
            try:
                website = next(results)
                # Print the website
                print(f"Website of {company_name}: {website}")
                # Split the website by '-'
                website_parts = website.split('-')
                # Get the last part, which is the CUI
                cui = website_parts[-1].strip()
                # Try to convert the CUI to an integer
                try:
                    
                    # Write the company name and the CUI to the output file
                    writer.writerow([company_name, cui])
                    # Print a message
                    print(f'Found CUI for {company_name}: {cui}')
                except ValueError:
                    # Print a message
                    print(f'CUI for {company_name} is not an integer')
                    # Write the company name and CUI not found to the output file
                    writer.writerow([company_name, 'CUI not found'])
            except StopIteration:
                # Print a message
                print(f'No results found for {company_name}')
                # Write the company name and CUI not found to the output file
                writer.writerow([company_name, 'CUI not found'])
