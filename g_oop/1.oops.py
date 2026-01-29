"""
================================================================================
        OBJECT-ORIENTED PROGRAMMING IN PYTHON - COMPLETE DEEP DIVE
================================================================================
Author: Your Python Professor & Ex-Google/Microsoft SDE-3
Purpose: Comprehensive OOP guide for future reference
Level: Beginner to Advanced
================================================================================

TABLE OF CONTENTS:
1. Introduction to OOP
2. Classes and Objects (Deep Dive)
3. The Four Pillars of OOP
   - Encapsulation
   - Inheritance
   - Polymorphism
   - Abstraction
4. Advanced OOP Concepts
5. Magic Methods (Dunder Methods)
6. Design Patterns
7. Best Practices
8. Real-world Examples

================================================================================
"""

# ============================================================================
# 1. INTRODUCTION TO OOP
# ============================================================================

"""
WHAT IS OOP?
------------
Object-Oriented Programming is a programming paradigm that organizes code 
into objects that contain both data (attributes) and behavior (methods).

WHY OOP?
--------
1. Code Reusability - Write once, use many times
2. Modularity - Break complex problems into smaller, manageable pieces
3. Maintainability - Easier to update and debug
4. Scalability - Easy to extend functionality
5. Real-world modeling - Maps naturally to real-world entities

PROCEDURAL vs OOP:
------------------
Procedural: Functions operate on data (data and behavior are separate)
OOP: Objects contain both data and behavior together
"""


# ============================================================================
# 2. CLASSES AND OBJECTS - DEEP DIVE
# ============================================================================

"""
CLASS: A blueprint/template for creating objects
OBJECT: An instance of a class (actual entity created from the blueprint)

Analogy: 
- Class = Cookie cutter (blueprint)
- Object = Actual cookie (instance)
"""

# -----------------------------
# 2.1 Basic Class Structure
# -----------------------------

class Student:
    """
    A class representing a student.
    
    This is a docstring - always document your classes!
    """
    
    # Class variable (shared by all instances), common to each object
    school_name = "Python University"
    total_students = 0
    
    def __init__(self, name, age, grade):
        """
        Constructor method - called when object is created
        """
        # Instance variables (unique to each object)
        self.name = name
        self.age = age
        self.grade = grade
        
        # Increment class variable
        Student.total_students += 1
    
    # Instance method (operates on instance)
    def study(self, subject):
        """Student studies a subject"""
        return f"{self.name} is studying {subject}"
    
    # Instance method
    def get_info(self):
        """Returns student information"""
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    # Class method (operates on class, not instance)
    @classmethod
    def get_school_name(cls):
        """Returns the school name"""
        return cls.school_name
    
    @classmethod
    def change_school_name(cls, new_name):
        """Changes school name for all students"""
        cls.school_name = new_name
    
    # Static method (doesn't operate on class or instance)
    # they are utility functions related to the class, used when no access to class or instance is needed
    # you can define them using @staticmethod decorator, you don't need to pass self or cls parameter
    @staticmethod
    def is_adult(age):
        """Checks if age qualifies as adult"""
        return age >= 18
    
    # Destructor (called when object is deleted)
    def __del__(self):
        """Destructor - cleanup when object is destroyed"""
        Student.total_students -= 1
        print(f"Student {self.name} record deleted")


# Creating objects (instances)
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 17, "B")
student3 = Student("Charlie", 22, "A+")

print(student1.study("Python"))  # Alice is studying Python
print(student2.get_info())       # Name: Bob, Age: 17, Grade: B

# Accessing class variables
print(Student.school_name)       # Python University
print(Student.total_students)    # 3

# Using class method
Student.change_school_name("Advanced Python Academy")
print(student1.school_name)      # Advanced Python Academy (changed for all!)

# Using static method, static methods are called using the class name
print(Student.is_adult(student1.age))  # True
print(Student.is_adult(student2.age))  # False


# -----------------------------
# 2.2 The 'self' Parameter - Deep Understanding
# -----------------------------

"""
'self' is a reference to the current instance of the class.
It's used to access variables and methods of that specific instance.

Think of 'self' as "this particular object"
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # self.account_number = THIS account's number
        self.balance = balance                # self.balance = THIS account's balance
    
    def deposit(self, amount):
        self.balance += amount  # Modify THIS account's balance
        return self.balance
    
    def transfer(self, other_account, amount):
        """
        Transfer money to another account
        'self' = sender account
        'other_account' = receiver account
        """
        if self.balance >= amount:
            self.balance -= amount           # Deduct from THIS account
            other_account.balance += amount  # Add to OTHER account
            return True
        return False

# Demo
acc1 = BankAccount("123", 1000)
acc2 = BankAccount("456", 500)

acc1.transfer(acc2, 200)  # self=acc1, other_account=acc2
print(f"Account 1: ${acc1.balance}")  # $800
print(f"Account 2: ${acc2.balance}")  # $700


# -----------------------------
# 2.3 Class Variables vs Instance Variables - Deep Dive
# -----------------------------

"""
CLASS VARIABLES:
- Shared by all instances
- Defined outside __init__
- Modified using ClassName.variable

INSTANCE VARIABLES:
- Unique to each instance
- Defined inside __init__ with self
- Modified using self.variable
"""

class Employee:
    # Class variables
    company = "Google"
    employee_count = 0
    salary_raise_percentage = 0.04  # 4% annual raise
    
    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def apply_raise(self):
        """Apply the standard company raise"""
        self.salary = self.salary * (1 + Employee.salary_raise_percentage)
    
    @classmethod
    def set_raise_percentage(cls, new_percentage):
        """Change raise percentage for entire company"""
        cls.salary_raise_percentage = new_percentage

# Demo
emp1 = Employee("Alice", 100000)
emp2 = Employee("Bob", 120000)

print(f"Company: {Employee.company}")  # Google
print(f"Employees: {Employee.employee_count}")  # 2

emp1.apply_raise()
print(f"Alice new salary: ${emp1.salary}")  # $104,000

# Change raise for entire company
Employee.set_raise_percentage(0.10)  # 10% raise now!
emp2.apply_raise()
print(f"Bob new salary: ${emp2.salary}")  # $132,000


# -----------------------------
# 2.4 Public, Protected, and Private Members
# -----------------------------

"""
PYTHON NAMING CONVENTIONS:
--------------------------
public:    variable      - Accessible from anywhere
protected: _variable     - Should not be accessed outside class (convention only)
private:   __variable    - Name mangling applied, harder to access

Note: Python doesn't have true private members (unlike Java/C++).
The __ prefix is a convention that triggers name mangling.
"""

class SecureAccount:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number    # Public
        self._balance = balance                 # Protected (convention)
        self.__pin = pin                        # Private (name mangled)
    
    def verify_pin(self, pin):
        """Public method to verify PIN"""
        return self.__pin == pin
    
    def get_balance(self):
        """Public method to access protected balance"""
        return self._balance
    
    def __internal_audit(self):
        """Private method - only used internally"""
        print("Performing internal audit...")
    
    def perform_transaction(self):
        """Public method that uses private method"""
        self.__internal_audit()  # Can call private method internally
        print("Transaction completed")


# Demo
account = SecureAccount("ACC123", 5000, "1234")

# Public access
print(account.account_number)  # ACC123 ✓

# Protected access (works but shouldn't be used)
print(account._balance)  # 5000 (accessible but discouraged)

# Private access (name mangled)
# print(account.__pin)  # ❌ AttributeError!

# Correct way to access private data
print(account.verify_pin("1234"))  # True ✓

# Name mangling explanation, name mangling means Python changes the name of the variable to include the class name, if you really want to access it (not recommended)
print(account._SecureAccount__pin)  # 1234 (this is how Python mangles it)
# Format: _ClassName__variable 


# ============================================================================
# 3. THE FOUR PILLARS OF OOP - DEEP DIVE
# ============================================================================

# ==================================
# 3.1 ENCAPSULATION - Deep Dive
# ==================================

"""
ENCAPSULATION: Bundling data and methods that operate on that data within 
a single unit (class), and restricting direct access to some components.

