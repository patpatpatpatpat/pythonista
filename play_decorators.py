# Let's play with Python decorators!
# Definition: a decorator is a function that modifies functions, methods or classes.
# Source
# 1. http://www.jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/


def surround_with(surrounding):
    """
    Return a function that takes a single argument and.
    """
    # Function nesting
    def surround_with_value(word):
        # Nested function has access to names in the scope.
        # e.g: This function has access to `surrounding` arg
        return '{}{}{}'.format(surrounding, word, surrounding)

    # Function that returns a function
    return surround_with_value


def transform_words(content, targets, transform):
    """
    Return a string based on *content* but with each occurence of words in
    *targets* replaced with the result of applying *transform* to it.
    """
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result


markdown_string = 'My name is Pat and I like Python but I do not own a Python'
target_strings = ['Python', 'Pat']
italic_indicator = '*'
markdown_string_italicized = transform_words(
    markdown_string,
    target_strings,
    surround_with(italic_indicator),
)

print 'Old string: %s' % markdown_string
print 'New string: %s' % markdown_string_italicized


# Source
# 1. http://www.brianholdefehr.com/decorators-and-functional-python


def logging_decorator(func):
    def wrapper():
        wrapper.count += 1
        print "The function I modify has been called {0} time(s)".format(
            wrapper.count)
        func()
    wrapper.count = 0
    return wrapper


def a_function():
    print "I'm a normal function."


modified_function = logging_decorator(a_function)
modified_function()
modified_function()


def some_function():
    print "Please decorate me!"

# Use the decorator function by passing the function we wanted to
# modify to it, and assigning the result to a variable
modified_function = logging_decorator(some_function)

# We can achieve the exact same thing with this syntax:
@logging_decorator
def some_function():
    print "Please decorate me!"



# Class decorators
foo = ['important', 'foo', 'stuff']

def add_foo(klass):
    klass.foo = foo
    return klass


@add_foo
class Person(object):
    pass

pat = Person()
print pat.foo


# A decorator can be a class
class IdentityDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print "I'm printed before calling the wrapped function!"
        self.func()


@IdentityDecorator
def a_function():
    print "I'm a normal function decorated by a decorator which is a class."

a_function()


# Decorators with arguments (required)
from functools import wraps
"""
A side effect of using decorators is that the function that gets wrapped
loses it’s natural __name__, __doc__, and __module__ attributes. The
wraps function is used as a decorator that wraps the function that
a decorator returns, restoring those three attributes to the values
they would have if the wrapped function was not decorated.
"""

def argumentative_decorator(gift):
    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(*args, **kwargs):
            print "I don't like this " + gift + " you gave me!"
            return func(gift , *args, **kwargs)
        return returned_wrapper
    return func_wrapper


@argumentative_decorator("sweater")
def grateful_function(gift):
    print "I love the " + gift + "! Thank you!"


grateful_function()

DEFAULT_NAME = 'Pat'


def print_name(function=None, name=DEFAULT_NAME):
    def actual_decorator(function):
        @wraps(function)
        def returned_func(*args, **kwargs):
            print "My name is " + name
            return function(*args, **kwargs)
        return returned_func

    if not function:  # User passed in a name argument
        def waiting_for_func(function):
            return actual_decorator(function)
        return waiting_for_func
    else:
        return actual_decorator(function)


@print_name
def a_function():
    print "I like the default name"

@print_name(name='Ed')
def another_function():
    print "Hey, new name!"

a_function()
another_function()
