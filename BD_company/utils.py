def create_menu(user_menu):
    user_menu_length = len(user_menu)
    print("-----------------------------------------------")
    for i in range(user_menu_length):
        print(f"{i+1}. {user_menu[i]}")
    print("-----------------------------------------------")
    user_decision = retrieve_integer("Enter the option you need from the menu: ")
    return [user_decision, user_menu[len(user_menu)-1]]


def retrieve_integer(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Вы вводите не цифровое значение, попробуйте еще раз")