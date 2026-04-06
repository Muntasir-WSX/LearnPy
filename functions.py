from os import name


def greet(name, age):
    print(f"Hello,{name} you are {age} years old")

# greet("Alice", 30)

counter = 0
while counter< 10:
    greet("Alice", 30)
    counter += 1