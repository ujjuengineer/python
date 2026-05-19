# mutable and immutable data types in python

# mutable :  that can be changed after creation 
li = [1,2,3,4]
li.append(5)
print(li)

# immutable : can't be changed once created
s = "hello"
# s[0] = "H"
# TypeError: 'str' object does not support item assignment

# In Python:
# Strings are stored as immutable objects
# Any modification → new object in memory


#=============================================================================================


# indexing and slicing

# indexing : accessing single element using index  O(1)
# slicing : accessing range of elements O(n), create new copy

nums = [10, 20, 30, 40, 50]

# Indexing
print(nums[1])   # 20
print(nums[-2])  # 40

# Slicing
print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[::-1])  # [50, 40, 30, 20, 10]

# Modification
nums[0] = 100
print(nums)  # [100, 20, 30, 40, 50]

# can be applied on tuple, string as well

# =============================================================================================



# del(), pop(), clear(), remove() in list

# del() -> can delete list from the memeory, can delete ele using indxing or slicing
# remove -> delete ele from the list using values, if value not found then show error
# pop() -> delete and return the ele of list by index
# clear() -> dlt all the ele of the list but keep the empty list in the memory


#==================================================================================================
print()
print("-------------------------------constructor-----------------------")
print()


# __init__ and __del__ : 
"""
-> they are constructor and destructor 

-> __init__ automatically called when object is created in the memeory 
    -> 2 types of constructor, default constructor, parameterized constructor
-> it initializes the object data and runs automatically when object is created


__del__() : destructor
-> called when object is destroyed from the memory


NOTE : python destructor are not reliable like c++ destructor, because python use garbage collection
this means, __del__ will called when object is garbage collected, not always immediately after del


"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, "constructor is called")
    
    def __del__(self):
        print(self.name, "destructor is called")


s1 = Student("ujjwal", 22)
s2 = Student("Ram", 21)



# ===============================================================================
print()
print("-------------------------- inheritance --------------")
print()


# inheritance ? 
# types of inheritance ? 
# constructor resolution during various inheritance 

"""

n Python, Inheritance is a fundamental pillar of Object-Oriented Programming (OOP). It allows a new class (known as a Child or Derived class) to inherit the attributes and methods of an existing class (the Parent or Base class).

This promotes code reusability and establishes a hierarchical relationship between classes.

1. Basic Syntax

To inherit from a class, you pass the name of the parent class as a parameter when defining the child class.
"""
class Parent:
    # Parent attributes and methods
    pass

class Child(Parent):
    # Child inherits everything from Parent
    pass

"""
2. Types of Inheritance

Python supports several forms of inheritance, making it highly flexible:

Single Inheritance: A child class inherits from a single parent class.

Multiple Inheritance: A child class inherits from more than one parent class.

Multilevel Inheritance: A child class inherits from a parent, which in turn inherits from another class (a grandparent).

Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

Hybrid Inheritance: A combination of two or more of the types mentioned above.


3. Key Components

A. The super() Function

The super() function is used to call methods from the parent class within the child class. This is most commonly used in the __init__ method to ensure the parent class is properly initialized.

B. Method Overriding

A child class can provide a specific implementation of a method that is already provided by its parent class. This allows the child to change or extend the behavior of that method.


4. Practical Example

Here is a comprehensive example showing a parent class Vehicle and a child class Car.
"""

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        # Using super() to inherit attributes from Vehicle
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    # Method Overriding
    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")

# Creating an instance
my_car = Car("Tesla", 2024, "Electric")
my_car.display_info()

"""
5. Advantages of Inheritance

Feature	Description
Reusability	You don't have to rewrite the same code for related classes.
Transitivity	If Class B inherits from A, then all subclasses of B will also inherit from A.
Maintenance	Changes made in the parent class automatically propagate to child classes, making code easier to manage.
Extensibility	You can add new features to a child class without modifying the parent class.


6. Method Resolution Order (MRO) (read from notes how its work)

In complex scenarios (like Multiple Inheritance), Python uses an algorithm called C3 Linearization to determine the order in which base classes are searched for a method. You can view this order using the ClassName.mro() method or the __mro__ attribute.

