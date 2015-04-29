# Since I'm also guilty of not remembering the syntax for writing decorators
# Source: http://www.pydanny.com/python-decorator-cheatsheet.html

# DECORATORS WITHOUT ARGUMENTSs
# These are decorators that do not accept arguments.
import functools  # Part of Python standard library

def decorator(wrapped_function):
    def _wrapper(*args, **kwargs):
        # do something before the function call
        result = wrapped_function(*args, **kwargs)
        # do something after the function call
        return result
    return _wrapper

# decorator with functools.wraps added
def decorator_with_wraps(wrapped_function):
    @functools.wraps(wrapped_function)
    def _wrapper(*args, **kwargs):
        # do something before the function call
        result = wrapped_function(*args, **kwargs)
        # do something after the function acll
        return result
    return _wrapper


import wrapt  # Requires installing the 'wrapt' library

# decorator powered by wrapt
@wrapt.decorator
def decorator_with_wrapt(wrapped_function, instance, args, kwargs):
    # do something before the function call
    result = wrapped_function(*args, **kwargs)
    # do something after the function call
    return result


def test_decorators():
    @decorator
    def func1():
        return 'I'

    @decorator_with_wraps
    def func2():
        return 'code'

    @decorator_with_wrapt
    def func3():
        return 'python'

    assert func1() == 'I'
    assert func2() == 'code'
    assert func3() == 'python'


# DECORATORS WITH ARGUMENTS
# These are decorators that accept arguments.
def arguments_decorator(arg1, arg2):
    def _outer_wrapper(wrapped_function):
        def _wrapper(*args, **kwargs):
            # do something before the function call
            result = wrapped_function(*args, **kwargs)
            # do something after the function call

            # Demonstrating what you can do with decorator arguments
            result = result * arg1 * arg2

            return result
        return _wrapper
    return _outer_wrapper


def arguments_decorator_with_wraps(arg1, arg2):
    def _outer_wrapper(wrapped_function):
        @functools.wraps(wrapped_function)
        def _wrapper(*args, **kwargs):
            # do something before the function call
            result = wrapped_function(*args, **kwargs)
            # do something after the function call

            # Demonstrating what you can do with decorator arguments
            result = result * arg1 * arg2

            return result
        return _wrapper
    return _outer_wrapper


def arguments_decorator_with_wrapt(arg1, arg2):
    @wrapt.decorator
    def _wrapper(wrapped_function, instance, args, kwargs):
        # do something before the function call
        result = wrapped_function(*args, **kwargs)
        # do something after the function call

        # Demonstrating what you can do with decorator arguments
        result = result * arg1 * arg2

        return result
    return _wrapper


def test_arguments_decorators():
    @arguments_decorator(2, 3)
    def func4():
        return 'We'

    @arguments_decorator_with_wraps(2, 2)
    def func5():
        return 'code'

    @arguments_decorator_with_wrapt(3, 2)
    def func6():
        return 'python'

    assert func4() == 'WeWeWeWeWeWe'
    assert func5() == 'codecodecodecode'
    assert func6() == 'pythonpythonpythonpythonpythonpython'
