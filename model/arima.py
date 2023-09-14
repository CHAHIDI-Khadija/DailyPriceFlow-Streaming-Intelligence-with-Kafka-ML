"""
arima.py - ARIMA Time Series Model Module

This module provides functions for predicting the next day's close price of a financial asset using an ARIMA model.

Functions:
    - predict_next_day_close_price(df):
        Predicts the next day's close price of a financial asset based on historical data.

Usage Example:
    from model.arima import predict_next_day_close_price

    # Assume 'df' is a DataFrame containing historical financial data.
    next_day_prediction = predict_next_day_close_price(df)

Note:
    Ensure that you provide a DataFrame with the 'close' price as a column for the 'predict_next_day_close_price' function.
"""

from datetime import timedelta
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from utils.logger import setup_logging

def predict_next_day_close_price(df):
    """
    Predict the next day's close price of a financial asset using an ARIMA model.

    This function takes a DataFrame containing historical financial data, including a 'close' price column,
    and uses an ARIMA (AutoRegressive Integrated Moving Average) model to predict the next day's close price.
    It also calculates and logs performance metrics for the model's predictions.

    Parameters:
        df (pd.DataFrame): A DataFrame containing historical financial data, including a 'close' price column.

    Returns:
        next_day_prediction (float): The predicted close price for the next day.

    Example:
        # Assume 'df' contains the historical financial data.
        next_day_prediction = predict_next_day_close_price(df)

    Note:
        Ensure that you provide a DataFrame with the 'close' price as a column for accurate predictions.
    """

    logger = setup_logging("Model", "3d_project_log.txt")

    logger.info("Starting predicting...")

    # Check if index is not datetime
    if not isinstance(df.index, pd.DatetimeIndex):
        try:
            df.index = pd.to_datetime(df.index)
        except Exception as e:
            logger.error(f"Error converting index to datetime: {str(e)}")
            return None  # Return None to indicate an error
    
    # Check if columns are not float
    if not all(df.dtypes == float):
        try:
            df = df.astype(float)
        except Exception as e:
            logger.error(f"Error converting columns to float: {str(e)}")
            return None  # Return None to indicate an error

    train_size = int(len(df) * 0.9)
    train_data, test_data = df[:train_size], df[train_size:]

    # Perform automatic ARIMA model selection
    model_autoARIMA = auto_arima(train_data['close'], start_p=0, start_q=0, test='adf', max_p=3, max_q=3,
                                m=1, d=None, seasonal=False, start_P=0, D=0, stepwise=True, trace=False,
                                error_action='ignore', suppress_warnings=True)

    # Get the selected ARIMA order
    order = model_autoARIMA.order

    # Initialize variables for predictions
    train_data = train_data['close'].values
    test_data = test_data['close'].values
    history = [x for x in train_data]
    model_predictions = []
    N_test_observations = len(test_data)

    # Generate predictions
    # Initialize the ARIMA model outside the loop
    model = ARIMA(history, order=order)
    model_fit = model.fit()
    logger.info("Model fitted.")

    # Iterate over test data points and make predictions
    for time_point in range(N_test_observations):
        # Get the true test value
        true_test_value = test_data[time_point]
        # Update the history with the true test value
        history.append(true_test_value) 
        # Re-fit the ARIMA model with the updated history
        model = ARIMA(history, order=order)
        model_fit = model.fit()
        # Forecast the next value
        yhat = model_fit.forecast(steps=1)[0]
        # Append the prediction to the list
        model_predictions.append(yhat)

    # Report performance metrics
    mse = mean_squared_error(test_data, model_predictions)
    mae = mean_absolute_error(test_data, model_predictions)
    rmse = math.sqrt(mse)
    mape = np.mean(np.abs(model_predictions - test_data) / np.abs(test_data))

    logger.info("Report performance metrics")
    logger.info('MSE: {:.3f}'.format(mse))
    logger.info('MAE: {:.3f}'.format(mae))
    logger.info('RMSE: {:.3f}'.format(rmse))
    logger.info('MAPE: {:.3f}%'.format(mape * 100))

    # Make a one-step-ahead prediction
    next_day_prediction = model_fit.forecast(steps=1)[0]

    # Make a plot of last 14 days with the predicted day
    last_14_days = df['close'][-14:]
    next_day = last_14_days.index[-1] + timedelta(days=1)  # Calculate the next day
    predicted_day = pd.Series([next_day_prediction], index=[next_day])  # Create a Series

    combined_data = pd.concat([last_14_days, predicted_day])

    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.xlabel('Dates')
    plt.ylabel('Close Value')

    plt.plot(combined_data.index, combined_data.values, '-k', linewidth=2)
    plt.plot(last_14_days.index, last_14_days.values, 'ko', label='Last 14 days', markersize=6, markeredgewidth=2)
    plt.plot(predicted_day.index, predicted_day.values, 'ro', label='Predicted Close Value', markersize=8)

    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() 

    plt.savefig('path/to/3D/images/close_values_with_prediction.png')

    logger.info("Prediction completed.")
    
    return next_day_prediction