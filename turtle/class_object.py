

class Animal():

    def __init__(self, animal_name, animal_type):
        self.animal_name = animal_name
        self.animal_type = animal_type

    def describe_animal(self):
        print(self.animal_name.title() + " mostly live in rivers. ")
        print("It is " + self.animal_type.title() )

rest1 = Animal('Crocodile', 'Reptial')

rest1.describe_animal()
