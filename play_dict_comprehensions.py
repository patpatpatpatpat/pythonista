# Let's play with Python Dictionary Comprehensions!
# Links:
# 1. https://docs.python.org/2/tutorial/datastructures.html#dictionaries

# Simple examples
root_and_square = {
    x : x**2
    for x in range(5)
}
print root_and_square

even_root_and_square = {
    x : x**2
    for x in range(5)
    if x % 2 == 0
}
print even_root_and_square

my_names = ['Ed', 'Patrick', 'Tan']

# Method calls in key/val
lower_and_upper = {
    name.lower(): name.upper()
    for name in my_names
}
print lower_and_upper