BENEFITS:
1. Data Hiding - Protect object's internal state
2. Controlled Access - Use getters/setters for validation
3. Flexibility - Change internal implementation without breaking external code
4. Security - Prevent unauthorized modifications
"""

class BankAccountAdvanced:
    """
    Advanced bank account with full encapsulation
    """
    
    # Class variable for interest rate
    _interest_rate = 0.03
    
    def __init__(self, account_holder, initial_balance=0):
        self.__account_holder = account_holder  # Private
        self.__balance = initial_balance        # Private
        self.__transaction_history = []         # Private
        self.__is_active = True                 # Private
    
    # Getter for balance (read-only access)
    @property
    def balance(self):
        """Get current balance"""
        if not self.__is_active:
            raise Exception("Account is inactive!")
        return self.__balance
    
    # Getter for account holder
    @property
    def account_holder(self):
        """Get account holder name"""
        return self.__account_holder
    
    # Setter for account holder (with validation)
    @account_holder.setter
    def account_holder(self, name):
        """Set account holder name with validation"""
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        self.__account_holder = name
    
    def deposit(self, amount):
        """Deposit money with validation"""
        if not self.__is_active:
            raise Exception("Account is inactive!")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.__balance += amount
        self.__add_transaction(f"Deposit: +${amount}")
        return self.__balance
    
    def withdraw(self, amount):
        """Withdraw money with validation"""
        if not self.__is_active:
            raise Exception("Account is inactive!")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount
        self.__add_transaction(f"Withdrawal: -${amount}")
        return self.__balance
    
    def __add_transaction(self, transaction):
        """Private method to record transactions"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history.append(f"{timestamp} - {transaction}")
    
    def get_transaction_history(self):
        """Get copy of transaction history"""
        return self.__transaction_history.copy()  # Return copy, not original
    
    def apply_interest(self):
        """Apply interest to balance"""
        interest = self.__balance * self._interest_rate
        self.__balance += interest
        self.__add_transaction(f"Interest: +${interest:.2f}")
    
    def close_account(self):
        """Close the account"""
        self.__is_active = False
        self.__add_transaction("Account closed")


# Demo - Encapsulation in Action
account = BankAccountAdvanced("John Doe", 1000)

# Using properties (looks like attribute access, but uses getters/setters)
print(account.balance)         # 1000 (using @property getter)
print(account.account_holder)  # John Doe

# Validation through setter
try:
    account.account_holder = ""  # ❌ Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# Controlled modification through methods
account.deposit(500)
account.withdraw(200)
account.apply_interest()

# Access transaction history (gets a copy, not the original)
history = account.get_transaction_history()
print("\nTransaction History:")
for transaction in history:
    print(transaction)

# Cannot directly modify private data
# account.__balance = 999999  # ❌ Won't work due to name mangling


# ==================================
# 3.2 INHERITANCE - Deep Dive
# ==================================

"""
INHERITANCE: Mechanism where a new class (child/derived) inherits attributes 
and methods from an existing class (parent/base).

TYPES OF INHERITANCE:
1. Single Inheritance - One parent, one child
2. Multiple Inheritance - Multiple parents, one child
3. Multilevel Inheritance - Chain of inheritance
4. Hierarchical Inheritance - One parent, multiple children
5. Hybrid Inheritance - Combination of above
"""

# -----------------------------
# Single Inheritance
# -----------------------------

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, species="Canine")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        return f"{self.name} says Woof! 🐕"
    
    # New method specific to Dog
    def fetch(self, item):
        return f"{self.name} fetched the {item}!"


# Demo
dog = Dog("Buddy", "Golden Retriever")
print(dog.eat())         # Inherited from Animal
print(dog.make_sound())  # Overridden in Dog
print(dog.fetch("ball")) # Specific to Dog


# -----------------------------
# Multiple Inheritance
# -----------------------------

"""
Multiple Inheritance: A class can inherit from multiple parent classes.
Be careful with the Method Resolution Order (MRO)!
"""

class Flyer:
    """Mixin for flying ability"""
    def fly(self):
        return f"{self.name} is flying!"


class Swimmer:
    """Mixin for swimming ability"""
    def swim(self):
        return f"{self.name} is swimming!"


class Duck(Animal, Flyer, Swimmer):
    """Duck can fly and swim"""
    
    def __init__(self, name):
        super().__init__(name, species="Waterfowl")
    
    def make_sound(self):
        return f"{self.name} says Quack! 🦆"


# Demo
duck = Duck("Donald")
print(duck.make_sound())  # From Duck
print(duck.eat())         # From Animal
print(duck.fly())         # From Flyer
print(duck.swim())        # From Swimmer

# Check Method Resolution Order
print("\nMethod Resolution Order:")
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Animal'>, 
#  <class '__main__.Flyer'>, <class '__main__.Swimmer'>, 
#  <class 'object'>)


# -----------------------------
# Multilevel Inheritance
# -----------------------------

class LivingBeing:
    """Top-level class"""
    def __init__(self):
        self.is_alive = True
    
    def breathe(self):
        return "Breathing..."


class Mammal(LivingBeing):
    """Inherits from LivingBeing"""
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.warm_blooded = True
    
    def feed_young(self):
        return "Feeding young with milk"


class Primate(Mammal):
    """Inherits from Mammal"""
    def __init__(self, name, intelligence_level):
        super().__init__(name)
        self.intelligence_level = intelligence_level
    
    def use_tools(self):
        return f"{self.name} is using tools!"


class Human(Primate):
    """Inherits from Primate"""
    def __init__(self, name, intelligence_level, language):
        super().__init__(name, intelligence_level)
        self.language = language
    
    def speak(self):
        return f"{self.name} speaks {self.language}"


# Demo - Multilevel Inheritance
human = Human("Alice", intelligence_level=95, language="English")
print(human.breathe())      # From LivingBeing
print(human.feed_young())   # From Mammal
print(human.use_tools())    # From Primate
print(human.speak())        # From Human


# -----------------------------
# Abstract Base Classes
# -----------------------------

"""
Abstract classes cannot be instantiated and are meant to be inherited.
They define a template for derived classes. 
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Must be implemented by child classes"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Must be implemented by child classes"""
        pass
    
    def describe(self):
        """Concrete method (can be used as-is)"""
        return f"A {self.color} shape"


class Rectangle(Shape):
    """Concrete class implementing Shape"""
    
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete class implementing Shape"""
    
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


# Demo
# shape = Shape("red")  # ❌ TypeError: Can't instantiate abstract class

rect = Rectangle("blue", 5, 3)
circle = Circle("red", 7)

print(f"Rectangle area: {rect.area()}")           # 15
print(f"Rectangle perimeter: {rect.perimeter()}") # 16
print(f"Circle area: {circle.area():.2f}")        # 153.94
print(circle.describe())                          # A red shape


# ==================================
# 3.3 POLYMORPHISM - Deep Dive
# ==================================

"""
POLYMORPHISM: The ability of different objects to respond to the same 
method call in different ways.

