"""
sendMail.py - Email Sending Module

This module provides functions for sending emails with stock price prediction information to designated recipients.

Functions:
    - send_email(email_config, symbol, prediction):
        Send an email with stock price prediction information to a specified recipient.

Usage Example:
    from mail.sendMail import send_email

    # Assume 'email_config', 'symbol', and 'prediction' are properly configured.
    send_email(email_config, symbol, prediction)

Note:
    Ensure that you provide valid email configuration, symbol, and prediction values for accurate email sending.
"""

import os
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from utils.logger import setup_logging


def send_email(email_config, symbol, prediction):
    """
    Send an email with stock price prediction information.

    This function sends an email with stock price prediction information, including the predicted closing price for a
    specific date and symbol, to a designated recipient. It uses the provided email configuration and attaches an image
    with a plot of the prediction.

    Parameters:
        email_config (dict): Configuration for sending the email.
        symbol (str): The symbol or stock name for which the prediction is made.
        prediction (float): The predicted closing price.

    Example:
        send_email(email_config, 'AAPL', 150.25)
    """
    
    logger = setup_logging("Send email", "3d_project_log.txt")

    logger.info("Starting sendMail...")

    sender_email = email_config['sender_email']
    sender_password = email_config['sender_password']
    receiver_email = email_config['receiver_email']
    smtp_port = email_config['smtp_port']
    smtp_server = email_config['smtp_server']

    # Get the date for the prediction
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Create the email message
    subject = f"Stock Price Prediction for {date}"
    message_text = f"""Dear Receiver,

We hope this message finds you well. We wanted to share with you today's stock price prediction for {symbol}.

Date: {date}
Predicted Closing Price: {prediction:.3f}

Our prediction model, based on historical data and advanced forecasting techniques, suggests that the closing price for {symbol} on {date} is expected to be approximately {prediction:.3f}. Please note that this prediction is for informational purposes only and should not be considered financial advice.

If you have any questions or would like more information about this prediction, please feel free to reach out to us.

Thank you for your interest in our stock price prediction service.

Best regards,
3D - Team 2
"""
    # Create a MIMEText object to represent the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(message_text, 'plain'))

    # Attach the image if the path is valid
    path = "path/to/folder/3D/"
    image_path = path+"images/close_values_with_prediction.png"
    try:
        if os.path.exists(image_path):
            with open(image_path, 'rb') as image_file:
                image_data = MIMEImage(image_file.read(), name='close_values_with_prediction.png')
            message.attach(image_data)
            logger.info(f'Attached image: {image_path}')
        else:
            logger.warning(f'Image file not found at path: {image_path}')

    except Exception as e:
        logger.error(f'Error attaching image: {str(e)}')

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message.as_string())

        server.quit()

        logger.info('Email sent successfully!')
        logger.info(f'Email sent from {sender_email}, to {receiver_email}')

    except Exception as e:
        logger.error(f'Email could not be sent. Error: {str(e)}')

    finally:
        logger.info("Email script execution finished.")