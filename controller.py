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
            response = self.view.ask_create_operation()
            if response == 'y':
                first_name, last_name = self.view.ask_person_data()
                person = Person(first_name, last_name)
                person.save()
            else:
                self.view.end_view()



    def start(self):
        self.view.start_view()
        self.show_all()
        