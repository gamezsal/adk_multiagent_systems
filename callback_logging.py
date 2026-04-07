import logging

def log_query_to_model(agent, model, prompt):
    logging.info(f"[{agent.name}] Querying model...")

def log_model_response(agent, model, response):
    logging.info(f"[{agent.name}] Received model response.")
