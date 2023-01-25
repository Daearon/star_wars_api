from logg import logging
from user_interface import user_menu
from user_interface import start_of_calculation


logging.info("Starting calculator")
data = user_menu()
start_of_calculation(data)
