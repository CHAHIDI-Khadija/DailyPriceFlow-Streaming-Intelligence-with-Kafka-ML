"""
logger.py - Logging Configuration Module

This module provides a function to configure logging for the application. It creates a logger instance with
customized settings, including a specified instance name and log file name. The logger can be used to record
various log messages at different levels, such as INFO, WARNING, ERROR, and CRITICAL.

Functions:
    - setup_logging(instance_name, log_filename):
        This function sets up and configures a logger instance with the given instance name and log file name.
        It defines a logging level of INFO, a timestamp-based log message format, and two handlers: a console
        handler and a file handler. Log messages are displayed on the console and saved to a specified log file.

Usage Example:
    from utils.logger import setup_logging
    logger = setup_logging("MyLogger", "my_log.log")
    logger.info("This is an information message.")

Note:
    Ensure that you specify the appropriate instance name and log file name when using the 'setup_logging' function.
    The log file will be saved in the specified directory.
"""


import logging

def setup_logging(instance_name, log_filename):
    """
    Setup logging for the application.

    This function creates and configures a logger instance with a specified instance name and log file name.
    It sets the logging level to INFO and defines a formatter for log messages with a timestamp, logger name,
    log level, and the message itself. Two handlers are added to the logger: a console handler and a file handler.

    Parameters:
        instance_name (str): A name for the logger instance.
        log_filename (str): The name of the log file where log messages will be saved.

    Returns:
        logger (logging.Logger): The configured logger instance.

    Example:
        logger = setup_logging("MyLogger", "my_log.log")
        logger.info("This is an information message.")
    """

    # Create a logger instance
    logger = logging.getLogger(instance_name)

    # Set the logging level
    logger.setLevel(logging.INFO)

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')

    # Create a console handler and set the formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Create a file handler and set the formatter
    file_handler = logging.FileHandler("path/to/3D/resources"+log_filename)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger