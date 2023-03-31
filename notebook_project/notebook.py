import datetime

from note import Note


class Notebook:

    @staticmethod
    def read_notes():
        lines = []
        f = open('notes.csv', 'r')
        for line in f:
            note_parts = line.strip('\n').split(';')
            lines.append(Note(int(note_parts[0]), note_parts[1], note_parts[2], note_parts[3]))
        f.close()
        if not lines:
            print("Record is not found")
        return lines

    @staticmethod
    def write_notes(notes_list: [Note]):
        f = open('notes.csv', 'w')
        for note in notes_list:
            f.write(f'{str(note.get_id())};{note.get_title()};{note.get_body()};{note.get_date()}\n')
        f.close()

    def create_id(self) -> int:
        notes_list = self.read_notes()
        max_id = 0
        for note in notes_list:
            if note.get_id() > max_id: max_id = note.get_id()
        return max_id + 1

    def create_note(self, title, body):
        notes_list = self.read_notes()
        new_note = Note(self.create_id(), title, body, str(datetime.datetime.now()))
        notes_list.append(new_note)
        self.write_notes(notes_list)

    def update_note(self, id, new_title, new_body):
        notes_list = self.read_notes()
        for note in notes_list:
            if note.get_id() == id:
                note.set_new_title(new_title)
                note.set_new_body(new_body)
                note.set_new_date()
        self.write_notes(notes_list)

    def delete_note(self, id):
        notes_list = self.read_notes()
        for note in notes_list:
            if note.get_id() == id:
                notes_list.remove(note)
        self.write_notes(notes_list)

    def find_by_id(self, id) -> Note:
        notes_list = self.read_notes()
        for note in notes_list:
            if note.get_id() == id:
                return note

    def filter_by_date(self, date) -> [Note]:
        notes_list = self.read_notes()
        result = []
        for note in notes_list:
            if date in note.get_date():
                result.append(note)
        return result
