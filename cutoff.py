"""
Tommy Ju
A01347715

(5) Implement a function called cutoff. This function accepts two parameters:
a list of integers, and another integer. The function should return a count of
the number of integers in the list that are a multiple of the given number.
Invoke this function from the main method with a set of arguments that will return
the value 3.
"""
def cutoff(list_of_integers, integer):
    """
    Count how many numbers in the list are multiples of a given number

    :param list_of_integers: a list of integers
    :param integer: an integer representing our given number
    :precondition: list_of_integers must be a non-empty list containing positive integers
    :precondition: integer must be an integer
    """
    count = 0

    if integer == 0:
        return count

    for element in list_of_integers:
        if abs(element) >= integer and element % integer == 0:
            count += 1
        else:
            continue
    return count

def main():
    print(cutoff([5, 10, 15], 5))
    print(cutoff([5, 10, 1], 5))
    print(cutoff([6, 0, 4], 0))
    print(cutoff([-5, -10, -1], 5))
    print(cutoff([5, 10, -15], -5))


if __name__ == "__main__":
    main()
