class decorated_class(object):
    #self for instance
    def __init__(self,original_function):
        self.original_function=original_function
    def __call__(self,*args,**kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorated_class
def display():
    print('display function ran')

display()