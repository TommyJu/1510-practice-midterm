"""
(7) Write a program that simulates rolling 1000000d6 and tallies the results.  That is, roll a 6-sided die one
million times and keep track of how many times each side is rolled, then report the results.

(Consider what we need to do.  We need to simulate rolling a die a million times.  That suggests we need
generate a random number, and we need to use a loop.  While we have not yet rolled the die a million
times, we roll it again, and record the value, keeping track of whether we’ve reach a million yet.

We probably want to record the value using a dictionary. The dictionary’s keys should be integers: 1, 2, 3,
4, 5, 6, and its values will be the number of times each number is rolled

Before any die has been rolled, the values in the dictionary will be zero of course.  Suppose the first thing
we roll is a 1.  The value for the key 1 will increment from 0 to 1.  Suppose we roll a 1 again (imagine the
odds!).  The value for the key 1 must now increment from 1 to 2.

There are at least three ways we can loop through the dictionary and print its contents.  After the die has
been rolled one million times, pick one, and print the results.)

"""
from random import randint


def roll_6_sided_die(number_of_rolls):
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    counter = 0
    while counter < number_of_rolls:
        results[randint(1, 6)] += 1
        counter += 1

    {print(f"Side {key}: {value} rolls") for (key, value) in results.items()}
    print("Total rolls:", sum(results.values()))

# USE MAIN FUNCTION
roll_6_sided_die(1000000)
