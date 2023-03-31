from controller import Controller
from list_of_commands import *


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    @staticmethod
    def make_validate_input(input_string):
        if not input_string.isdigit():
            return input("Only digit is allowed. Try again:\n")
        else:
            return input_string

    def make_validate_id(self, id) -> bool:
        notes_list = self.controller.read_notebook()
        id_list = [note.get_id() for note in notes_list]
        if id not in id_list:
            return False
        else:
            return True

    @staticmethod
    def print_note(note):
        print(f'ID: {note.get_id()} Title: {note.get_title()} Body: {note.get_body()} Date: {note.get_date()}')

    @staticmethod
    def print_notes_list(notes_list):
        for note in notes_list:
            print(
                f'ID: {note.get_id()} Title: {note.get_title()} Body: {note.get_body()} Date: {note.get_date()}')

    def run(self):
        while True:
            command = input(list_of_commands)
            match command:
                case '1':
                    notes = self.controller.read_notebook()
                    self.print_notes_list(notes)
                    continue
                case '2':
                    title = input('Enter title of your record: ')
                    body = input('Enter body of your record: ')
                    self.controller.create_note(title, body)
                    print(f'New record was successfully created\n')
                    continue
                case '3':
                    id = int(self.make_validate_input(input('Enter ID: ')))
                    if self.make_validate_id(id):
                        new_title = input('Enter new title of your record: ')
                        new_body = input('Enter new body of your record: ')
                        self.controller.update_note(id, new_title, new_body)
                        print(f'Record with ID: {id} was successfully updated\n')
                        continue
                    else:
                        print('No such ID, try again\n')
                        continue
                case '4':
                    id = int(self.make_validate_input(input('Enter ID: ')))
                    if self.make_validate_id(id):
                        self.controller.delete_note(id)
                        print(f'Record with ID: {id} was successfully deleted\n')
                        continue
                    else:
                        print('No such ID, try again\n')
                        continue
                case '5':
                    id = int(self.make_validate_input(input('Enter ID: ')))
                    if self.make_validate_id(id):
                        note = self.controller.find_by_id(id)
                        self.print_note(note)
                        continue
                    else:
                        print('No such ID, try again\n')
                        continue
                case '6':
                    date = input('Enter date (format: YYYY-MM-DD or YYYY-MM or YYYY)\n')
                    result = self.controller.filter_by_date(date)
                    if len(result) == 0:
                        print('Nothing was found\n')
                        continue
                    else:
                        self.print_notes_list(result)
                        continue
                case '7':
                    break
                case _:
                    print('Wrong command. Try again.\n')
