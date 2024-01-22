import requests
from bs4 import BeautifulSoup
from mudah import *
import pandas as pd

# Set the base URL and page parameter
base_url = "https://www.mudah.my/neighbouring-kuala-lumpur/properties-for-sale"
# base_url = "https://www.mudah.my/neighbouring-kuala-lumpur/motorcycles-for-sale?q=fz150"

page_param = "o"

# Set the number of pages you want to scrape
num_pages = 2

# List to store scraped data
main_DF = pd.DataFrame()

for page in range(1, num_pages + 1):
    url = f"{base_url}?{page_param}={page}"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Get DF as return
        response_soup = scrap(soup)

        # print DF
        print('\n', page)
        print(response_soup)

        # Concatenate the extracted DataFrame to main_DF
        main_DF = pd.concat([main_DF, response_soup], ignore_index=True)
        
    else:
        print(f"Failed to retrieve page {page}")

# Display the concatenated DataFrame
print(main_DF)
main_DF.to_csv('ndan.csv')
