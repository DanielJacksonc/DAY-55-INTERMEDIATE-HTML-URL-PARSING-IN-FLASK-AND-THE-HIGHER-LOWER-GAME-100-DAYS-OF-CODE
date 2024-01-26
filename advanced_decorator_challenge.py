# Challenge: Create a logging decorator() which is going to print the name of fuction that was called,
# the argument it was given and finally the returned output
# Example you called a function(1,2,3), it returned : 6

inputs = eval(input(" Input here : "))
# todo: Create the logging decorator() function


def logging_decorator(function):
    def wrapper(*args):
        print (f"You called {function.__name__}{args} ")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


# use the decorator
@logging_decorator
def a_function(a,b,c):
    return a * b * c
a_function(inputs[0], inputs[1],inputs[2] )