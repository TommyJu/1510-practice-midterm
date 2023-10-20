"""
5) Implement a function called prepender that accepts two parameters, a list of strings and another string.
The function should modify the list by prepending (adding) the given string to the beginning of each string in the
given list. The function should modify the list given without returning anything.
"""

def prepender(list_of_strings, prepend_string):
    for index in range(len(list_of_strings)):
         list_of_strings[index] = prepend_string + list_of_strings[index]
    return list_of_strings

def main():
    print(prepender(["cool", "super", "great"], "You are "))

if __name__ == "__main__":
    main()