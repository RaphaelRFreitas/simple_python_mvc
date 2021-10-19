from view import PersonView
from model import Person


class PersonController:

    def __init__(self):
        self.view =  PersonView()

    def show_all(self):
        response = self.view.ask_read_operation()

        if response == 'y':
            people_in_db = Person.get_all()
            self.view.show_all(people_in_db)
        else:
            return self.view.end_view()


    def write_person(self):
        response = self.view.write_person()

        if response == 'y':
            first_name, last_name = self.view.ask_person_data()
            person = Person(first_name, last_name)
            person.save()
        else:
            return self.view.end_view()

    def start(self):
        self.view.start_view()
        self.show_all()
        self.write_person()
        