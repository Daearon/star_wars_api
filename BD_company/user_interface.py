from utils import *
from db_operations import *
import sys


def running_program():
    user_menu_list = ["Add record -->", "View record -->", "Dismiss civil_servant -->",
                      "Making an power of attorney -->", "Exit -->"]
    choice_for_user = create_menu(user_menu_list)
    match choice_for_user[0]:
        case 1:
            add_in_bd()
        case 2:
            read_bd()
        case 3:
            except_from_bd()
        case 4:
            make_update_bd()
        case 5:
            print("All right, thank you for use our date base. Bye")
            sys.exit()
        case _:
            print("You entered incorrect number. Try again, please")
