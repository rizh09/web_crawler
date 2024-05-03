import csv
import requests
from bs4 import BeautifulSoup

def append_domain(url):
    if url and not url.startswith("http://") and not url.startswith("https://"):
        url = "https://www.aia.com.hk/" + url
    return url

url = "https://www.aia.com.hk/en/sitemap"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <a> elements, <button>, and <img> with the specified CSS selector
links = soup.select('a, button, img[style="padding-right: 0px; overflow: unset;"]')

# Create a list to store the extracted data
data = []

# Extract the relevant information from the elements
for link in links:
    if link.name == 'a':
        element_type = 'Hyperlink'
        element_text = link.text.strip()
        #element_href = link['href'] if 'href' in link.attrs and link['href'].startswith(('http', 'https', '/en', '/zh')) else ''
        element_href = link['href'] if 'href' in link.attrs and link['href'] and link['href'].startswith(('http', 'https', '/en', '/zh-hk')) else ''
        element_link = link
    else:
        continue

    # Append the extracted data to the list
    element_href = append_domain(element_href)

    data.append([element_type, element_text, element_href, element_link])

# Define the output CSV file name
csv_file = 'scraped_data.csv'


# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Element Type', 'Text', 'URL','Raw'])
    writer.writerows(data)

print(f"Scraped data saved to {csv_file}")