"""

# exception in python

"""
1. Types of Exceptions

Exceptions are events that disrupt the normal flow of a program's instructions. They are generally categorized into two groups:

Built-in Exceptions: These are predefined by Python. Common examples include:

ZeroDivisionError: Raised when the second operand of division or modulo is zero.

ValueError: Raised when a function receives an argument of the right type but inappropriate value (e.g., trying to convert "abc" to an integer).

TypeError: Raised when an operation is applied to an object of inappropriate type.

IndexError: Raised when a sequence subscript is out of range.

FileNotFoundError: Raised when a file or directory is requested but doesn't exist.

User-defined Exceptions: Programmers can create their own exceptions by creating a new class that inherits from the built-in Exception class.

2. Importance of the Handling Blocks

Python uses a try-except-else-finally structure to manage errors.

Block	Significance
try	Contains the code that might throw an exception. Python monitors this block for errors.
except	Executes only if an error occurs in the try block. It allows you to "catch" the error and handle it (e.g., logging or showing a message).
else	Executes only if no exceptions were raised in the try block. It’s useful for code that should only run if the try block was successful.
finally	Executes regardless of whether an exception occurred or not. It is primarily used for "clean-up" actions, like closing files or database connections.
3. Significance of the raise Keyword

The raise keyword is used to forcefully trigger an exception. This is useful when:

Validation: You want to stop execution if a specific condition isn't met (e.g., raise ValueError("Age cannot be negative")).

Rethrowing: You want to catch an error, perform a specific action (like logging), and then let the error continue to propagate up the stack.

4. Program: Division with Exception Handling

This program handles both ZeroDivisionError (dividing by 0) and ValueError (entering text instead of numbers).
"""

def divide_numbers():
    try:
        # Taking user input
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        
        # Performing division
        result = num1 / num2
        
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        # Runs only if no error occurred
        print(f"Success! The result is: {result}")
    finally:
        # Runs no matter what
        print("Division operation attempt complete.")

# Run the function
divide_numbers()


# extra info for exception 

# IndexError : when you access index out of range 
# KeyError : when you access a key which doesn't exist
# NameError : when you try to access or print unknown/undefined variable
# AttributeError : when you try to access an attribute of any class which doesn't exist
# NotImplementedError : you can use this error when you are in development phase 

# RuntimeError : this is base error, and other errors inherit from this, its basically error when you are running your program. so it can be anything

# SyntaxError : when you write wrong syntax of python
# IndentationError : more like a syntax error, when you write loop or funciton

# TabError : if you are using tab for indentation inside a one funciotn then stick to that, don't use spacebar for the indentation in another function, it may cause this error

# TypeError : when you try to add 2 different classes, like when you add str and int 
# ValueError : when you pass invalid input, see the example

# ImportError : when you import a file "x" into file "y" and file "y" is also been imported to file "x"
                # this will cause importerror

# DeprecationWarning : you can raise a deprecationwarning for something which still works but it's not a proper way do that !!


# creating our custom error

class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")

# err = CustomError('An error happende.', 500)

raise CustomError('An error happend!.', 500)





"""--------------------------------POLYMORPHISM----------------------------------------"""


"""

1. What is Polymorphism?

The word Polymorphism is derived from two Greek words: Poly (many) and Morphs (forms). In programming, it refers to the ability of a single function, method, or object to behave differently depending on the context.

2. Types of Polymorphism in Python

Polymorphism can be broadly classified into the following types:

A. Duck Typing

Python is dynamically typed. "If it walks like a duck and quacks like a duck, it’s a duck." This means Python focuses on whether an object has a specific method, rather than what the class of the object is.
"""
class File:
    def read(self):
        print("Reading file")

class Database:
    def read(self):
        print("Reading database")

def fetch_data(source):
    source.read()

fetch_data(File())
fetch_data(Database())

"""
B. Operator Overloading

The same operator can behave differently depending on the data type.

