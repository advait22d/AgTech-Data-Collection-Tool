import logging

def fetch_data_with_error_handling(fetch_function, *args, **kwargs):
    try:
        return fetch_function(*args, **kwargs)
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None


