"""
Tommy Ju
A01347715
"""
"""
(10) Using unittest, write the FIVE (5) most informative tests you can think of for a function 
called is_sorted in a module called TestSorting.py. The is_sorted function accepts a list 
of integers as input and returns True if the list is sorted in non-decreasing order, 
or False if it is not. Non-decreasing order means that each integer in the list is 
equal to or greater than the preceding integer in the list. 
You may use the next page if you run out of room.
"""


def is_sorted(list_of_integers):
    """
    Check if a list of integers is sorted by increasing order

    :param list_of_integers: A list containing integers
    :precondition: list_of_integers must be non-empty and contain only integers
    :postcondition: correctly determines if the integers are in increasing order
    :return: A boolean value, True represents a correctly sorted list of integers
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([1, 3, 2])
    False
    >>> is_sorted([1, 1, 1])
    True
    >>> is_sorted([2])
    True
    """
    if len(list_of_integers) < 2:
        return True

    previous_integer = list_of_integers[0]
    for integer in list_of_integers:
        if previous_integer <= integer:
            previous_integer = integer
        else:
            return False
    return True


def main():
    print(is_sorted([1, 2, 3, 4]))
    print(is_sorted([1, 2, 4, 3]))
    print(is_sorted([1, 2]))
    print(is_sorted([1]))


if __name__ == "__main__":
    main()
