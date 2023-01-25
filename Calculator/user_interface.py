from exception import *
from logg import logging
import sys
from mod_calc import *


def user_menu():
    print("Welcome, user")
    user_choice = retrieve_integer("What type of numbers will we work with? Type '1' for complex number,"
                                 "type '2' for rational number, type '3' for exit: ")
    if user_choice == 1:
        first_part_of_first_complex = retrieve_integer("Enter your first number: ")
        second_part_of_first_complex = retrieve_integer("Enter your second number: ")
        argument_1 = complex(first_part_of_first_complex, second_part_of_first_complex)
        first_part_of_second_complex = retrieve_integer("Enter your third number: ")
        second_part_of_second_complex = retrieve_integer("Enter your fourth number: ")
        argument_2 = complex(first_part_of_second_complex, second_part_of_second_complex)
        print("What type of operation you choose?")
        user_choice_operation = retrieve_integer("What type of operation you choose? Type '1' for summation, "
                                                 "'2' for subtraction, '3' for multiplication, '4' for division, "
                                                 "'5' for exponentiation, '6' for calculation square root: ")
    elif user_choice == 2:
        first_part_of_first_rational = retrieve_integer("Enter your first number: ")
        second_part_of_first_rational = retrieve_integer("Enter your second number: ")
        argument_1 = float(first_part_of_first_rational / second_part_of_first_rational)
        first_part_of_second_rational = retrieve_integer("Enter your third number: ")
        second_part_of_second_rational = retrieve_integer("Enter your fourth number: ")
        argument_2 = float(first_part_of_second_rational / second_part_of_second_rational)
        print("What type of operation you choose?")
        user_choice_operation = retrieve_integer("What type of operation you choose? Type '1' for summation, "
                                                 "'2' for subtraction, '3' for multiplication, '4' for division, "
                                                 "'5' for exponentiation, '6' for calculation square root: ")
    elif user_choice == 3:
        logging.info("Calculator terminated by user")
        print("Good, see you later")
        return sys.exit
    else:
        logging.info("Calculator terminated because user entered incorrect data")
        print("You entered incorrect data, calculator will be terminated")
        return
    return argument_1, argument_2, user_choice_operation


def start_of_calculation(data):
    calculation_result = create_option_for_calculation(data)
    print(f"Your result is {calculation_result}")
    logging.info(calculation_result)