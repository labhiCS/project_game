class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
        
    def read_odometer(self):
        print("This car has {} miles on it".format(str(self.odometer_reading)))
    
    
    def update_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            print("Odometer miles Succefully updated !!!")
            self.odometer_reading = mileage
        else:
            print("you cannot roll back an odometer!!")
    
    def increment(self, value):
        print("Additonal Miles added Successfully !!")
        self.odometer_reading += value
        
car_1 = Car('Audi', 'Q4', 2019)
car_1.odometer_reading = 100

# 3 modifying attribute's value using method
car_1.update_odometer(150)

car_1.increment(50)

car_1.read_odometer()