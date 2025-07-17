# chapter_6.py

# chapter_6.py

class Car:
    runs = True
    number_of_wheels = 4
    
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car("Ford","Thunderbird")
my_car.start()
# print(f"Cars have {Car.get_number_of_wheels()} wheels.")

# # Of course, we can override this in our instance:
# my_car.number_of_wheels = 6

# # And when we access our new instance variable:
# print(f"My car has {my_car.number_of_wheels} wheels.")

# # But, when we call our class method on our instance:
# print(f"My car has {my_car.get_number_of_wheels()} wheels.")
