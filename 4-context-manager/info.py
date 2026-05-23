# if you noticed how we open file in python with "with" statement

with open("xyz.txt", 'w') as file:
    file.write("Jai shree Ram")

# this is context manager 

"""
A Context Manager is a brilliant Python feature designed to handle the setup and teardown of resources automatically.


1. How to Explain It (The Analogy)

Imagine you go into a secure server room at work. To do your job safely, you must follow a 

strict routine:
Setup: Unlock the heavy door and turn on the lights.
Work: Do your actual job (e.g., swapping a hard drive).
Teardown: Turn off the lights and lock the door behind you.

If you get distracted or an emergency happens halfway through, you might forget step 3, leaving the server room wide open.


In Python, a Context Manager is the automated security guard that stands at the door. It ensures that no matter what happens while you are working—even if your code crashes or encounters an error—the door always gets locked when you leave.

In code, this behavior is triggered using the with statement.
"""


# we can even buit our own context manager, lets built the file opening and closing context manager