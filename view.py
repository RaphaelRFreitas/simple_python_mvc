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
    
    def write_person(self):
        return input('Do you want to save a new person in my db?[y/n]\n')

    def ask_person_data(self):
        first_name = input("Input the first name:\n")
        last_name = input('Input the last name:\n')
        return first_name, last_name