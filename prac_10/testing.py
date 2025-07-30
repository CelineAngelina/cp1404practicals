"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly

    car = Car(fuel=10)
    assert car.fuel == 10

    default_car = Car()
    assert default_car.fuel == 0

run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (Don't change the tests, change the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
#   'hello' -> 'Hello.'
#   'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more that you decide is a useful test.
# Run your doctests and watch the tests fail.
# Then write the body of the function so that the tests pass.

def change_format(sentence):
    """
    Changing the format of sentence input to start with capital and ends with full stop
    >>> change_format("hello")
    'Hello.'
    >>> change_format("It is an ex parrot.")
    'It is an ex parrot.'
    >>> change_format("welcome to CP1404")
    'Welcome to CP1404.'
    """
    sentence = sentence.strip()
    sentence = sentence[0].upper() + sentence[1:]
    if not sentence.endswith("."):
        sentence += "."
    return sentence