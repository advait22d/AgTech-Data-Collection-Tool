import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def fetch_historical_data(api_url, api_key, params):
    try:
        headers = {
            'Authorization': f'Bearer {api_key}',  # Adjust if necessary
            'Content-Type': 'application/json'  # Adjust based on API requirements
        }
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # Checking if the request was successful
    except requests.exceptions.HTTPError as errh:
        logger.error(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.RequestException as err:
        logger.error(f"Request Exception: {err}")
        return None

    try:
        data = response.json()  # Parsing the JSON data
        records = data.get('data', [])  # Adjust based on the structure of the API response
        if not records:
            logger.warning("No data found in the API response.")
            return None
        df = pd.json_normalize(records)  # Normalize JSON to DataFrame
    except ValueError as e:
        logger.error(f"Error parsing JSON: {e}")
        return None
    except KeyError as e:
        logger.error(f"KeyError: {e} - Ensure 'data' field is present in the JSON response.")
        return None
    except Exception as e:
        logger.error(f"Error converting JSON to DataFrame: {e}")
        return None
    
    return df

if __name__ == '__main__':
    api_url = 'https://api.ers.usda.gov/data/arms/surveydata'  
    api_key = '0OYbmWUiUhblO1v27fGdTOUKU5aTKLoNnctc9xXi'  # Replace with your actual API key
    params = {
        'api_key': api_key,
        'year': '2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023',
        'variable': 'evfertc',
        'state': 'all'
    }
    
    historical_data_df = fetch_historical_data(api_url, api_key, params)
    if historical_data_df is not None:
        historical_data_df.to_csv('historical_sales_trends.csv', index=False)
        logger.info('Historical sales trends data saved successfully.')
    else:
        logger.error('Failed to fetch historical sales trends data.')
