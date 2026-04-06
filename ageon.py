from os import name


def greet(name, age):
    print(f"Hello,{name} you are {age} years old")
    
    greet(name="Paulo", age = 42)
counter = 0
while counter< 10:
    greet("Alice", 42)
    counter += 1