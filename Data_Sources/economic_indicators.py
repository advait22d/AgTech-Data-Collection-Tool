# economic_indicators.py

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def fetch_economic_indicators(url):
    try:
        # Initialize Selenium WebDriver (make sure you have ChromeDriver installed)
        driver = webdriver.Chrome()
        driver.get(url)

        # Get page source after waiting for JavaScript to render
        page_source = driver.page_source

        # Close the webdriver
        driver.quit()

        # Parse HTML content
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the table element
        table = soup.find('table', class_='table-hover')

        # Initialize lists to store data
        data = []

        # Iterate through rows in the table body
        for row in table.find_all('tr'):
            # Extract data from each column (td) in the row
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            # Append data to list if it's not an empty row
            if cols:
                data.append(cols)

        # Convert data to DataFrame
        df = pd.DataFrame(data, columns=['Category', 'Last', 'Previous', 'Highest', 'Lowest', 'Unit', 'Date'])

        logger.info(f'Successfully fetched economic indicators data from {url}')
        return df  # Return DataFrame on success

    except Exception as e:
        logger.error(f"Error fetching economic indicators: {e}")
        return None  # Return None on error
