import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap(soup):
    # # URL of the webpage you want to scrape
    # # url = 'https://www.mudah.my'
    # url = 'https://www.mudah.my/neighbouring-kuala-lumpur/properties-for-sale'

    # # Send an HTTP GET request to the URL
    # response = requests.get(url)
    # print(response)

    # # Parse the HTML content of the response using Beautiful Soup
    # soup = BeautifulSoup(response.content, 'html.parser')
    # # print(soup)

    # Find all div elements with the data-testid attribute
    divs_with_testid = soup.find_all('div', {'data-testid': True})

    LIST = []

    # Print the found div elements
    for div in divs_with_testid:
        house = []
        # print(div)
        # # Find the <a> tag with title attributes
        a_tag_title = div.find('a', {'title': True})

        if a_tag_title:
            # Print the title attribute
            title = a_tag_title['title']
            # print(title)
            house.append(title)

            # Find the next <div> element after the title <a> tag
            next_div = a_tag_title.find_next('div')
            if next_div:
                price = next_div.get_text()  # Get the text content of the div
                # print("Price:", price)
                # house.append(price)

            next_div = next_div.find_next('div')
            # next_div = next_div.find_next('div')
            # print("\n", next_div)

            # Find all <div> elements with text
            all_divs_with_text = next_div.find_all('div', text=True)
            # print("\n", all_divs_with_text)

            # print(len(all_divs_with_text))
            if len(all_divs_with_text) == 6:
                del all_divs_with_text[1]

            # Print the text content of each div
            for div in all_divs_with_text:
                text = div.get_text()
                # print(div.get_text())
                # print(text)
                house.append(text)
                # print('-' * 40)

            # print(house)
            LIST.append(house)

    # print(LIST)
    columns = ['Title', 'Price', 'Land Size', 'Built Up', 'Price', 'Price Per Sqft']

    # Create a DataFrame
    df = pd.DataFrame(LIST, columns=columns)

    # Print the DataFrame
    # print('\n', df)
    return df







        # next_divs = next_div.find_all('div')
        # print(next_divs)
        # # if next_div:
        #     next_text = next_div.get_text()  # Get the text content of the div
        #     print("next:", next_text)
            
        #     # Extract different parts using slicing
        #     title = next_text.split('RM ')[0].strip()
        #     after_title = next_text.split('RM ')[1].strip()
        #     price = next_text.split('RM ')[1].split('House')[0].strip()
        #     # type = next_text.split('RM ')[1].split('House')[1].strip()
        #     # size = next_text.split('House')[1].split('Bedrooms')[0].strip()
        #     # bedrooms = next_text.split('Bedrooms')[1].split('Bathrooms')[0].strip()
        #     # bathrooms = next_text.split('Bathrooms')[1].strip()
            
        #     print("Title:", title)
        #     print("after_Title:", after_title)
        #     print("Price:", price)
        #     # # print("Type:", type)
        #     # print("Size:", size)
        #     # print("Bedrooms:", bedrooms)
        #     # print("Bathrooms:", bathrooms)
        #     print()

    # # Check if the <a> tag is found
    # if a_tag:
    #     # Extract the title attribute value
    #     title = a_tag['title']
        
    #     # Print the title
    #     print(title)

# # Find all the div elements with the data-testid attribute
# ads = soup.find_all('div', {'data-testid': 'listing-ad-item'})

# # Extract and print information from each ad
# for ad in ads:
#     # You can extract specific information from the ad element here
#     # For example, if the title is stored in a child element, you can use:
#     # title = ad.find('h2').text
#     # Print the extracted information
#     # print(title)
    
#     # Print the whole ad element
#     print(ad)

# # Find all the article titles on the webpage
# article_titles = soup.find_all('h2', class_='article-title')

# # Print the titles
# for title in article_titles:
#     print(title.text)