Example: The + operator adds two integers (5 + 5 = 10) but concatenates two strings ("Py" + "thon" = "Python").
"""

print(2 + 3)        # 5
print("Hi " + "Bro") # Hi Bro


"""
C. Method Overriding (Run-time Polymorphism)

Occurs in inheritance when a Child class provides a specific implementation of a method that is already defined in its Parent class.
"""
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

a = Animal()
d = Dog()
c = Cat()

a.sound()  # Some sound
d.sound()  # Bark
c.sound()  # Meow

"""

D. Method Overloading (Compile-time Polymorphism)

In many languages, this means having multiple methods with the same name but different parameters. Note: Python does not support traditional method overloading directly; the latest defined method will overwrite previous ones. However, we achieve this using default arguments or variable-length arguments (*args).

3. Polymorphism with Class Methods: Objects within a Loop

This approach involves creating a list of different objects and iterating through them. Even though the objects belong to different classes, we call the same method name on each.

"""
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

# Creating objects
my_cat = Cat()
my_dog = Dog()

# Objects within a Loop
for animal in [my_cat, my_dog]:
    print(f"The animal says: {animal.speak()}")

"""
4. Polymorphism with Class Methods: Objects as Function Arguments

In this case, we create a generic function that accepts an object as a parameter. The function then calls a method on that object without needing to know its specific class type.

"""
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

# Function that takes an object as an argument
def print_capital(country_obj):
    country_obj.capital()

# Creating instances
obj_ind = India()
obj_usa = USA()

# Passing objects to the function
print_capital(obj_ind)
print_capital(obj_usa)



# static polymorphism : compile time polymorphism -> Decision is made before program runs
# method overloading, operator overloading

# dynamic polymorphism : run time polymorphism -> Decision is made while program is running
# method overriding, ducktyping


""" -----------------------OPERATOR OVERLOADING--------------------------------"""

"""
Operator overloading is a key feature in Python that allows us to redefine the behavior of built-in operators (like +, -, *, ==) for our custom objects.

1. Contribution to Static Polymorphism

Operator overloading is a feature where the same operator behaves differently for different data types.
For example, the + operator can perform addition for numbers and concatenation for strings.

🧠 Contribution to Static Polymorphism
Operator overloading is considered a form of static polymorphism because:
The same operator is used for different operations
The behavior is determined based on operand types
The decision is made without changing the operator name

💡 Example in Python
print(2 + 3)          # Addition → 5
print("Hi " + "Bro")  # Concatenation → Hi Bro

👉 Here, + works differently depending on data type.

Thus, operator overloading enables one operator to perform multiple operations, which is a key idea of polymorphism.
Although Python is dynamically typed, operator overloading still demonstrates static polymorphism behavior.

2. Magic Methods Overview

To overload operators, Python provides specific magic methods. Here are the most common ones categorized by their operation:

A. Unary Operators (Single Operand)

Operator	Magic Method	Description
-	__neg__(self)	Overloads unary minus (e.g., -obj)
+	__pos__(self)	Overloads unary plus
abs()	__abs__(self)	Overloads the absolute value function 


B. Binary Operators (Two Operands)

Operator	Magic Method	Description
+	__add__(self, other)	Addition
-	__sub__(self, other)	Subtraction
*	__mul__(self, other)	Multiplication
/	__truediv__(self, other)	Division


C. Comparison Operators

Operator	Magic Method	Description
==	__eq__(self, other)	Equal to
<	__lt__(self, other)	Less than
>	__gt__(self, other)	Greater than
>=	__ge__(self, other)	Greater than or equal to


D. Assignment Operators

These are used for "in-place" operations (e.g., +=).

Operator	Magic Method	Description
+=	__iadd__(self, other)	Addition assignment
-=	__isub__(self, other)	Subtraction assignment


3. Program: Adding Complex Numbers

In this program, we overload the __add__ method to define how two Complex objects should be summed.

