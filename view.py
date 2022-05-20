from model import Person


class PersonView:

    def start_view(self):
        print('MVC - the simplest example')

    def ask_read_operation(self):
        return input('Do you want to see everyone in my db?[y/n]\n')

    def end_view(self):
        print('Goodbye!')

    def show_all(self, people):
        print(f'\nIn our db we have {len(people)} people. Here they are:')

        for item in people:
            print(item.full_name)

    def ask_create_operation(self):
        return input('Do you want to add a new person to our db?[y/n]')

    def ask_person_data(self):
        first_name = input('First name: ')
        last_name = input('Last name: ')
        return first_name, last_name