TYPES:
1. Method Overriding - Child class provides specific implementation
2. Method Overloading - Same method name, different parameters (not directly supported in Python)
3. Duck Typing - "If it walks like a duck and quacks like a duck, it's a duck"
4. Operator Overloading - Define behavior of operators for custom objects
"""

# -----------------------------
# Method Overriding (Runtime Polymorphism)
# -----------------------------

class PaymentMethod:
    """Base class for payment methods"""
    
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement this method")


class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card ending in {self.card_number[-4:]}"


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal account {self.email}"


class Bitcoin(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount):
        return f"Processing ${amount} via Bitcoin wallet {self.wallet_address[:10]}..."


# Polymorphism in action - same method, different behavior
def checkout(payment_method, amount):
    """
    This function doesn't care what type of payment method it is.
    It just knows it has a process_payment method.
    """
    print(payment_method.process_payment(amount))


# Demo
payments = [
    CreditCard("1234-5678-9012-3456"),
    PayPal("user@example.com"),
    Bitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
]

for payment in payments:
    checkout(payment, 100)  # Same call, different behaviors!


# -----------------------------
# Duck Typing
# -----------------------------

"""
Duck Typing: Type checking based on object behavior rather than class.
"If it looks like a duck and quacks like a duck, it must be a duck"
"""

class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying with wings!"


class Person:
    def quack(self):
        return "I'm imitating a duck: Quack!"
    
    def fly(self):
        return "I'm flapping my arms!"


class Airplane:
    def fly(self):
        return "Flying with engines!"


def make_it_quack(thing):
    """
    Doesn't check type - just tries to call quack()
    If it has quack(), it works!
    """
    try:
        print(thing.quack())
    except AttributeError:
        print(f"{thing.__class__.__name__} can't quack!")


def make_it_fly(thing):
    """Duck typing - if it has fly(), call it!"""
    try:
        print(thing.fly())
    except AttributeError:
        print(f"{thing.__class__.__name__} can't fly!")


# Demo
duck = Duck()
person = Person()
plane = Airplane()

make_it_quack(duck)    # Quack!
make_it_quack(person)  # I'm imitating a duck: Quack!
make_it_quack(plane)   # Airplane can't quack!

make_it_fly(duck)      # Flying with wings!
make_it_fly(person)    # I'm flapping my arms!
make_it_fly(plane)     # Flying with engines!


# -----------------------------
# Operator Overloading
# -----------------------------

"""
Operator Overloading: Define custom behavior for operators (+, -, *, etc.)
using magic methods (dunder methods)
"""

class Vector:
    """2D Vector class with operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Official representation"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        """Overload abs() function"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __len__(self):
        """Overload len() function"""
        return 2  # 2D vector has 2 components
    
    def __getitem__(self, index):
        """Overload [] operator"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")


# Demo - Operator Overloading
v1 = Vector(2, 3)
v2 = Vector(5, 7)

print(v1 + v2)      # Vector(7, 10) - using __add__
print(v1 - v2)      # Vector(-3, -4) - using __sub__
print(v1 * 3)       # Vector(6, 9) - using __mul__
print(v1 == v2)     # False - using __eq__
print(abs(v1))      # 3.605... - using __abs__
print(len(v1))      # 2 - using __len__
print(v1[0], v1[1]) # 2, 3 - using __getitem__


# ==================================
# 3.4 ABSTRACTION - Deep Dive
# ==================================

"""
ABSTRACTION: Hiding complex implementation details and showing only 
essential features of an object.

KEY CONCEPTS:
1. Abstract classes - Cannot be instantiated
2. Abstract methods - Must be implemented by child classes
3. Interface-like behavior - Define contracts that classes must follow
"""

from abc import ABC, abstractmethod

class Database(ABC):
    """
    Abstract Database class
    Defines interface that all database implementations must follow
    """
    
    @abstractmethod
    def connect(self):
        """Connect to database"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Disconnect from database"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute a query"""
        pass
    
    # Concrete method (shared by all databases)
    def log_query(self, query):
        """Log the query (concrete implementation)"""
        print(f"[LOG] Executing: {query}")


class MySQLDatabase(Database):
    """MySQL implementation"""
    
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.connection = None
    
    def connect(self):
        self.connection = f"MySQL Connection to {self.host}"
        print(f"✓ Connected to MySQL at {self.host}")
    
    def disconnect(self):
        self.connection = None
        print("✓ Disconnected from MySQL")
    
    def execute_query(self, query):
        self.log_query(query)  # Use inherited method
        print(f"✓ MySQL: Executing '{query}'")


class MongoDBDatabase(Database):
    """MongoDB implementation"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def connect(self):
        self.connection = f"MongoDB Connection to {self.host}:{self.port}"
        print(f"✓ Connected to MongoDB at {self.host}:{self.port}")
    
    def disconnect(self):
        self.connection = None
        print("✓ Disconnected from MongoDB")
    
    def execute_query(self, query):
        self.log_query(query)  # Use inherited method
        print(f"✓ MongoDB: Executing '{query}'")


class PostgreSQLDatabase(Database):
    """PostgreSQL implementation"""
    
    def __init__(self, host, database_name):
        self.host = host
        self.database_name = database_name
        self.connection = None
    
    def connect(self):
        self.connection = f"PostgreSQL Connection to {self.host}/{self.database_name}"
        print(f"✓ Connected to PostgreSQL: {self.database_name}")
    
    def disconnect(self):
        self.connection = None
        print("✓ Disconnected from PostgreSQL")
    
    def execute_query(self, query):
        self.log_query(query)  # Use inherited method
        print(f"✓ PostgreSQL: Executing '{query}'")


# Database Manager - Works with any database implementation
class DatabaseManager:
    """
    High-level abstraction - doesn't care about database type
    Only cares that it implements the Database interface
    """
    
    def __init__(self, database: Database):
        self.database = database
    
    def run_query(self, query):
        """
        Run a query without knowing database specifics
        This is the power of abstraction!
        """
        self.database.connect()
        self.database.execute_query(query)
        self.database.disconnect()


# Demo - Abstraction in Action
print("\n=== Using MySQL ===")
mysql = MySQLDatabase("localhost", "admin", "password123")
manager1 = DatabaseManager(mysql)
manager1.run_query("SELECT * FROM users")

print("\n=== Using MongoDB ===")
mongo = MongoDBDatabase("localhost", 27017)
manager2 = DatabaseManager(mongo)
manager2.run_query("db.users.find()")

print("\n=== Using PostgreSQL ===")
postgres = PostgreSQLDatabase("localhost", "myapp_db")
manager3 = DatabaseManager(postgres)
manager3.run_query("SELECT * FROM users WHERE active = true")


# ============================================================================
# 4. ADVANCED OOP CONCEPTS
# ============================================================================

# -----------------------------
# 4.1 Composition vs Inheritance
# -----------------------------

"""
COMPOSITION: "HAS-A" relationship
INHERITANCE: "IS-A" relationship

Rule of Thumb: Favor composition over inheritance when possible
"""

# Bad: Using inheritance when composition is better
# class ElectricCarBad(Car):  # IS-A relationship - awkward!

# Good: Using composition
class Engine:
    """Engine component"""
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower
    
    def start(self):
        return f"{self.engine_type} engine started ({self.horsepower} HP)"
    
    def stop(self):
        return f"{self.engine_type} engine stopped"


class Battery:
    """Battery component"""
    def __init__(self, capacity, voltage):
        self.capacity = capacity
        self.voltage = voltage
        self.charge = capacity
    
    def recharge(self):
        self.charge = self.capacity
        return f"Battery recharged to {self.capacity} kWh"
    
    def use_power(self, amount):
        self.charge = max(0, self.charge - amount)


