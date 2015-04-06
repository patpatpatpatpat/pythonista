# Let's play with Python decorators!
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
