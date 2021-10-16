from view import PersonView
from model import Person


class PersonController:

    def __init__(self):
        self.view =  PersonView()

    def show_all(self):
        people_in_db = Person.get_all()
        return self.view.show_all(people_in_db)

    def start(self):
        self.view.start_view()
        response = self.view.ask_operation()

        if response == 'y':
            return self.show_all()
        else:
            return self.view.end_view()
