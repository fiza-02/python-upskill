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
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function #display= decorator_function(display)
def display():
    print('display function ran')
# display= decorator_function(display)
display()
#this is a decorator.

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

'''
    display_info("viswa",23)
TypeError: decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 2 were given
display_info("viswa",23)
'''
display_info("viswa",23)
'''
output:
wrapper executed this before display_info
display_info ran with arguments (viswa,23)
'''
# my_s=decorator_function("kiko")
# my_s()