class Vehicle:
    """Vehicle using composition"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class GasolineCar(Vehicle):
    """Has-A Engine"""
    def __init__(self, brand, model, engine_type, horsepower):
        super().__init__(brand, model)
        self.engine = Engine(engine_type, horsepower)  # HAS-A relationship
    
    def start(self):
        return self.engine.start()


class ElectricCar(Vehicle):
    """Has-A Battery"""
    def __init__(self, brand, model, battery_capacity, battery_voltage):
        super().__init__(brand, model)
        self.battery = Battery(battery_capacity, battery_voltage)  # HAS-A relationship
    
    def charge(self):
        return self.battery.recharge()


# Demo
gas_car = GasolineCar("Ford", "Mustang", "V8", 450)
electric_car = ElectricCar("Tesla", "Model S", 100, 400)

print(gas_car.start())
print(electric_car.charge())


# -----------------------------
# 4.2 Mixins
# -----------------------------

"""
MIXINS: Small classes that provide additional functionality.
They're not meant to stand alone, but to be mixed into other classes.
"""

class TimestampMixin:
    """Adds timestamp functionality to any class"""
    def __init__(self):
        from datetime import datetime
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def touch(self):
        """Update the updated_at timestamp"""
        from datetime import datetime
        self.updated_at = datetime.now()


class SerializableMixin:
    """Adds JSON serialization to any class"""
    def to_dict(self):
        """Convert object to dictionary"""
        return {k: v for k, v in self.__dict__.items() 
                if not k.startswith('_')}
    
    def to_json(self):
        """Convert object to JSON string"""
        import json
        return json.dumps(self.to_dict(), default=str)


class ValidatableMixin:
    """Adds validation functionality"""
    def validate(self):
        """Validate object state"""
        errors = []
        for key, value in self.__dict__.items():
            if value is None:
                errors.append(f"{key} cannot be None")
        return errors


# Using mixins
class User(TimestampMixin, SerializableMixin, ValidatableMixin):
    """User class with multiple mixins"""
    def __init__(self, username, email):
        TimestampMixin.__init__(self)
        self.username = username
        self.email = email


# Demo
user = User("john_doe", "john@example.com")
print(f"Created at: {user.created_at}")
print(f"JSON: {user.to_json()}")

import time
time.sleep(1)
user.touch()
print(f"Updated at: {user.updated_at}")


# -----------------------------
# 4.3 Metaclasses (Advanced!)
# -----------------------------

"""
METACLASSES: Classes that create classes.
"Classes are instances of metaclasses"

Warning: This is advanced! You rarely need this, but it's powerful.
As Tim Peters said: "Metaclasses are deeper magic than 99% of users 
should ever worry about."
"""

class SingletonMeta(type):
    """
    Metaclass that creates Singleton classes.
    Only one instance of the class can exist.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Using Singleton pattern via metaclass"""
    def __init__(self, host):
        self.host = host
        print(f"Creating connection to {host}")


# Demo - Singleton pattern
db1 = DatabaseConnection("localhost")  # Creating connection to localhost
db2 = DatabaseConnection("localhost")  # No new connection created!
db3 = DatabaseConnection("remote")     # No new connection created!

print(db1 is db2 is db3)  # True - all are the same instance!


# -----------------------------
# 4.4 Descriptors (Advanced!)
# -----------------------------

"""
DESCRIPTORS: Objects that customize attribute access.
They implement __get__, __set__, and/or __delete__ methods.
"""

class PositiveNumber:
    """Descriptor that only allows positive numbers"""
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]


class Product:
    """Product class using descriptors for validation"""
    price = PositiveNumber("price")
    quantity = PositiveNumber("quantity")
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price      # Validated by descriptor
        self.quantity = quantity # Validated by descriptor


# Demo
product = Product("Laptop", 999.99, 5)
print(f"Price: ${product.price}")

try:
    product.price = -100  # ❌ Raises ValueError
except ValueError as e:
    print(f"Error: {e}")


# -----------------------------
# 4.5 Context Managers
# -----------------------------

"""
CONTEXT MANAGERS: Objects that define runtime context using 'with' statement.
Implement __enter__ and __exit__ methods.
"""

class FileManager:
    """Custom context manager for file operations"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()
        
        # Handle exceptions if needed
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        
        return False  # Don't suppress exceptions


# Demo
# with FileManager("test.txt", "w") as f:
#     f.write("Hello, World!")
# File automatically closed after 'with' block


class DatabaseTransaction:
    """Context manager for database transactions"""
    def __init__(self, db_connection):
        self.connection = db_connection
        self.transaction = None
    
    def __enter__(self):
        print("Beginning transaction...")
        self.transaction = "Active Transaction"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Committing transaction...")
            # self.connection.commit()
        else:
            print("Rolling back transaction...")
            # self.connection.rollback()
        return False


# Demo
# with DatabaseTransaction(some_db) as transaction:
#     # Do database operations
#     pass
# Transaction automatically committed or rolled back


# ============================================================================
# 5. MAGIC METHODS (DUNDER METHODS) - COMPLETE REFERENCE
# ============================================================================

"""
MAGIC METHODS: Special methods with double underscores.
They enable operator overloading and custom behavior.
"""

