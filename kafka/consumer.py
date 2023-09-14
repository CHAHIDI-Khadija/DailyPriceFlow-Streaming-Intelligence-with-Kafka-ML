"""
consumer.py - Kafka Consumer Module

This module provides a function to consume financial data from a Kafka topic, process it, and make predictions using a pre-trained ARIMA model.

Functions:
    - consumer(consumer_config, topic):
        Consumes financial data from a specified Kafka topic, processes it, and makes predictions using a pre-trained ARIMA model.

Usage Example:
    from kafka.consumer import consumer

    # Assume 'consumer_config' and 'topic' are properly configured.
    next_day_prediction = consumer(consumer_config, 'financial_data_topic')

Note:
    Ensure that you provide valid configurations and a Kafka topic with financial data for the consumer to function correctly.
"""

import pandas as pd
from confluent_kafka import Consumer
from model.arima import predict_next_day_close_price
from utils.logger import setup_logging

def consumer(consumer_config, topic):
    """
    Consume financial data from a Kafka topic, process it, and make predictions using a pre-trained ARIMA model.

    This function creates a Kafka consumer instance, subscribes to the specified Kafka topic, and continuously polls
    for messages. Upon receiving a message, it decodes the data, creates a DataFrame, and makes predictions using
    a pre-trained ARIMA model. It acknowledges the message after successful processing and gracefully closes the consumer
    when done.

    Parameters:
        consumer_config (dict): Configuration for the Kafka consumer.
        topic (str): The Kafka topic from which to consume financial data.

    Returns:
        prediction (float or None): The predicted close price for the next day, or None if an error occurs.

    Example:
        # Assume 'consumer_config' and 'topic' are properly configured.
        next_day_prediction = consumer(consumer_config, 'financial_data_topic')

    Note:
        Ensure that you provide valid configurations and a Kafka topic with financial data for accurate predictions.
    """

    # Set up logging
    logger = setup_logging("Consumer", "3d_project_log.txt")

    logger.info("Starting the consumer...")

    # Create a Kafka consumer instance
    consumer = Consumer(consumer_config)
    consumer.subscribe([topic])
    logger.info("Consumer instance created...")

    prediction = None

    try:
        while True:
            message = consumer.poll(1.0)  # Poll for messages with a timeout
            if message is None:
                continue
            if message.error():
                error_message = message.error()
                logger.error(f"Error: {error_message}")

                # Acknowledge the message to prevent it from being reprocessed
                consumer.commit(message)
                logger.info("Message acknowledged.")
                continue

            try:
                value = message.value().decode('utf-8')
                logger.info("Message received.")

                df = pd.read_json(value, orient='split')
                logger.info("DataFrame created.")

                # Make predictions using the pre-trained model
                prediction = predict_next_day_close_price(df)

                # Acknowledge the message after successful processing
                consumer.commit(message)
                logger.info("Message acknowledged.")

                # Exit the loop after processing a single message
                break

            except Exception as e:
                logger.error(f"Error: {e}")

    except KeyboardInterrupt:
        pass

    finally:
        # Close the consumer gracefully when done
        consumer.close()
        logger.info("Consumer script execution finished.")

    return prediction