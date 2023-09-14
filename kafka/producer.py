"""
producer.py - Kafka Producer Module

This module provides a function to produce financial data in JSON format to a Kafka topic for further processing.

Functions:
    - producer(producer_config, topic, data_config):
        Produces financial data to a specified Kafka topic after retrieving and preprocessing the data.

Usage Example:
    from kafka.producer import producer

    # Assume you have already configured 'producer_config' and 'data_config'.
    producer(producer_config, 'financial_data_topic', data_config)

Note:
    Ensure that you provide valid configurations and data for the producer to function correctly.
"""

from confluent_kafka import Producer
from utils.logger import setup_logging
from data.data import retrieve_data
from data.preprocessing import clean_data

def delivery_report(err, msg):
    """
    Callback function for message delivery report.

    This function is called to handle delivery reports for produced Kafka messages. It logs information about
    successful or failed message delivery.

    Parameters:
        err (confluent_kafka.KafkaError or None): An error message if message delivery failed, or None for success.
        msg (confluent_kafka.Message): The Kafka message object.

    Example:
        # This function is automatically used by the 'producer' function.
        producer.produce('topic', message.encode('utf-8'), callback=delivery_report)
    """
    logger = setup_logging("Producer", "3d_project_log.txt")
    if err is not None:
        logger.error(f'Message delivery failed: {err}')
    else:
        logger.info(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def producer(producer_config, topic, data_config):
    """
    Produce financial data to a Kafka topic.

    This function retrieves financial data, preprocesses it, and then produces it as JSON to a specified Kafka topic.
    It also handles delivery reports for produced messages.

    Parameters:
        producer_config (dict): Configuration for the Kafka producer.
        topic (str): The Kafka topic to which the data will be produced.
        data_config (dict): Configuration for data retrieval.

    Example:
        # Assume 'producer_config' and 'data_config' are properly configured.
        producer(producer_config, 'financial_data_topic', data_config)

    Note:
        Ensure that you provide valid configurations and data for the producer to function correctly.
    """
    # Set up logging
    logger = setup_logging("Producer", "3d_project_log.txt")

    logger.info("Starting the producer...")

    API_KEY = data_config['API_KEY']
    SYMBOL = data_config['SYMBOL']

    # Clean and prepare data
    data = retrieve_data(SYMBOL, API_KEY)
    df = clean_data(data)
    df_json = df.to_json(date_format='iso', orient='split')

    # Create a Kafka producer instance
    producer = Producer(producer_config)

    # Produce a message to the Kafka topic
    producer.produce(topic, df_json.encode('utf-8'), callback=delivery_report)

    logger.info("A message to the Kafka topic produced.")

    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()

    # Log script completion
    logger.info("Producer script execution finished.")
