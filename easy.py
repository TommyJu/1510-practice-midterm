"""
Define a function called count_evens.

The count_evens function accepts a non-empty list of integers called readings.

The count_evens function must return a tuple that contains two integers.
The first value in the tuple must be the number of even integers in the list called readings.
The second value must be the sum of the even integers in the list called readings.

You may not modify the list passed as an argument in any way, even temporarily, if you do you
will earn zero marks for this question.

You must provide a full docstring for this function including all pre- and post-conditions.
You must create two useful and different doctests for this function.
No main function is required.
"""

"""
Tommy Ju
A01347715
Set F
"""


def count_evens(readings):
    """
    Count and add the number of even integers in a list

    :param readings: a list of integers
    :precondition: readings must be non-empty
    :postcondition: correctly identifies the even integers and their sum
    :return: a tuple representing the number of even integers, and the sum

    >>> count_evens([1, 2, 3, 4])
    (2, 6)
    >>> count_evens([0, 1, -1, 2])
    (2, 2)
    >>> count_evens([-2, 2, -2, 2])
    (4, 0)
    """

    even_integers = []
    for i in readings:
        # integer is even
        if i % 2 == 0:
            even_integers.append(i)
        # integer is odd
        else:
            continue

    return len(even_integers), sum(even_integers)
