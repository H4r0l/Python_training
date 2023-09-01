#Problem: Timing Decorator

#Create a timing decorator @timing that can be applied to functions to measure and print the time taken for the function to execute. Additionally, implement a function that accepts a list of functions and runs each function, applying the @timing decorator to them. This way, you can easily measure the execution time of multiple functions.
#

#"Your tasks:

#Implement the @timing decorator.
#Implement a function that accepts a list of functions and runs each function with the @timing decorator applied.
#


import time

def timmer_decorator(function):
    def wrapper(*args, **kwargs):
        print("Time starts")
        init_time = time.time()
        function(*args, **kwargs)
        print("Time ends")
        final_time = time.time() - init_time
        print(f'the function took {final_time} seconds')
    return wrapper

@timmer_decorator
def hello(sleep_time):
    time.sleep(sleep_time)
    print("Hello")

hello(2)