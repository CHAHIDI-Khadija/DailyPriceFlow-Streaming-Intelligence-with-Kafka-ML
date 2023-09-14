"""
data.py - Data Retrieval Module

This module provides functions to retrieve financial data from an external API and process it for further analysis.

Functions:
    - retrieve_data(SYMBOL, API_KEY):
        Retrieves daily time series data for a specified financial symbol using the Alpha Vantage API.

Usage Example:
    from data.data import retrieve_data

    SYMBOL = 'AAPL'  # Replace with the desired financial symbol
    API_KEY = 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key

    data = retrieve_data(SYMBOL, API_KEY)

    if data is not None:
        # Data retrieval successful, continue with data processing.
        ...

Note:
    Ensure that you provide a valid financial symbol and Alpha Vantage API key when using the 'retrieve_data' function.
"""

import requests
import pandas as pd
from utils.logger import setup_logging

def retrieve_data(SYMBOL, API_KEY):
    """
    Retrieve daily time series data for a financial symbol from Alpha Vantage.

    This function sends an HTTP request to the Alpha Vantage API to retrieve daily time series data for the
    specified financial symbol. The retrieved data is in JSON format. If the retrieval is successful, the data
    is returned; otherwise, an error message is logged, and None is returned.

    Parameters:
        SYMBOL (str): The financial symbol for which data is to be retrieved (e.g., 'AAPL' for Apple Inc.).
        API_KEY (str): Your Alpha Vantage API key for authentication.

    Returns:
        data (dict or None): A dictionary containing daily time series data if retrieval is successful, or None
                            if an error occurs.

    Example:
        SYMBOL = 'AAPL'
        API_KEY = 'YOUR_API_KEY'
        data = retrieve_data(SYMBOL, API_KEY)

        if data is not None:
            # Data retrieval successful, continue with data processing.
            ...
    """

    logger = setup_logging("Data Retrieval", "3d_project_log.txt")

    try:
        # Retrieve data from an external API
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&outputsize=full&apikey={API_KEY}'
        response = requests.get(url)
        # Raise an error if there are issues with the HTTP request
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()

    # Handle exceptions, if any, and log an error message
    except Exception as e:
        logger.error(f"Error retrieving data: {e}")
        return None

    return data