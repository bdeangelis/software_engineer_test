#!/usr/bin/python
__author__ = 'brettdeangelis'

# accepts the decorator variable and returns decorator
def minimum_x(x):
    '''
    - returns a decorator that can be used to decorate another function
    - verifies argument of the function it decorates <= the given value
    - raises a ValueError on failure.
    '''
    # passes in the function to be decorated returns outer function
    def outer(some_func):
        # passes function variable for comparison returns inner function
        def inner(val):
            #performs comparison and runs decorated function or raises ValueError
            if not x <= val:
                raise ValueError("Function variable less than decorator variable")
            print val
        return inner
    return outer


