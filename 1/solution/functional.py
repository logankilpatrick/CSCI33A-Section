import time

# Create a wrapper function that times another function
def timer(f):
    def wrapper():
        start = time.time()
        f()
        end = time.time()
        print(f"Finished running after {end - start} seconds.")
    return wrapper


# Create a lambda function that takes in a name and 
# returns a string greeting that name
greet = lambda name: f"Hello, {name}!"


# Functions for Testing:
@timer
def f1():
    total = 0
    for i in range(10 ** 6):
        total += i
    print(f"Total: {total}")

@timer
def f2():
    total = 0
    for i in range(10 ** 8):
        total += i
    print(f"Total: {total}")

# f1()
# f2()

print(greet("Connor"))