class CompleteExample:
    """Class demonstrating all major magic methods"""
    
    # ----------------
    # Initialization
    # ----------------
    def __init__(self, value):
        """Constructor"""
        self.value = value
    
    def __new__(cls, *args, **kwargs):
        """Called before __init__ to create instance"""
        print("Creating new instance")
        return super().__new__(cls)
    
    def __del__(self):
        """Destructor (called when object is garbage collected)"""
        print(f"Deleting instance with value {self.value}")
    
    # ----------------
    # Representation
    # ----------------
    def __str__(self):
        """String representation for print()"""
        return f"CompleteExample({self.value})"
    
    def __repr__(self):
        """Official string representation"""
        return f"CompleteExample(value={self.value})"
    
    def __format__(self, format_spec):
        """Custom string formatting"""
        return f"Formatted: {self.value:{format_spec}}"
    
    # ----------------
    # Comparison Operators
    # ----------------
    def __eq__(self, other):
        """Equal to: =="""
        return self.value == other.value
    
    def __ne__(self, other):
        """Not equal to: !="""
        return self.value != other.value
    
    def __lt__(self, other):
        """Less than: <"""
        return self.value < other.value
    
    def __le__(self, other):
        """Less than or equal: <="""
        return self.value <= other.value
    
    def __gt__(self, other):
        """Greater than: >"""
        return self.value > other.value
    
    def __ge__(self, other):
        """Greater than or equal: >="""
        return self.value >= other.value
    
    # ----------------
    # Arithmetic Operators
    # ----------------
    def __add__(self, other):
        """Addition: +"""
        return CompleteExample(self.value + other.value)
    
    def __sub__(self, other):
        """Subtraction: -"""
        return CompleteExample(self.value - other.value)
    
    def __mul__(self, other):
        """Multiplication: *"""
        return CompleteExample(self.value * other.value)
    
    def __truediv__(self, other):
        """Division: /"""
        return CompleteExample(self.value / other.value)
    
    def __floordiv__(self, other):
        """Floor division: //"""
        return CompleteExample(self.value // other.value)
    
    def __mod__(self, other):
        """Modulo: %"""
        return CompleteExample(self.value % other.value)
    
    def __pow__(self, other):
        """Power: **"""
        return CompleteExample(self.value ** other.value)
    
    # ----------------
    # Unary Operators
    # ----------------
    def __neg__(self):
        """Negation: -obj"""
        return CompleteExample(-self.value)
    
    def __pos__(self):
        """Positive: +obj"""
        return CompleteExample(+self.value)
    
    def __abs__(self):
        """Absolute value: abs(obj)"""
        return CompleteExample(abs(self.value))
    
    # ----------------
    # Type Conversion
    # ----------------
    def __int__(self):
        """Convert to int: int(obj)"""
        return int(self.value)
    
    def __float__(self):
        """Convert to float: float(obj)"""
        return float(self.value)
    
    def __bool__(self):
        """Convert to bool: bool(obj)"""
        return bool(self.value)
    
    # ----------------
    # Container Methods
    # ----------------
    def __len__(self):
        """Length: len(obj)"""
        return len(str(self.value))
    
    def __getitem__(self, key):
        """Get item: obj[key]"""
        return str(self.value)[key]
    
    def __setitem__(self, key, value):
        """Set item: obj[key] = value"""
        pass  # Implement as needed
    
    def __delitem__(self, key):
        """Delete item: del obj[key]"""
        pass  # Implement as needed
    
    def __contains__(self, item):
        """Membership test: item in obj"""
        return item in str(self.value)
    
    # ----------------
    # Callable
    # ----------------
    def __call__(self, *args, **kwargs):
        """Make object callable: obj()"""
        return f"Called with args={args}, kwargs={kwargs}"
    
    # ----------------
    # Attribute Access
    # ----------------
    def __getattr__(self, name):
        """Called when attribute not found"""
        return f"Attribute '{name}' not found"
    
    def __setattr__(self, name, value):
        """Called when setting attribute"""
        self.__dict__[name] = value
    
    def __delattr__(self, name):
        """Called when deleting attribute"""
        del self.__dict__[name]


# Demo - Magic Methods
obj1 = CompleteExample(10)
obj2 = CompleteExample(5)

print(obj1)              # __str__
print(repr(obj1))        # __repr__
print(obj1 == obj2)      # __eq__
print(obj1 > obj2)       # __gt__
print(obj1 + obj2)       # __add__
print(-obj1)             # __neg__
print(len(obj1))         # __len__
print(obj1[0])           # __getitem__
print('1' in obj1)       # __contains__
print(obj1())            # __call__


# ============================================================================
# 6. DESIGN PATTERNS IN OOP
# ============================================================================

# -----------------------------
# 6.1 Singleton Pattern
# -----------------------------

"""
SINGLETON: Ensure a class has only one instance.
Useful for: Database connections, configuration managers, loggers
"""

class Logger:
    """Singleton Logger class"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance
    
    def log(self, message):
        self.logs.append(message)
        print(f"[LOG] {message}")
    
    def get_logs(self):
        return self.logs


# Demo
logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

print(logger1 is logger2)  # True - same instance
print(logger1.get_logs())  # Both messages in same logger


# -----------------------------
# 6.2 Factory Pattern
# -----------------------------

"""
FACTORY: Create objects without specifying exact class.
Useful for: Creating different types of objects based on conditions
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"


class AnimalFactory:
    """Factory to create animals"""
    
    @staticmethod
    def create_animal(animal_type):
        """Create animal based on type"""
        animals = {
            'dog': Dog,
            'cat': Cat,
            'cow': Cow
        }
        
        animal_class = animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Demo
factory = AnimalFactory()

dog = factory.create_animal('dog')
cat = factory.create_animal('cat')
cow = factory.create_animal('cow')

print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
print(cow.speak())  # Moo!


# -----------------------------
# 6.3 Observer Pattern
# -----------------------------

"""
OBSERVER: Define one-to-many dependency. When one object changes state,
all dependents are notified.
Useful for: Event systems, notifications, UI updates
"""

class Subject:
    """Subject that observers watch"""
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """Add observer"""
        self._observers.append(observer)
    
    def detach(self, observer):
        """Remove observer"""
        self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        """Change state and notify observers"""
        self._state = state
        self.notify()
    
    def get_state(self):
        return self._state


class Observer:
    """Base observer class"""
    def update(self, subject):
        pass


class EmailObserver(Observer):
    """Sends email when subject changes"""
    def update(self, subject):
        print(f"📧 Email: State changed to {subject.get_state()}")


class SMSObserver(Observer):
    """Sends SMS when subject changes"""
    def update(self, subject):
        print(f"📱 SMS: State changed to {subject.get_state()}")


class LogObserver(Observer):
    """Logs changes"""
    def update(self, subject):
        print(f"📝 Log: State changed to {subject.get_state()}")


# Demo
subject = Subject()

# Attach observers
email_obs = EmailObserver()
sms_obs = SMSObserver()
log_obs = LogObserver()

subject.attach(email_obs)
subject.attach(sms_obs)
subject.attach(log_obs)

# Change state - all observers notified!
subject.set_state("Order Placed")
subject.set_state("Order Shipped")


# -----------------------------
# 6.4 Strategy Pattern
# -----------------------------

"""
STRATEGY: Define family of algorithms, encapsulate each one,
and make them interchangeable.
Useful for: Different sorting algorithms, payment methods, compression
"""

class SortStrategy:
    """Base strategy"""
    def sort(self, data):
        pass


class BubbleSort(SortStrategy):
    """Bubble sort strategy"""
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)  # Simplified


class QuickSort(SortStrategy):
    """Quick sort strategy"""
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data)  # Simplified


class MergeSort(SortStrategy):
    """Merge sort strategy"""
    def sort(self, data):
        print("Sorting using Merge Sort")
        return sorted(data)  # Simplified


class DataSorter:
    """Context that uses strategy"""
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        """Change strategy at runtime"""
        self.strategy = strategy
    
    def sort(self, data):
        """Sort using current strategy"""
        return self.strategy.sort(data)


# Demo
data = [5, 2, 8, 1, 9]

sorter = DataSorter(BubbleSort())
print(sorter.sort(data))

# Change strategy at runtime
sorter.set_strategy(QuickSort())
print(sorter.sort(data))

sorter.set_strategy(MergeSort())
print(sorter.sort(data))


# ============================================================================
# 7. BEST PRACTICES & PRINCIPLES
# ============================================================================

"""
SOLID PRINCIPLES:
-----------------

S - Single Responsibility Principle
    A class should have only one reason to change

O - Open/Closed Principle
    Open for extension, closed for modification

L - Liskov Substitution Principle
    Derived classes must be substitutable for base classes

I - Interface Segregation Principle
    Many specific interfaces better than one general interface

D - Dependency Inversion Principle
    Depend on abstractions, not concretions
"""

# -----------------------------
# Single Responsibility Principle (SRP)
# -----------------------------

# ❌ Bad: Class has multiple responsibilities
class UserBad:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        # Database logic
        pass
    
    def send_email(self):
        # Email logic
        pass
    
    def generate_report(self):
        # Report logic
        pass


# ✓ Good: Each class has single responsibility
class User:
    def __init__(self, name):
        self.name = name


class UserRepository:
    def save(self, user):
        # Database logic
        pass


class EmailService:
    def send_email(self, user):
        # Email logic
        pass


class ReportGenerator:
    def generate(self, user):
        # Report logic
        pass


# -----------------------------
# Open/Closed Principle (OCP)
# -----------------------------

# ✓ Good: Open for extension, closed for modification
class Discount(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass


class NoDiscount(Discount):
    def calculate(self, amount):
        return amount


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage
    
    def calculate(self, amount):
        return amount * (1 - self.percentage / 100)


class FixedDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount
    
    def calculate(self, amount):
        return max(0, amount - self.discount_amount)


# Now you can add new discount types without modifying existing code


# -----------------------------
# Liskov Substitution Principle (LSP)
# -----------------------------

# ✓ Good: Derived class can replace base class
class Bird:
    def move(self):
        return "Moving"


class FlyingBird(Bird):
    def move(self):
        return "Flying"


class Penguin(Bird):
    def move(self):
        return "Swimming"


def make_bird_move(bird: Bird):
    """Works with any Bird subclass"""
    print(bird.move())


# All work correctly
make_bird_move(FlyingBird())
make_bird_move(Penguin())


# ============================================================================
# 8. REAL-WORLD EXAMPLES
# ============================================================================

# -----------------------------
# 8.1 E-Commerce System
# -----------------------------

class Product:
    """Product in e-commerce system"""
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self, quantity=1):
        return self.stock >= quantity
    
    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False


class ShoppingCart:
    """Shopping cart"""
    def __init__(self):
        self.items = {}  # {product_id: (product, quantity)}
    
    def add_item(self, product, quantity=1):
        if product.is_available(quantity):
            if product.product_id in self.items:
                _, current_qty = self.items[product.product_id]
                self.items[product.product_id] = (product, current_qty + quantity)
            else:
                self.items[product.product_id] = (product, quantity)
            return True
        return False
    
    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
    
    def get_total(self):
        total = 0
        for product, quantity in self.items.values():
            total += product.price * quantity
        return total
    
    def get_items(self):
        return list(self.items.values())


