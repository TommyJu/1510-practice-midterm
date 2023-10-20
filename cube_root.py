"""
(10) There is a simple algorithm that employs exhaustive enumeration to determine the integer cube root,
if it exists, of a positive integer. Starting with a value of 0, cube the value and test if it equal to
the positive integer. If it is less than the positive integer, we must increment value and try again. If
the cube of value is greater than the positive integer, we know there is no integer cube root and we can end.
If it is equal, we have found the cube root.
Implement a function called cube_root. This function accepts a positive integer.
This function is not required to work if the argument is not a positive integer (assume zero is positive).
Employ the algorithm I just described to determine the cube root of the argument.
If it exists, print it. If it doesn’t exist, print a message in the recommended format.
You may use the next page if you run out of room.
"""


def cube_root(number):
    number_cube_root = 0
    while number_cube_root ** 3 <= number:
        if number_cube_root ** 3 == number:
            return number_cube_root
        else:
            number_cube_root += 1
    return "No cube root bud"


def main():
    print(cube_root(27))
    print(cube_root(1000))
    print(cube_root(0))
    print(cube_root(5))


if __name__ == "__main__":
    main()
