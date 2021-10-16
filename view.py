from model import Person


class PersonView:

    def show_all(self, people):
        print(f'\nIn our db we have {len(people)} people. Here they are:')

        for item in people:
            print(item.full_name)

    def start_view(self):
        print('MVC - the simplest example')

    def ask_operation(self):
        return input('Do you want to see everyone in my db?[y/n]\n')

    def end_view(self):
        print('Goodbye!')
