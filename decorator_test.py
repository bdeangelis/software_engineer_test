#!/usr/bin/python
__author__ = 'brettdeangelis'
from decorator import minimum_x

'''A script to view the test examples for question 2'''


#set decorator variable
#function variable must equal or be greater than decorator variable

@minimum_x(6)
def foo(x):
    print x


if __name__ == '__main__':
    foo(6)
    #foo(5)
    #foo(7)
