import json


class Car:

    # Constructor
    def __init__(self, name, color, kms):
        self.name = name
        self.color = color
        self.kms = kms

    def increase_km(self, amount):
        self.kms += amount

    def change_color(self, new_color):
        self.color = new_color

    def json_dump(self, destination_file):
        instance_dict = {
            'name': self.name,
            'color': self.color,
            'kms': self.kms
        }
        json.dump(instance_dict, open(destination_file, 'w'))


car_dict = json.load(open('car.json'))

car = Car(car_dict['name'], car_dict['color'], car_dict['kms'])
car.increase_km(3)
car.change_color('pink')
car.json_dump('car.json')
