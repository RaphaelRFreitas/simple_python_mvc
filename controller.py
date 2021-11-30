from view import PersonView
from model import Person


class PersonController:

    def __init__(self):
        self.view = PersonView()

    def show_all(self):
        response = self.view.ask_read_operation()

        if response == 'y':
            people = Person.get_all()
            return self.view.show_all(people)
        else:
            return self.view.end_view()

    def start(self):
        self.view.start_view()
        self.show_all()
        