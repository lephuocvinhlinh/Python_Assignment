def login_required(func):
    def wrapper():
        # Provide 3 chances to login
        for i in range(3):
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == "KNN" and password == "1710":
                print("Login is successful!")
                # Call the decorated function
                return func()
            else:
                print("Invalid login. Please try again.")
        print("You have exceeded the maximum number of login attempts.")
    return wrapper

@login_required
def my_function():
    print("Access granted!")

my_function()
print(end = '\n')

# Evaluate the execution time of a function
import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time: .6f} seconds")
        return result
    return wrapper

@execution_time
def my_function():
    pass
my_function()
print(end = '\n')

# A chain of function decorators 
def bold(func):
    def wrapper():
        #return "<b>" + func() + "</b>"
        return f"\033[1m{func()}\033[0m"
    return wrapper

def italic(func):
    def wrapper():
        #return "<i>" + func() + "</i>"
        return f"\033[3m{func()}\033[0m"
    return wrapper

def underline(func):
    def wrapper():
        #return "<u>" + func() + "</u>"
        return f"\033[4m{func()}\033[0m"
    return wrapper

@bold
@italic
@underline

#def format_text(text):
#    return text
#print(format_text("Hello World!"))

def format_text():
    return "Hello World"
print(format_text())
print(end = '\n')

# Write decor1 and decor2
def decor1(func):
    def wrapper():
        return func() ** 2
    return wrapper

def decor2(func):
    def wrapper():
        return func() * 2
    return wrapper

@decor1
@decor2
def num_a():
    return 10

@decor2
@decor1
def num_b():
    return 10

print(num_a())  
print(num_b())  
