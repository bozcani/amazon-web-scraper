import urllib.request as urllib
from bs4 import BeautifulSoup
import requests

def get_productIDs(url):
    url = url[:-1] # Ignore last character. Because it is 

    # Create fake browser info.
    header = {'Connection': 'keep-alive',
                'Expires': '-1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
                }    

    # Get response from Amazon.            
    response = requests.get(url, headers=header)

    # Create soup instance.
    soup = BeautifulSoup(response.text, 'lxml')

    # Product ids that will be returned.
    product_ids = [] 

    # Extract product id.
    for div in soup.select('div[data-asin]'):
        product_id = (div['data-asin'], div.get_text(strip=True))[0] # First 10 characters indicate product id.
        product_ids.append(product_id) # Add a product id to the list.

    return product_ids

# Read links from a file.
link_file = open("links.txt", "r")

# Create a file to write product ids.
out_file = open("product-IDs.txt", "w+")

# Read each line in the link file and extract product ids.
for line in link_file.readlines():
    product_ids = get_productIDs(line)
    for p_id in product_ids:
        out_file.write(p_id+"\n")

out_file.close()    