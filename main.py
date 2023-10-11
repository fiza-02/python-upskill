"""
print("Hello CodeSandbox!")

def outer_function():
    message= "hi" #free variable

    def inner_function():
        print(message)
    return inner_function
my_func=outer_function()
my_func()
my_func()

"""


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')
# display= decorator_function(display)
display()
#this is a decorator.



# my_s=decorator_function("kiko")
# my_s()