from controller import Controller
from console_utils import ConsoleUtils


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    @staticmethod
    def print_note(note):
        print(note)

    @staticmethod
    def print_notes_list(notes_list):
        for note in notes_list:
            print(note)

    def check_id_exists(self, id) -> bool:
        notes_list = self.controller.read_notebook()
        id_list = [note.get_id() for note in notes_list]
        if id not in id_list:
            return False
        else:
            return True

    def show_all_records(self):
        notes = self.controller.read_notebook()
        self.print_notes_list(notes)

    def create_new_record(self):
        title = ConsoleUtils.retrieve_str('Enter title of your record: ')
        body = ConsoleUtils.retrieve_str('Enter body of your record: ')
        self.controller.create_note(title, body)
        print(f'New record was successfully created\n')

    def find_record_by_ID_and_edit_it(self):
        id = ConsoleUtils.retrieve_digit("Input ID: ")
        if self.check_id_exists(id):
            new_title = input('Enter new title of your record: ')
            new_body = input('Enter new body of your record: ')
            self.controller.update_note(id, new_title, new_body)
            print(f'Record with ID: {id} was successfully updated\n')
        else:
            print('No such ID, try again\n')

    def find_record_by_ID_and_delete_it(self):
        id = ConsoleUtils.retrieve_digit('Input ID: ')
        if self.check_id_exists(id):
            self.controller.delete_note(id)
            print(f'Record with ID: {id} was successfully deleted\n')
        else:
            print('No such ID, try again\n')

    def find_record_by_ID(self):
        id = ConsoleUtils.retrieve_digit('Input ID: ')
        if self.check_id_exists(id):
            note = self.controller.find_by_id(id)
            self.print_note(note)
        else:
            print('No such ID, try again\n')

    def find_records_by_date(self):
        date = input('Enter date (format: YYYY-MM-DD or YYYY-MM or YYYY)\n')
        result = self.controller.filter_by_date(date)
        if len(result) == 0:
            print('Nothing was found\n')
        else:
            self.print_notes_list(result)

    def stop_this_program(self):
        print("See you later")
        quit()

    def run(self):
        menu_list = {1: ("show all records", self.show_all_records),
                     2: ("create new record", self.create_new_record),
                     3: ("find record by ID and edit it", self.find_record_by_ID_and_edit_it),
                     4: ("find record by ID and delete it", self.find_record_by_ID_and_delete_it),
                     5: ("find record by ID", self.find_record_by_ID),
                     6: ("find records by date", self.find_records_by_date),
                     7: ("stop this program", self.stop_this_program)}

        list_of_commands = ""
        for menu_position in menu_list:
            list_of_commands += f"{menu_position} - {menu_list[menu_position][0]} \n"

        while True:
            command = ConsoleUtils.retrieve_digit(list_of_commands)
            if command not in menu_list:
                print('Wrong command. Try again.\n')
            else:
                menu_list[command][1]()
