class ConsoleUtils:

    @staticmethod
    def retrieve_digit(msg):
        while True:
            try:
                return int(input(msg))
            except ValueError:
                print("You input non digit value, try again")

    @staticmethod
    def retrieve_str(msg):
        while True:
            user_input = input(msg)
            if len(user_input) == 0:
                print("You input nothing, try again")
                continue
            else:
                return user_input