"""
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the + operator
    def __add__(self, other):
        # Adding real parts and imaginary parts separately
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    # Overloading the string representation for easy printing
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Creating two complex number objects
c1 = ComplexNumber(3, 5)
c2 = ComplexNumber(1, 2)

# Using the + operator (this calls c1.__add__(c2))
result = c1 + c2

print(f"First Number: {c1}")
print(f"Second Number: {c2}")
print(f"Sum: {result}")






"""--------------------- Abstract class. vs concreat class ----------------------"""

"""
🔥 1. Abstract Class vs Concrete Class

🧠 Abstract Class
An abstract class is like a blueprint with incomplete methods.
It cannot be instantiated (you can't create objects from it directly)

It may contain:
abstract methods (no implementation)
normal methods (with implementation)

👉 Real-life example:
Think of a “Vehicle” blueprint
You know every vehicle must have:
start()
stop()

But how a car starts vs how a bike starts → different.
So you just define:
“Every vehicle must have start and stop methods”
But you DON'T define how.


🧱 Concrete Class
A concrete class is a fully implemented class

You can create objects

All methods are fully defined

👉 Real-life example:
Car 🚗
Bike 🏍️

They implement actual behavior.

"""

"""
Feature	
Abstract Class	
Concrete Class

Definition	
A blueprint for other classes. It cannot be instantiated.	
A complete class used to create objects.

Methods	
Can have both abstract methods (no body) and concrete methods.	
All methods must have a complete implementation.

Purpose	
To provide a common interface/structure for subclasses.	
To perform specific tasks and hold data.

Instantiation	
obj = AbstractClass() will throw an error.	
obj = ConcreteClass() works perfectly. 




2. Why do we use Abstract Base Classes (ABCs)?

ABCs are used to define a formal contract between the base class and its subclasses.

Enforcement: They ensure that any subclass derived from the ABC must implement specific methods, otherwise the subclass cannot be instantiated.

Consistency: They provide a uniform interface across different implementations (e.g., all "Shapes" must have an area() method).

Readability: They make the code more maintainable by clearly defining what a group of related classes should do.


🧠 Think like this:
You’re building a backend system for payments:

You want every payment method to have:
pay()
refund()

If someone creates:
CreditCardPayment
UPI
PayPal

You want to force them to implement these methods.
👉 Without ABC:
Someone might forget → system breaks 💀

👉 With ABC:
Python will literally stop them from creating the class unless they implement required methods.



3. Does Python provide Abstract Classes? (Justification)

Yes, Python provides abstract classes. However, unlike Java or C++, they are not a built-in keyword. Python provides them via a built-in module called abc (Abstract Base Classes).

Justification:
To create an abstract class in Python, a class must:

Inherit from abc.ABC.

Use the @abstractmethod decorator to define methods that subclasses must implement.

Without this module, Python doesn't prevent you from instantiating a class that has "empty" methods. Using the abc module is the formal way to enforce abstraction.

"""
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

"""
4. Method Overriding and Dynamic Polymorphism 

Method Overriding is the mechanism where a child class provides a specific implementation of a method that is already defined in its parent class.

Contribution to Dynamic Polymorphism:
Dynamic Polymorphism (or Run-time Polymorphism) is the ability of a language to determine which method to execute at runtime rather than at compile time.

When you call a method on an object, Python checks the object's type and executes the overridden version in the child class if it exists.

This allows a single interface (method name) to trigger different behaviors depending on which object is calling it.
"""
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Child Class 1
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

# Child Class 2
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# Demonstrating Dynamic Polymorphism
def animal_concert(animal_obj):
    # The program decides which make_sound to call at runtime
    print(animal_obj.make_sound())

# Creating objects
dog = Dog()
cat = Cat()

print("Dog says:")
animal_concert(dog)

print("Cat says:")
animal_concert(cat)

# Attempting to instantiate the Abstract class (Will cause an Error)
# a = Animal() # TypeError: Can't instantiate abstract class Animal






"""-----------------REAL WORLD USE OF PYTHON----------------"""

"""
1. Solving Real-Time Problems with Python

Python is used to address complex, real-world issues across various domains:

Data Science & Analytics: Real-time processing of stock market data or social media trends to predict market shifts or public sentiment.

Artificial Intelligence & ML: Developing diagnostic tools in healthcare that analyze X-rays or MRIs in real-time to detect anomalies.

Automation & Scripting: Automating repetitive office tasks, such as generating thousands of PDF invoices or organizing massive datasets.

Internet of Things (IoT): Using Python on devices like Raspberry Pi to monitor temperature and humidity in smart farms, triggering irrigation systems automatically.

2. Python Libraries for Web Development

Web development in Python is dominated by frameworks that handle the "heavy lifting" (security, database management, and routing).

A. Django (The "Batteries-Included" Framework)

Best for large-scale, complex applications.

Methods/Features: models.Model (Database mapping), urls.path() (Routing), views.APIView (Handling logic).

B. Flask (The Micro-Framework)

Best for small to medium apps or microservices where you want full control.

Methods/Features: Flask(), @app.route() (Routing decorator), render_template() (Rendering HTML).

C. Requests (For API Interaction)

Used to send HTTP requests to other servers.

Methods: requests.get(), requests.post().

3. Code Fragments for Web Development

Below are small snippets showing how these libraries function in a real-world project context.

I. Basic Routing with Flask

This snippet shows how to create a simple web server that handles a "Home" page.

Python
from flask import Flask

app = Flask(__name__)

# Method: @app.route defines the URL path
@app.route('/')
def home():
    return "<h1>Welcome to the Real-Time Dashboard</h1>"

if __name__ == "__main__":
    app.run(debug=True)
II. Database Modeling with Django

This defines a "Product" structure for an e-commerce site. Django automatically converts this into a SQL database table.

Python
from django.db import models

class Product(models.Model):
    # Method: CharField and DecimalField define data types
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField()

    def __str__(self):
        return self.name
III. Handling External Data with Requests

Often, web apps need to fetch real-time data (like weather or currency rates) from other services.

Python
import requests

def get_weather(city):
    api_url = f"https://api.weatherapi.com/v1/current.json?key=API_KEY&q={city}"
    
    # Method: requests.get() fetches data from the URL
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data['current']['temp_c']
    return "Error fetching data"

    
4. Summary Table for Web Libraries

Library	    Primary Use	            Common Methods
Flask	    Quick API/Web Dev	    route(), request(), jsonify()
Django	    Robust Web Apps	        objects.all(), save(), filter()
SQLAlchemy	Database ORM	        session.add(), query.filter_by()
FastAPI	    High-performance APIs	get(), post(), Body()


"""




#----------------------- classification vs clustring ---------------------------

"""

In Machine Learning, both Classification and Clustering are used to identify patterns in data, but they operate under completely different paradigms: Supervised vs. Unsupervised learning.

1. Classification vs. Clustering

Classification (Supervised Learning)

Classification is the process of predicting the categorical label of new observations based on past training data. The data is "labeled," meaning the computer already knows the categories (e.g., "Spam" or "Not Spam") during the training phase.

Goal: To find a boundary that separates different classes.

Example: Predicting whether an image is of a 'Cat' or a 'Dog'.

Clustering (Unsupervised Learning)

Clustering is the process of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups. There are no predefined labels; the algorithm finds patterns on its own.

Goal: To discover hidden structures or groupings in the data.

Example: Segmenting customers into different groups based on their purchasing behavior for targeted marketing.

2. Python Libraries and Methods

Python provides robust libraries to implement these techniques efficiently.

Technique	        Library	        Common Methods/Algorithms

Classification	    Scikit-learn	LogisticRegression(), RandomForestClassifier(), SVC() 
                                    (Support Vector Machine), KNeighborsClassifier()
Clustering	        Scikit-learn	KMeans(), AgglomerativeClustering(), DBSCAN()

Data Handling	Pandas / NumPy	read_csv(), array(), iloc[]

"""

""" Classification Example """
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# load data
data = load_iris()
X = data.data
y = data.target

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = LogisticRegression()
model.fit(X_train, y_train)

# prediction
pred = model.predict(X_test)

print(pred)


"""Clustering Example"""
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,2], [1,4], [1,0],
              [10,2], [10,4], [10,0]])

model = KMeans(n_clusters=2)
model.fit(X)

print(model.labels_)


"""
3. Does Python support Deep Learning? (Justification)

Yes, Python is the industry standard for developing Deep Learning (DL) models. It serves as the primary interface for almost all major DL frameworks.

Reasons for Python's Dominance in DL:

Rich Ecosystem: Python offers specialized libraries like TensorFlow, Keras, and PyTorch that simplify the creation of complex neural networks.

Hardware Acceleration: These libraries allow Python code to run on GPUs (Graphics Processing Units) and TPUs, which is essential for the massive matrix multiplications required in DL.

Community & Research: Most cutting-edge research papers in AI release their official implementations in Python.

C/C++ Integration: While Python is high-level, the backend of DL libraries is written in C++ for speed, giving Python "the best of both worlds."

Examples of Deep Learning Methods in Python:

Convolutional Neural Networks (CNNs): Used for Image Recognition (Implemented via torch.nn or keras.layers.Conv2D).

Recurrent Neural Networks (RNNs): Used for Natural Language Processing and Time-series prediction.

Generative Adversarial Networks (GANs): Used to generate realistic images or videos.
"""

"""Simple Neural Network (Keras)"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

print("Model created 🚀")


#--------------- Python in Research -----------------

"""
1. How Python is used to solve research problems
Python is heavily used in research because it helps in:

🔬 Key roles:
-> Data collection (from sensors, APIs, experiments)
-> Data analysis (statistics, ML)
-> Simulation & modeling
-> Visualization
-> Automation of experiments

📦 Real-life research examples

🏥 1. Medical Research
👉 Predict diseases using patient data
ML models detect diabetes, cancer risk

🧬 2. Bioinformatics
👉 DNA sequence analysis
Pattern matching in genes

🌍 3. Environmental Research
👉 Air quality monitoring using IoT sensors
Analyze pollution trends

❤️ 4. Smart Healthcare IoT
👉 Wearables track:
heart rate
oxygen level
temperature
Python processes this data → alerts doctors if abnormal
"""

"""
2. Python Libraries for Healthcare IoT

🔥 1. NumPy
👉 Numerical data processing
np.array()
np.mean()
np.std()

📊 2. pandas
👉 Data handling
read_csv()
DataFrame()
describe()

📈 3. matplotlib
👉 Visualization
plt.plot()
plt.show()

🌐 4. requests
👉 Send/receive data from cloud APIs
requests.get()
requests.post()

📡 5. paho-mqtt (IoT communication)
👉 For sensor data transfer
client.connect()
client.publish()
client.subscribe()

🤖 6. scikit-learn
👉 ML for prediction
model.fit()
model.predict()
"""

# Example 1: Simulating Sensor Data
import numpy as np

# simulate heart rate data
heart_rate = np.array([72, 75, 78, 120, 76])

avg = np.mean(heart_rate)

print("Average Heart Rate:", avg)



# Example 2: Store & Analyze Data
import pandas as pd

data = {
    "HeartRate": [72, 75, 120, 80],
    "Temp": [98.6, 99.1, 101.2, 98.4]
}

df = pd.DataFrame(data)

print(df.describe())



# Example 3: Plot Health Data
import matplotlib.pyplot as plt

heart_rate = [72, 75, 78, 120, 76]

plt.plot(heart_rate)
plt.title("Heart Rate Monitoring")
plt.show()



# Example 4: Send Data to Server
import requests

data = {"heart_rate": 120}

response = requests.post("https://example.com/api", json=data)

print(response.status_code)



# Example 6: Simple ML Prediction
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[70], [75], [120], [80]])  # heart rate
y = np.array([0, 0, 1, 0])  # 1 = abnormal

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[110]]))

"""
4. Why Python for Healthcare Research?

Speed of Development: Researchers can prototype algorithms quickly without worrying about complex memory management.

Accuracy: Built-in scientific libraries are peer-reviewed and highly accurate for clinical calculations.

Visualization: Converting complex biological data into heatmaps or 3D models helps in better diagnosis.
"""