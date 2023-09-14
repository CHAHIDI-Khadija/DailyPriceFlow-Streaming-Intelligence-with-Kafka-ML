"""
main.py - Main Program Module

This module serves as the main program for the 3D project. It loads configurations, interacts with Kafka for data processing,
performs ARIMA predictions, and sends email notifications with prediction results.

Functions:
    - main():
        The main function that orchestrates the entire project workflow.

Usage Example:
    if __name__ == "__main__":
        main()

Note:
    Ensure that you have valid configuration files and Kafka topics set up for accurate data processing and notifications.
"""

import json
from kafka.producer import producer
from kafka.consumer import consumer
from mail.sendMail import send_email
from utils.logger import setup_logging

def main():
    """
    Main program for the 3D project.

    This function orchestrates the entire project workflow, including loading configurations, interacting with Kafka for
    data processing, performing ARIMA predictions, and sending email notifications with prediction results.

    Example:
        if __name__ == "__main__":
            main()

    Note:
        Ensure that you have valid configuration files and Kafka topics set up for accurate data processing and notifications.
    """
    
    # Initialize the logger
    logger = setup_logging("Main", "3d_project_log.txt")

    logger.info("Starting the main program...")
    # Load configuration from JSON files
    
    path = "path/to/project/folder/3D"
    try:
        logger.info("Loading configurations.")

        with open(path+'/config/data_config.json', 'r') as data_config_file:
            data_config = json.load(data_config_file)

        with open(path+'/config/kafka_config.json', 'r') as kafka_config_file:
            kafka_config = json.load(kafka_config_file)

        with open(path+'/config/email_config.json', 'r') as email_config_file:
            email_config = json.load(email_config_file)

        logger.info("Configurations Loaded")

    except FileNotFoundError as e:
        logger.error(f"Config file not found: {e}")

    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON: {e}")

    producer(kafka_config["producer_config"], kafka_config["topic"], data_config)

    # Perform ARIMA prediction
    next_day_prediction = consumer(kafka_config["consumer_config"], kafka_config["topic"])

    # Send an email notification
    send_email(email_config, data_config['SYMBOL'], next_day_prediction)

    logger.info("Main script execution finished.")
    logger.info("Have a great day!")

if __name__ == "__main__":
    main()