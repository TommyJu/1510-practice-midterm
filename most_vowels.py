"""
Tommy Ju
A01347715

10) Implement a function called most_vowels that accepts a possibly empty tuple of strings and returns an
integer representing the number of vowels in the string that contains the most vowels. For example, if passed a
tuple containing the strings ‘a’, ‘eve’, and ‘applesauce’, the function will return 5 because the word applesauce
contains five vowels and a and eve only contain one and two respectively.
"""

# We will assume y is a vowel because I support inclusion
vowels = ["a", "e", "i", "o", "u", "y"]
def most_vowels(tuple_of_strings):

    max_vowels = 0
    for word in tuple_of_strings:

        vowels_in_word = 0
        for character in word:
            if character.casefold() in vowels:
                vowels_in_word += 1
            else:
                continue

        if vowels_in_word > max_vowels:
            max_vowels = vowels_in_word
        else:
            continue

    return max_vowels

def main():
    print(most_vowels(("a", "eve", "Applesauce")))
    print(most_vowels(()))


if __name__ == "__main__":
    main()
