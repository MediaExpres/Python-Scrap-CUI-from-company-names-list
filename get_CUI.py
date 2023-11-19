# # Import the libraries
# import requests
# from bs4 import BeautifulSoup
# import csv

# # Open the CSV file with company names
# with open('nume_companii_TV.csv', 'r') as input_file:
#     # Create a CSV reader object
#     reader = csv.reader(input_file)
#     # Skip the header row
#     next(reader)
#     # Open a new CSV file to write the output
#     with open('output_TV.csv', 'w') as output_file:
#         # Create a CSV writer object
#         writer = csv.writer(output_file)
#         # Write the header row
#         writer.writerow(['Company Name', 'CUI'])
#         # Loop through each row in the input file
#         for row in reader:
#             # Get the company name
#             company_name = row[0]
#             # Construct the URL for the search query
#             url = 'https://listafirme.ro/' + company_name
#             # Make a GET request to the URL
#             response = requests.get(url)
#             # Check if the response is successful
#             if response.status_code == 200:
#                 # Parse the HTML content
#                 soup = BeautifulSoup(response.text, 'html.parser')
#                 # Find the elements that match the classes
#                 box_date = soup.find(class_='box_date-firma')
#                 subtitle_content = soup.find(class_='subtitle_content text-white')
#                 # Check if the elements are not None
#                 if box_date and subtitle_content:
#                     # Get the text content of the elements
#                     box_date_text = box_date.get_text()
#                     subtitle_content_text = subtitle_content.get_text()
#                     # Check if the text content matches the company name
#                     if company_name in box_date_text and company_name in subtitle_content_text:
#                         # Find the element that has the title attribute
#                         title_element = box_date.find(title=True)
#                         # Check if the element is not None
#                         if title_element:
#                             # Get the value of the title attribute
#                             title_value = title_element['title']
#                             # Split the title value by '-'
#                             title_parts = title_value.split('-')
#                             # Check if the title value has two parts
#                             if len(title_parts) == 2:
#                                 # Get the second part, which is the CUI
#                                 cui = title_parts[1].strip()
#                                 # Write the company name and the CUI to the output file
#                                 writer.writerow([company_name, cui])
#                                 # Print a message
#                                 print(f'Found CUI for {company_name}: {cui}')
#                             else:
#                                 # Print a message
#                                 print(f'Could not find CUI for {company_name}')
#                         else:
#                             # Print a message
#                             print(f'Could not find CUI for {company_name}')
#                     else:
#                         # Print a message
#                         print(f'Could not find CUI for {company_name}')
#                 else:
#                     # Print a message
#                     print(f'Could not find CUI for {company_name}')
#             else:
#                 # Print a message
#                 print(f'Could not find CUI for {company_name}')
