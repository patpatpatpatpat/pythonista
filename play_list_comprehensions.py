# Let's play with Python List comprehensions!
# A list comprehension consists of brackets containing an expression
# followed by a `for` clause, then zero or more `for` or `if` clauses.
# The result will be a new list resulting from evaluating the expression
# in the context of the `for` and `if` clauses which follow it.
# Links:
# 1. https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

# I want a list of squares!
squares = []
for x in range(10):
    squares.append(x**2)

print squares

# It's the same with:
squares = [x**2 for x in range(10)]
# This is also equivalent to squares = map(lambda x: x**2, range(10)),
# but it's more concise and readable


# This listcomp combines the elements of two lists
# if they are not equal
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# It's equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))


# Flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print [num for elem in vec for num in elem]
