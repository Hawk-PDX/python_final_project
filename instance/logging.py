import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def log_error(message):
    logging.error(message)

def log_info(message):
    logging.info(message)