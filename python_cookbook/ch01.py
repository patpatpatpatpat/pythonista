"""
Chapter 1

1. Use Python "star expressions" to unpack elements from iterables of arbitrary length.
2. Use `collections.deque` to store the last few items during iteration or during some processing.
3. Use `heapq` to get the list of largest or smallest N items in a collection
4. Use `collections.defaultdict` and initialize the first value so you can focus on adding items.
5. Use `collections.OrderedDict` when creating a dictionary where you can control the order of items when iterating
6. Use `zip` to group items together
7. You can use `key` argument when using `min` and `max` functions
8. Use set operations to find out what two dicts (keys or values) have in common: &, -
9. Use `set` and generators to remove duplicates from a sequence while maintaining order
10. Use `slice` class to avoid mysterious hardcoded indices
11. Use `collections.Counter` class when determining most frequently occuring items in a sequence. You can also use mathematical operations in instances of them
12. Use `operator.itemgetter` to sort list of dicts based on one or more of the dict values.
    `lambda` expressions can be used too, though (but the former is faster).
13. Use `operator.attrgetter` to sort objects of the same class, but don't natively support comparison operations.
14. Use `itertools.groupby` (after sorting the data according to the field of interest) to
    iterate over data in groups
15. Use list comprehensions or `filter` when you need to extract values or reduce the sequence
    using some criteria.
    You can also transform the data at the same time!
    Example: you can replace the values that don't meet the criteria with a new value instead
    of discarding them.
    Also: look into `itertools.compress`
16. Use dictionary comprehensions when creating a dictionary that is a subset of another dict.
17. `collections.namedtuple` to improve readability when accessing list or tuple elements by
    position! However, they are immutable.
18. Use `collections.ChainMap` to perform lookups under multiple dictionaries (without merging them)
"""
