import yaml
from Data_Sources.industry_sales_trends import fetch_historical_data
from Data_Sources.economic_indicators import fetch_economic_indicators
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

def main():
    # Load configuration from config.yaml
    config = load_config('config.yaml')

    # Fetch industry sales trends data
    industry_sales_config = config['data_sources']['industry_sales_trends']
    api_url_industry = industry_sales_config['api_url']
    api_key_industry = industry_sales_config['api_key']
    params_industry = industry_sales_config['params']

    industry_data = fetch_historical_data(api_url_industry, api_key_industry, params_industry)
    if industry_data is not None:
        industry_data.to_csv('historical_sales_trends.csv', index=False)
        logger.info('Historical sales trends data saved successfully.')
    else:
        logger.error('Failed to fetch historical sales trends data.')

    # Fetch economic indicators data
    economic_config = config['data_sources']['economic_indicators']
    url_economic = economic_config['url']

    economic_data = fetch_economic_indicators(url_economic)
    if economic_data is not None:
        economic_data.to_csv('economic_indicators.csv', index=False)
        logger.info('Economic indicators data saved successfully.')
    else:
        logger.error('Failed to fetch economic indicators data.')

if __name__ == '__main__':
    main()
