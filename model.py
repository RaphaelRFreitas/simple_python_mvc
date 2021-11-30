import json
import os


class Person:
    db_file_path = os.path.join(os.path.dirname(__file__), 'db.txt')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        raw_data = None
        with open(cls.db_file_path) as f:    
            raw_data = json.loads(f.read())

        people = []
        for item in raw_data['people']:
            person = cls(item['first_name'], item['last_name'])
            people.append(person)

        return people
