import csv
import datetime
from note import Note


class Notebook:
    file_name = 'notes.csv'
    header = ['id', 'title', 'body', 'date']

    def read_notes(self) -> [Note]:
        lines = []

        with open(self.file_name, encoding='UTF8') as f:
            csv_reader = csv.reader(f)
            for line_no, line in enumerate(csv_reader, 1):
                if line_no == 1:  # пропускаем первую строку с заголовками
                    continue
                lines.append(Note(int(line[0]), line[1], line[2], line[3]))
        if not lines:
            print("Record is not found")
        return lines

    def write_notes(self, notes_list: [Note]):
        with open(self.file_name, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            for note in notes_list:
                writer.writerow([note.get_id(), note.get_title(), note.get_body(), note.get_date()])

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