class Order:
    """Order"""
    order_counter = 1000
    
    def __init__(self, customer, cart):
        Order.order_counter += 1
        self.order_id = Order.order_counter
        self.customer = customer
        self.items = cart.get_items()
        self.total = cart.get_total()
        self.status = "Pending"
    
    def confirm(self):
        # Reduce stock for all items
        for product, quantity in self.items:
            product.reduce_stock(quantity)
        self.status = "Confirmed"
    
    def ship(self):
        if self.status == "Confirmed":
            self.status = "Shipped"
    
    def deliver(self):
        if self.status == "Shipped":
            self.status = "Delivered"


class Customer:
    """Customer"""
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = []
    
    def place_order(self, cart):
        order = Order(self, cart)
        self.orders.append(order)
        return order


# Demo - E-Commerce System
laptop = Product(1, "Laptop", 999.99, 10)
mouse = Product(2, "Mouse", 29.99, 50)
keyboard = Product(3, "Keyboard", 79.99, 30)

customer = Customer(1, "John Doe", "john@example.com")

cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)

print(f"Cart Total: ${cart.get_total():.2f}")

order = customer.place_order(cart)
order.confirm()
order.ship()
order.deliver()

print(f"Order #{order.order_id} Status: {order.status}")


# -----------------------------
# 8.2 Social Media System
# -----------------------------

class Post:
    """Social media post"""
    post_counter = 0
    
    def __init__(self, author, content):
        Post.post_counter += 1
        self.post_id = Post.post_counter
        self.author = author
        self.content = content
        self.likes = set()
        self.comments = []
        from datetime import datetime
        self.created_at = datetime.now()
    
    def like(self, user):
        self.likes.add(user)
    
    def unlike(self, user):
        self.likes.discard(user)
    
    def add_comment(self, comment):
        self.comments.append(comment)
    
    def get_like_count(self):
        return len(self.likes)


class Comment:
    """Comment on a post"""
    def __init__(self, author, content):
        self.author = author
        self.content = content
        from datetime import datetime
        self.created_at = datetime.now()


class SocialUser:
    """Social media user"""
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
        self.followers = set()
        self.following = set()
    
    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post
    
    def follow(self, other_user):
        self.following.add(other_user)
        other_user.followers.add(self)
    
    def unfollow(self, other_user):
        self.following.discard(other_user)
        other_user.followers.discard(self)
    
    def get_feed(self):
        """Get posts from users I follow"""
        feed = []
        for user in self.following:
            feed.extend(user.posts)
        return sorted(feed, key=lambda p: p.created_at, reverse=True)


# Demo - Social Media
alice = SocialUser("alice", "alice@example.com")
bob = SocialUser("bob", "bob@example.com")
charlie = SocialUser("charlie", "charlie@example.com")

# Alice follows Bob
alice.follow(bob)

# Bob creates post
post = bob.create_post("Hello World! This is my first post!")

# Alice likes and comments
post.like(alice)
post.add_comment(Comment(alice, "Great post!"))

print(f"Post has {post.get_like_count()} likes")
print(f"Bob has {len(bob.followers)} followers")


# ============================================================================
# 9. COMMON MISTAKES & ANTI-PATTERNS TO AVOID
# ============================================================================

"""
COMMON MISTAKES:
1. God Objects - Classes that do too much
2. Tight Coupling - Classes too dependent on each other
3. Not using inheritance/composition appropriately
4. Overusing inheritance (deep inheritance hierarchies)
5. Mutable default arguments
6. Not using @property for computed attributes
7. Mixing class and instance variables incorrectly
"""

# ❌ Mistake: Mutable default argument
class TeamBad:
    def __init__(self, members=[]):  # ❌ DON'T DO THIS!
        self.members = members


# ✓ Correct way
class TeamGood:
    def __init__(self, members=None):
        self.members = members if members is not None else []


# ============================================================================
# 10. TESTING OOP CODE
# ============================================================================

"""
TESTING: Always write tests for your classes!
"""

class Calculator:
    """Simple calculator for testing example"""
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# Test cases (using unittest framework)
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Run before each test"""
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


# Run tests: python -m unittest this_file.py


# ============================================================================
# END OF OOP DEEP DIVE
# ============================================================================

"""
SUMMARY:
--------
1. OOP organizes code into objects with data and behavior
2. Four pillars: Encapsulation, Inheritance, Polymorphism, Abstraction
3. Use composition over inheritance when possible
4. Follow SOLID principles for better design
5. Use magic methods to create pythonic classes
6. Apply design patterns for common problems
7. Write tests for your classes
8. Keep classes focused and simple (Single Responsibility)
9. Use properties for computed attributes and validation
10. Document your code with docstrings

RESOURCES FOR FURTHER LEARNING:
-------------------------------
- "Design Patterns" by Gang of Four
- "Clean Code" by Robert C. Martin
- "Python Cookbook" by David Beazley
- Real Python tutorials on OOP
- Python's official documentation on classes

Remember: OOP is a tool, not a religion. Use it when it makes sense,
but don't force everything into classes if a simple function would work better!
"""


# ============================================================================
# BONUS: ADVANCED PATTERNS & TECHNIQUES
# ============================================================================

# -----------------------------
# Property Decorators - Advanced Usage
# -----------------------------

class Temperature:
    """Temperature class with validation and conversion"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit (computed property)"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin (computed property)"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Set temperature using Kelvin"""
        self.celsius = value - 273.15


# Demo
temp = Temperature()
temp.celsius = 25
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
print(f"Kelvin: {temp.kelvin}")

temp.fahrenheit = 98.6  # Set using Fahrenheit
print(f"New Celsius: {temp.celsius:.2f}")


# -----------------------------
# Slots - Memory Optimization
# -----------------------------

"""
__slots__: Restrict attributes and save memory.
Useful when creating millions of objects.
"""

class PointWithoutSlots:
    """Regular class - uses __dict__"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointWithSlots:
    """Using __slots__ - more memory efficient"""
    __slots__ = ['x', 'y']  # Only these attributes allowed
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Demo
import sys

p1 = PointWithoutSlots(1, 2)
p2 = PointWithSlots(1, 2)

print(f"Without slots: {sys.getsizeof(p1.__dict__)} bytes")
print(f"With slots: {sys.getsizeof(p2)} bytes")

# With slots, you can't add new attributes dynamically
# p2.z = 3  # ❌ AttributeError!


# -----------------------------
# Data Classes (Python 3.7+)
# -----------------------------

"""
@dataclass: Automatically generate __init__, __repr__, __eq__, etc.
Great for classes that mainly store data.
"""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    """Person data class"""
    name: str
    age: int
    email: str
    hobbies: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Called after __init__"""
        if self.age < 0:
            raise ValueError("Age cannot be negative")


# Demo
person = Person("Alice", 30, "alice@example.com", ["reading", "coding"])
print(person)  # Automatic __repr__

person2 = Person("Alice", 30, "alice@example.com", ["reading", "coding"])
print(person == person2)  # Automatic __eq__


@dataclass(frozen=True)  # Immutable
class ImmutablePoint:
    """Immutable point"""
    x: float
    y: float


# point = ImmutablePoint(1, 2)
# point.x = 5  # ❌ FrozenInstanceError!


@dataclass(order=True)  # Adds comparison methods
class Student:
    """Student with automatic ordering by grade"""
    name: str = field(compare=False)
    grade: float
    
    def __str__(self):
        return f"{self.name}: {self.grade}"


# Demo
students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("Charlie", 78)
]

print(sorted(students))  # Automatically sorted by grade!


# -----------------------------
# Enum Classes
# -----------------------------

"""
Enum: Create enumerated constants (better than string/int constants)
"""

from enum import Enum, auto

