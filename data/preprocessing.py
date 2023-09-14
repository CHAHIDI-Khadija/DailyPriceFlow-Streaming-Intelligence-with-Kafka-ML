"""
preprocessing.py - Data Preprocessing Module

This module provides a function to clean and preprocess financial data retrieved from an external source for further analysis.

Functions:
    - clean_data(data):
        Cleans and preprocesses the retrieved financial data, converting it into a structured DataFrame suitable for analysis.

Usage Example:
    from data.preprocessing import clean_data

    # Assume you have already retrieved financial data using the 'retrieve_data' function.
    data = retrieve_data('AAPL', 'YOUR_API_KEY')

    if data is not None:
        cleaned_data = clean_data(data)
        if cleaned_data is not None:
            # Data preprocessing successful, continue with analysis.
            ...

Note:
    Ensure that you pass the retrieved financial data to the 'clean_data' function, and the data must be in the expected format.
"""

import pandas as pd
from utils.logger import setup_logging

def clean_data(data):
    """
    Clean and preprocess financial data for analysis.

    This function takes raw financial data in JSON format, cleans it, and converts it into a structured DataFrame.
    The data must have a 'Time Series (Daily)' key. If the data cleaning and preprocessing are successful,
    a cleaned DataFrame is returned; otherwise, an error message is logged, and None is returned.

    Parameters:
        data (dict): Raw financial data in JSON format.

    Returns:
        df (pd.DataFrame or None): A cleaned and processed DataFrame if successful, or None if an error occurs.

    Example:
        # Assume 'data' contains the retrieved financial data.
        cleaned_data = clean_data(data)

        if cleaned_data is not None:
            # Data preprocessing successful, continue with analysis.
            ...
    """

    logger = setup_logging("Data Preprocessing", "3d_project_log.txt")

    # Check if the data has the expected structure
    if 'Time Series (Daily)' in data:
        time_series = data['Time Series (Daily)']
        # Create a DataFrame from the time series data
        df = pd.DataFrame.from_dict(time_series).T
        # Convert the index to datetime
        df.index = pd.to_datetime(df.index)
        # Sort the DataFrame by date
        df.sort_index(ascending=True, inplace=True)
        # Rename columns by removing a prefix
        df.columns = [col.split('. ')[1] for col in df.columns]
        # Convert data types to float
        df = df.astype(float)

        logger.info("Processing data completed. Data is ready")
        return df

    else:
        # Log an error message for invalid data format
        logger.error("Invalid data format")
        return None