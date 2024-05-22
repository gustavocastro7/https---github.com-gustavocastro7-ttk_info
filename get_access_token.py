import logging

class pLogger_cl(object):
    """
    Logger class for pLogger_cl
    """

    def __init__(self, log_file_path):
        """
        Constructor for pLogger_cl.

        :param log_file_path: Path to log file
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def log(self, msg, level=logging.DEBUG):
        """
        Log a message

        :param msg: Message to log
        :param level: Logging level
        """
        self.logger.log(level, msg)

    def debug(self, msg):
        """
        Log a debug message

        :param msg: Message to log
        """
        self.log(msg, logging.DEBUG)

    def info(self, msg):
        """
        Log an info message

        :param msg: Message to log
        """
        self.log(msg, logging.INFO)

    def warning(self, msg):
        """
        Log a warning message

        :param msg: Message to log
        """
        self.log(msg, logging.WARNING)

    def error(self, msg):
        """
        Log an error message

        :param msg: Message to log
        """
        self.log(msg, logging.ERROR)

    def critical(self, msg):
        """
        Log a critical message

        :param msg: Message to log
        """
        self.log(msg, logging.CRITICAL)

if __name__ == '__main__':
    logger = pLogger_cl("log/log.txt")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

def request_access_token():
    # Load authentication details from JSON file
    secret, app_id, auth_code = load_auth_from_json("config/auth.json")

    # Args in JSON format
    my_args = {
        "secret": secret,
        "app_id": app_id,
        "auth_code": auth_code
    }

    # Send POST request
    response = post(json.dumps(my_args))

    # Log the request result
    logger = pLogger_cl("log/log.txt")
    if response.status_code == 200 and response.json().get('code') == 0:
        logger.info("Request access token successful")
    else:
        logger.error(f"Request access token failed. Status code: {response.status_code}, Text: {response.text}")

    print_json(response.json())

if __name__ == '__main__':
    request_access_token()


