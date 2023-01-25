from logg import logging


def create_option_for_calculation(data):
    argument_1, argument_2, user_choice_operation = data
    if user_choice_operation == 1:
        return summation(argument_1, argument_2)
    if user_choice_operation == 2:
        return subtraction(argument_1, argument_2)
    if user_choice_operation == 3:
        return multiplication(argument_1, argument_2)
    if user_choice_operation == 5:
        return exponentiation(argument_1, argument_2)
    if user_choice_operation == 6:
        return calculation_square_root(argument_1)
    if (user_choice_operation == 4) and (argument_2 != 0):
        return division(argument_1, argument_2)
    else:
        logging.warning("User entered incorrect data")
        return print('You cannot division on zero and entered number < 1 and > 6')


def summation(argument_1, argument_2):
    return argument_1 + argument_2


def subtraction(argument_1, argument_2):
    return argument_1 - argument_2


def multiplication(argument_1, argument_2):
    return argument_1 * argument_2


def division(argument_1, argument_2):
    return argument_1 / argument_2


def exponentiation(argument_1, argument_2):
    return argument_1 ** argument_2


def calculation_square_root(argument_1):
    return argument_1 ** 0.5


