import logging

def log_query_to_model(*args, **kwargs):
    logging.info("Querying model...")

def log_model_response(*args, **kwargs):
    logging.info("Received model response.")
