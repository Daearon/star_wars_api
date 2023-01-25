import logging


logging.basicConfig(level=logging.INFO, filename="calculation_log.log",
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
                    datefmt='%d-%m-%Y %H:%M:%S')