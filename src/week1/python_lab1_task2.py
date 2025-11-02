"""
Task 2 🟡 Greeting Function with String Manipulation
----------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""

def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    # TODO: implement cleaning and formatting
    name_cleaned = name.strip().capitalize()
    message = f"Hi {name_cleaned}, nice to see you learning Python!"
    return message

if __name__ == "__main__":
    # TODO: read name from input and print greeting
    user = input("Type your name: ")
    print(greet_user(user))
