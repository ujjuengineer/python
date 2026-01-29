# multiple inheritance : inherit from more than one parent class
#                        class Child(Parent1, Parent2):

# multilevel inheritance : inherit from a parent class which is also inheriting from another parent class
#                          A -> B(A) -> C(B)



# multiple inheritance example
class Flyer:
    def fly(self):
        print("Flying high in the sky!")

class Swimmer:
    def swim(self):
        print("Swimming in the water!") 

class Duck(Flyer, Swimmer):  # Duck class inherits from both Flyer and Swimmer classes
    def quack(self):
        print("Quack! Quack!")

duck1 = Duck()
duck1.fly()    # Output: Flying high in the sky!
duck1.swim()   # Output: Swimming in the water!
duck1.quack()  # Output: Quack! Quack!




# multilevel inheritance example
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):  # Car class inherits from Vehicle class
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):  # ElectricCar class inherits from Car class
    def charge(self):
        print("Electric car is charging")   

electric_car1 = ElectricCar()
electric_car1.start()  # Output: Vehicle started
electric_car1.drive()  # Output: Car is driving
electric_car1.charge() # Output: Electric car is charging

