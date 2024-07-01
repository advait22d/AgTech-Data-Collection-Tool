# AgTech-Data-Collection-Tool

## Project Overview
This project is a Python-based data collection tool designed to fetch and process agricultural data from various sources, focusing on industry sales trends and economic indicators. The tool uses the USDA's Economic Research Service API for industry sales data and web scraping techniques for economic indicators data from the trading economics site.

## Project Structure
AGTECH-DATA-COLLECTION-TOOL/
│
├── main.py
├── config.yaml
├── Data_Sources/
│   ├── industry_sales_trends.py
│   └── economic_indicators.py
└── fetch_utils.py


## Features
- Automated data extraction from reliable sources
- Modular and flexible code structure
- Error handling and logging for robustness
- Configuration files for easy customization of data sources and parameters
- Data storage in structured formats (CSV)

## Requirements
- Python 3.7+
- pip (Python package installer)
- ChromeDriver (for Selenium) 

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

git clone https://github.com/advait22d/AgTech-Data-Collection-Tool.git

### 2. Create a virtual environment
conda create -n agtech python=3.8 -y
activate agtech

### 3. Install all the requirements
pip install -r requirements.txt

Ensure your 'requirements.txt' has :
pyyaml
requests
pandas
selenium
beautifulsoup4

### 4. Set Up ChromeDriver
Download ChromeDriver from the official site and ensure it's in your PATH. On Linux/Mac, you can place it in /usr/local/bin. On Windows, you can place it in the project directory and add the path to the system's environment variables.

### 5: Configure the Project
Update the config.yaml file with your API keys and any other necessary configuration.

data_sources:
  industry_sales_trends:
    api_url: 'url'
    api_key: 'YOUR_API_KEY'
    params:
      year: ''
      variable: ''
      state: ''
  economic_indicators:
    url: ''
Replace YOUR_API_KEY with your actual API key for the USDA ERS API.

### 6. Running the project

Run the main script to fetch and save the data.

python main.py


Check the project directory for the output CSV files:

historical_sales_trends.csv
economic_indicators.csv
These files should contain the fetched data.


