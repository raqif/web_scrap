import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage you want to scrape
# url = 'https://www.mudah.my'
url = 'https://www.bursamarketplace.com/mkt/themarket/stock'

# Send an HTTP GET request to 
# the URL
response = requests.get(url)
# response = requests.get(url, headers={'User-Agent':'test'})
print(response)

# Parse the HTML content of the response using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

with open('webpage.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

soup_div = soup.find_all("div", class_="tb_row tb_label")
# soup_div = soup.find_all("div", class_="tb_cell tb_data")

print(soup_div)

# soup_div2 = soup.find_all("div", class_="tb_row tb_data")
# print(soup_div2)
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Find the specific elements that contain the stock data
#     # You'll need to inspect the page's HTML to identify the correct elements
#     stock_data = soup.find_all("div", class_="your-target-class")

#     # Process and print the scraped data
#     for stock in stock_data:
#         # Extract and process the data as needed
#         print(stock.text)
# else:
#     print("Failed to retrieve the webpage")



# def scrap(soup):
#     # Find all div elements with the data-testid attribute
#     divs_with_testid = soup.find_all('div', {'data-testid': True})

#     LIST = []

#     # Print the found div elements
#     for div in divs_with_testid:
#         house = []
#         # print(div)
#         # # Find the <a> tag with title attributes
#         a_tag_title = div.find('a', {'title': True})

#         if a_tag_title:
#             # Print the title attribute
#             title = a_tag_title['title']
#             # print(title)
#             house.append(title)

#             # Find the next <div> element after the title <a> tag
#             next_div = a_tag_title.find_next('div')
#             if next_div:
#                 price = next_div.get_text()  # Get the text content of the div
#                 # print("Price:", price)
#                 # house.append(price)

#             next_div = next_div.find_next('div')
#             # next_div = next_div.find_next('div')
#             # print("\n", next_div)

#             # Find all <div> elements with text
#             all_divs_with_text = next_div.find_all('div', text=True)
#             # print("\n", all_divs_with_text)

#             # print(len(all_divs_with_text))
#             if len(all_divs_with_text) == 6:
#                 del all_divs_with_text[1]

#             # Print the text content of each div
#             for div in all_divs_with_text:
#                 text = div.get_text()
#                 # print(div.get_text())
#                 # print(text)
#                 house.append(text)
#                 # print('-' * 40)

#             # print(house)
#             LIST.append(house)

#     # print(LIST)
#     columns = ['Title', 'Price', 'Land Size', 'Built Up', 'Price', 'Price Per Sqft']

#     # Create a DataFrame
#     df = pd.DataFrame(LIST, columns=columns)

#     # Print the DataFrame
#     # print('\n', df)
#     return df
