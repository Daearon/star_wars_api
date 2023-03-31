from notebook import Notebook
from note import Note


class Controller:

    def __init__(self, notebook: Notebook):
        self.notebook = notebook

    def read_notebook(self) -> [Note]:
        notes = self.notebook.read_notes()
        return notes

    def create_note(self, title, body):
        self.notebook.create_note(title, body)

    def update_note(self, id, new_title, new_body):
        self.notebook.update_note(id, new_title, new_body)

    def delete_note(self, id):
        self.notebook.delete_note(id)

    def find_by_id(self, id) -> Note:
        return self.notebook.find_by_id(id)

    def filter_by_date(self, date) -> [Note]:
        return self.notebook.filter_by_date(date)
