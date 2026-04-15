# how to check if any instance belongs to any particular class or not ? 
# isinstance(instanceName, ClassName) -> it will return true or false

class Name:
    def __init__(self, name):
        self.name = name
    
    # __repr__ is more like a __str__ method, it  exist inside the memory by default ,if __str__ is missing then python automatically calls this method

    def __repr__(self):
        return f'<Name {self.name} >'

name = Name("ujjwal")
print(isinstance(name, Name)) # true


# raising a typeerror

class Car:
    def __init__(self, make, model):
        self.make = self.make
        self.model = self.model

    def __repr__(self):
        return f"<Car {self.make} {self.model}"

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            # car.__class__ → gives class of object
            # .__name__ → gives class name as string
            # Used to make error messages smart & helpful
            raise TypeError(f'Tried to add a {car.__class__.__name__} to the garage, but yu can only add "Car" objects.')
        self.cars.append(car)