class Color(Enum):
    """Color enumeration"""
    RED = 1
    GREEN = 2
    BLUE = 3


class Status(Enum):
    """Status with auto-numbering"""
    PENDING = auto()
    PROCESSING = auto()
    COMPLETED = auto()
    FAILED = auto()


class Priority(Enum):
    """Priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    
    def __str__(self):
        return self.value


# Demo
print(Color.RED)           # Color.RED
print(Color.RED.value)     # 1
print(Status.PENDING)      # Status.PENDING
print(Priority.HIGH)       # high

# Type-safe comparisons
if Color.RED == Color.RED:
    print("Same color!")


# -----------------------------
# Named Tuples
# -----------------------------

"""
Named Tuples: Lightweight, immutable classes for storing data
"""

from collections import namedtuple

# Old way
Point = namedtuple('Point', ['x', 'y'])

# New way (Python 3.6+)
from typing import NamedTuple

class Point3D(NamedTuple):
    """3D Point using NamedTuple"""
    x: float
    y: float
    z: float
    
    def magnitude(self):
        """Calculate magnitude"""
        return (self.x**2 + self.y**2 + self.z**2)**0.5


# Demo
point = Point3D(3, 4, 5)
print(f"Point: {point}")
print(f"Magnitude: {point.magnitude():.2f}")

# Immutable
# point.x = 10  # ❌ AttributeError!

# Can unpack
x, y, z = point
print(f"x={x}, y={y}, z={z}")


# -----------------------------
# Multiple Dispatch (Simulated)
# -----------------------------

"""
Multiple Dispatch: Different behavior based on argument types
Python doesn't natively support this, but we can simulate it.
"""

from functools import singledispatch

@singledispatch
def process(arg):
    """Generic processor"""
    print(f"Processing {type(arg).__name__}: {arg}")

@process.register(int)
def _(arg):
    """Process integer"""
    print(f"Processing integer: {arg * 2}")

@process.register(str)
def _(arg):
    """Process string"""
    print(f"Processing string: {arg.upper()}")

@process.register(list)
def _(arg):
    """Process list"""
    print(f"Processing list of {len(arg)} items")


# Demo
process(42)           # Processing integer: 84
process("hello")      # Processing string: HELLO
process([1, 2, 3])    # Processing list of 3 items
process(3.14)         # Processing float: 3.14 (generic)


# -----------------------------
# Proxy Pattern
# -----------------------------

"""
Proxy: Control access to another object
Useful for: Lazy loading, access control, logging
"""

class ExpensiveObject:
    """Object that's expensive to create"""
    def __init__(self):
        print("Creating expensive object...")
        import time
        time.sleep(1)  # Simulate expensive operation
        self.data = "Important data"
    
    def process(self):
        return f"Processing: {self.data}"


class LazyProxy:
    """Proxy that creates object only when needed"""
    def __init__(self):
        self._object = None
    
    def process(self):
        if self._object is None:
            print("Lazy loading...")
            self._object = ExpensiveObject()
        return self._object.process()


# Demo
print("Creating proxy (fast)...")
proxy = LazyProxy()

print("\nFirst access (slow - creates object)...")
print(proxy.process())

print("\nSecond access (fast - object already exists)...")
print(proxy.process())


# -----------------------------
# Builder Pattern
# -----------------------------

"""
Builder: Construct complex objects step by step
Useful for: Objects with many optional parameters
"""

class Pizza:
    """Pizza product"""
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.cheese = None
    
    def __str__(self):
        return (f"{self.size} pizza with {self.crust} crust, "
                f"{self.cheese} cheese, toppings: {', '.join(self.toppings)}")


class PizzaBuilder:
    """Builder for Pizza"""
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self  # Return self for method chaining
    
    def set_crust(self, crust):
        self.pizza.crust = crust
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self
    
    def build(self):
        """Return the built pizza"""
        return self.pizza


# Demo - Method chaining
pizza = (PizzaBuilder()
         .set_size("Large")
         .set_crust("Thin")
         .set_cheese("Mozzarella")
         .add_topping("Pepperoni")
         .add_topping("Mushrooms")
         .add_topping("Olives")
         .build())

print(pizza)


# -----------------------------
# Decorator Pattern (not to confuse with @decorators)
# -----------------------------

"""
Decorator Pattern: Add functionality to objects dynamically
"""

class Coffee:
    """Base coffee"""
    def cost(self):
        return 2.0
    
    def description(self):
        return "Coffee"


class CoffeeDecorator(Coffee):
    """Base decorator"""
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()


class Milk(CoffeeDecorator):
    """Add milk"""
    def cost(self):
        return self._coffee.cost() + 0.5
    
    def description(self):
        return self._coffee.description() + ", Milk"


class Sugar(CoffeeDecorator):
    """Add sugar"""
    def cost(self):
        return self._coffee.cost() + 0.2
    
    def description(self):
        return self._coffee.description() + ", Sugar"


class WhippedCream(CoffeeDecorator):
    """Add whipped cream"""
    def cost(self):
        return self._coffee.cost() + 0.7
    
    def description(self):
        return self._coffee.description() + ", Whipped Cream"


# Demo - Build coffee with decorators
coffee = Coffee()
print(f"{coffee.description()}: ${coffee.cost()}")

coffee_with_milk = Milk(coffee)
print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")

fancy_coffee = WhippedCream(Sugar(Milk(Coffee())))
print(f"{fancy_coffee.description()}: ${fancy_coffee.cost()}")


# -----------------------------
# Chain of Responsibility Pattern
# -----------------------------

"""
Chain of Responsibility: Pass request along chain of handlers
"""

class Handler:
    """Base handler"""
    def __init__(self):
        self._next = None
    
    def set_next(self, handler):
        self._next = handler
        return handler
    
    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        return None


class AuthenticationHandler(Handler):
    """Check authentication"""
    def handle(self, request):
        if not request.get('authenticated'):
            return "Authentication required!"
        print("✓ Authentication passed")
        return super().handle(request)


class AuthorizationHandler(Handler):
    """Check authorization"""
    def handle(self, request):
        if request.get('role') != 'admin':
            return "Insufficient permissions!"
        print("✓ Authorization passed")
        return super().handle(request)


class ValidationHandler(Handler):
    """Validate data"""
    def handle(self, request):
        if not request.get('data'):
            return "Data validation failed!"
        print("✓ Validation passed")
        return super().handle(request)


class ProcessHandler(Handler):
    """Process the request"""
    def handle(self, request):
        print("✓ Request processed successfully")
        return "Success!"


# Demo - Chain handlers
auth = AuthenticationHandler()
authz = AuthorizationHandler()
valid = ValidationHandler()
process = ProcessHandler()

# Build chain
auth.set_next(authz).set_next(valid).set_next(process)

# Test requests
request1 = {
    'authenticated': True,
    'role': 'admin',
    'data': {'name': 'John'}
}

print("\nProcessing valid request:")
result = auth.handle(request1)
print(f"Result: {result}")

print("\nProcessing invalid request:")
request2 = {'authenticated': True, 'role': 'user'}
result = auth.handle(request2)
print(f"Result: {result}")


# ============================================================================
# PERFORMANCE OPTIMIZATION TIPS
# ============================================================================

"""
OPTIMIZATION TIPS:
------------------
1. Use __slots__ for classes with many instances
2. Use @property for computed attributes (lazy evaluation)
3. Cache expensive computations
4. Use generators for large data sets
5. Profile before optimizing!
"""

from functools import lru_cache

class FibonacciCalculator:
    """Fibonacci with caching"""
    
    @staticmethod
    @lru_cache(maxsize=None)  # Cache all results
    def calculate(n):
        """Calculate nth Fibonacci number"""
        if n < 2:
            return n
        return (FibonacciCalculator.calculate(n-1) + 
                FibonacciCalculator.calculate(n-2))


