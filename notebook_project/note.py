import datetime


class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_new_date(self):
        self.date = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def set_new_title(self, new_title):
        self.title = new_title

    def set_new_body(self, new_body):
        self.body = new_body
