# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# # Set up the Selenium browser options
# options = Options()
# options.headless = True  # Run in headless mode if you don't need a browser UI
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")

# # Set up the Selenium WebDriver
# service = Service(ChromeDriverManager().install())
# browser = webdriver.Chrome(service=service, options=options)

# # Go to the webpage
# browser.get('https://www.bursamarketplace.com/mkt/themarket/stock')

# print('getting wait 10 sec')
# # Wait for the desired content to load, you may need to adjust the waiting mechanism
# browser.implicitly_wait(10)  # Waits up to 10 seconds for elements to become available
# print('after wait 10 sec')

# # Now that the page is loaded, you can use BeautifulSoup to parse it
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
# data_cells = soup.find_all("div", class_="tb_cell tb_data")
# print(data_cells)

# # Process your data_cells as needed...

# # Don't forget to close the browser
# browser.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import pandas as pd

data_rows = []

# Set up the Selenium options
options = Options()
options.headless = True  # Run in headless mode if you don't need a browser UI
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Set up the Selenium WebDriver with correct service and options
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
# Go to the webpage
browser.get('https://www.bursamarketplace.com/mkt/themarket/stock')

print('getting wait 10 sec')
# Use WebDriverWait to wait for a specific element to be loaded
wait = WebDriverWait(browser, 4)
try:
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tb_cell.tb_data")))
except TimeoutException:
    # print("Timed out waiting for page to load")
    # Print the current state of the page source to debug
    # print(browser.page_source)
    print("Timed out waiting for the page to load, but trying to scrape anyway.")

print('after wait 10 sec')

# Now that the page is loaded, you can use BeautifulSoup to parse it
soup = BeautifulSoup(browser.page_source, 'html.parser')
data_cells = soup.find_all("div", class_="tb_row tb_data")
# print(data_cells)

for cell in data_cells:
    # print(cell.text.strip())
    data_points = cell.find_all("div", class_="tb_cell")
    print(data_points)
    
    # Extract the text from each data point
    row_data = [dp.get_text(strip=True) for dp in data_points]
    
    # Separate the 'Buy' and 'Sell' values and their respective quantities
    if len(row_data) >= 11:
        buy_value, buy_qty = row_data[9].rsplit(' ', 1)
        sell_value, sell_qty = row_data[10].rsplit(' ', 1)
        row_data[9] = buy_qty  # Replace 'Buy' with just the quantity
        row_data[10] = sell_qty  # Replace 'Sell' with just the quantity

    # Append the list of data points to our list of rows
    data_rows.append(row_data)

# Define the column names for our DataFrame
columns = ['CASHTAG', 'NAME', 'PRICE', 'CLOSE', 'CHG', '%CHG', 'VOLUME', 'HIGH', 'LOW', 'BUY (QTY)', 'SELL (QTY)']

# Create a DataFrame from our list of rows
df = pd.DataFrame(data_rows, columns=columns)

# Display the DataFrame
print(df)
browser.quit()