# Demo
import time

start = time.time()
result = FibonacciCalculator.calculate(35)
end = time.time()
print(f"Fibonacci(35) = {result}, Time: {end-start:.4f}s")

# Second call is instant (cached)
start = time.time()
result = FibonacciCalculator.calculate(35)
end = time.time()
print(f"Fibonacci(35) = {result}, Time: {end-start:.4f}s (cached)")


# -----------------------------
# Lazy Properties
# -----------------------------

class LazyProperty:
    """Descriptor for lazy property evaluation"""
    def __init__(self, func):
        self.func = func
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.func.__name__, value)
        return value


class DataAnalyzer:
    """Analyzer with lazy properties"""
    def __init__(self, data):
        self.data = data
    
    @LazyProperty
    def mean(self):
        """Calculate mean (only once)"""
        print("Calculating mean...")
        return sum(self.data) / len(self.data)
    
    @LazyProperty
    def variance(self):
        """Calculate variance (only once)"""
        print("Calculating variance...")
        mean = self.mean
        return sum((x - mean)**2 for x in self.data) / len(self.data)


# Demo
analyzer = DataAnalyzer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("First access to mean:")
print(analyzer.mean)  # Calculates

print("\nSecond access to mean:")
print(analyzer.mean)  # Uses cached value

print("\nFirst access to variance:")
print(analyzer.variance)  # Calculates


# ============================================================================
# REAL-WORLD SYSTEM: LIBRARY MANAGEMENT SYSTEM
# ============================================================================

"""
Complete Library Management System demonstrating all OOP concepts
"""

from datetime import datetime, timedelta
from enum import Enum

class BookStatus(Enum):
    """Book availability status"""
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"
    RESERVED = "reserved"
    MAINTENANCE = "maintenance"


class Book:
    """Book in library"""
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.status = BookStatus.AVAILABLE
        self.current_borrower = None
        self.due_date = None
    
    def is_available(self):
        return self.status == BookStatus.AVAILABLE
    
    def checkout(self, member, days=14):
        """Check out book to member"""
        if not self.is_available():
            raise ValueError("Book is not available")
        
        self.status = BookStatus.CHECKED_OUT
        self.current_borrower = member
        self.due_date = datetime.now() + timedelta(days=days)
        return self.due_date
    
    def return_book(self):
        """Return book to library"""
        if self.status != BookStatus.CHECKED_OUT:
            raise ValueError("Book is not checked out")
        
        self.status = BookStatus.AVAILABLE
        self.current_borrower = None
        self.due_date = None
    
    def is_overdue(self):
        """Check if book is overdue"""
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class Member:
    """Library member"""
    member_counter = 1000
    
    def __init__(self, name, email):
        Member.member_counter += 1
        self.member_id = Member.member_counter
        self.name = name
        self.email = email
        self.borrowed_books = []
        self.fines = 0.0
    
    def can_borrow(self, max_books=5):
        """Check if member can borrow more books"""
        return len(self.borrowed_books) < max_books and self.fines == 0
    
    def borrow_book(self, book):
        """Borrow a book"""
        if not self.can_borrow():
            raise ValueError("Cannot borrow more books")
        
        book.checkout(self)
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        """Return a book"""
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by this member")
        
        # Calculate fine if overdue
        if book.is_overdue():
            days_overdue = (datetime.now() - book.due_date).days
            fine = days_overdue * 1.0  # $1 per day
            self.fines += fine
            print(f"Fine applied: ${fine:.2f}")
        
        book.return_book()
        self.borrowed_books.remove(book)
    
    def pay_fine(self, amount):
        """Pay outstanding fines"""
        self.fines = max(0, self.fines - amount)
    
    def __str__(self):
        return f"Member #{self.member_id}: {self.name}"


class Library:
    """Library management system"""
    def __init__(self, name):
        self.name = name
        self.books = {}  # isbn -> Book
        self.members = {}  # member_id -> Member
    
    def add_book(self, book):
        """Add book to library"""
        self.books[book.isbn] = book
    
    def remove_book(self, isbn):
        """Remove book from library"""
        if isbn in self.books:
            del self.books[isbn]
    
    def register_member(self, member):
        """Register new member"""
        self.members[member.member_id] = member
    
    def find_book_by_isbn(self, isbn):
        """Find book by ISBN"""
        return self.books.get(isbn)
    
    def find_books_by_author(self, author):
        """Find all books by author"""
        return [book for book in self.books.values() 
                if author.lower() in book.author.lower()]
    
    def find_books_by_title(self, title):
        """Find books by title (partial match)"""
        return [book for book in self.books.values() 
                if title.lower() in book.title.lower()]
    
    def get_available_books(self):
        """Get all available books"""
        return [book for book in self.books.values() if book.is_available()]
    
    def get_overdue_books(self):
        """Get all overdue books"""
        return [book for book in self.books.values() if book.is_overdue()]
    
    def generate_report(self):
        """Generate library statistics"""
        total_books = len(self.books)
        available = len(self.get_available_books())
        checked_out = sum(1 for b in self.books.values() 
                         if b.status == BookStatus.CHECKED_OUT)
        overdue = len(self.get_overdue_books())
        
        return {
            'total_books': total_books,
            'available': available,
            'checked_out': checked_out,
            'overdue': overdue,
            'total_members': len(self.members)
        }


# Demo - Library Management System
print("\n" + "="*60)
print("LIBRARY MANAGEMENT SYSTEM DEMO")
print("="*60)

# Create library
library = Library("City Central Library")

# Add books
book1 = Book("978-0-123456-47-2", "Python Programming", "John Smith", 2020)
book2 = Book("978-0-123456-48-9", "Data Structures", "Jane Doe", 2019)
book3 = Book("978-0-123456-49-6", "Algorithms", "Bob Johnson", 2021)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register members
member1 = Member("Alice Cooper", "alice@example.com")
member2 = Member("Bob Dylan", "bob@example.com")

library.register_member(member1)
library.register_member(member2)

# Member borrows book
print(f"\n{member1.name} borrowing '{book1.title}'...")
member1.borrow_book(book1)
print(f"Due date: {book1.due_date.strftime('%Y-%m-%d')}")

# Search books
print("\nSearching for 'Python' books:")
results = library.find_books_by_title("Python")
for book in results:
    print(f"  - {book}")

# Generate report
print("\nLibrary Report:")
report = library.generate_report()
for key, value in report.items():
    print(f"  {key}: {value}")


# ============================================================================
# FINAL NOTES AND BEST PRACTICES
# ============================================================================

"""
KEY TAKEAWAYS:
--------------

1. START SIMPLE: Don't over-engineer. Use simple classes first.

2. COMPOSITION > INHERITANCE: Prefer composition when possible.

3. SOLID PRINCIPLES: Follow them for maintainable code.

4. SINGLE RESPONSIBILITY: Each class should do ONE thing well.

5. DRY (Don't Repeat Yourself): Reuse code through inheritance/composition.

6. DOCUMENTATION: Always write docstrings.

7. TYPE HINTS: Use them for better code clarity (Python 3.5+).

8. TESTING: Write tests for your classes.

9. KEEP IT PYTHONIC: 
   - Use properties instead of getters/setters
   - Use magic methods for operator overloading
   - Use list comprehensions where appropriate
   - Follow PEP 8 style guide

10. PROFILE BEFORE OPTIMIZING: Don't optimize prematurely.

WHEN TO USE OOP:
----------------
✓ When modeling real-world entities
✓ When you need encapsulation and data hiding
✓ When you want code reusability
✓ For large, complex systems
✓ When working in teams (better code organization)

WHEN NOT TO USE OOP:
--------------------
✗ For simple scripts or one-off tasks
✗ When functional programming is more natural
✗ When performance is critical and OOP adds overhead
✗ For very small programs

Remember: OOP is a tool in your toolbox. Use it wisely!
"""