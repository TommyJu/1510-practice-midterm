"""
Tommy Ju
A01347715

(10) Write a program that simulates rolling a die and tallies and then reports the result. Start by asking the user for
the number of sides, and then how many times they want to roll the die. You must tally and then report the results,
i.e., keep track of how many times each side is rolled, then print the results.
(Consider what we need to do. We need to simulate rolling a die with a certain number of sides a certain number of
times. That suggests we need generate a random number, and we need to use a loop. While we have not yet rolled the
 die the total number of times, we roll it again, and record the value, keeping track of whether we’ve rolled it
 enough times yet.
We probably want to record the value using a dictionary. The dictionary’s keys should be integers: 1, 2, 3, and
so on..., and its values will be the number of times each number is rolled
Before any die has been rolled, the values in the dictionary will be zero of course. Suppose the first thing we
 roll is a 1. The value for the key 1 will increment from 0 to 1. Suppose we roll a 1 again (imagine the odds!).
 The value for the key 1 must now increment from 1 to 2.
There are at least three ways we can loop through the dictionary and print its contents. After the die has been
rolled the correct number of times, pick one, and print the results.)
There is room on the next page to complete this program.
"""
import random


def tally_dice(sides, max_rolls):

    # Generate the dictionary
    tally = {}
    for number in range(1, sides + 1):
        tally[number] = 0

    # Roll the dice
    while max_rolls > 0:
        roll = random.randint(1, sides)
        tally[roll] += 1

        max_rolls -= 1

    return tally


def main():
    print(tally_dice(1, 0))
    print(tally_dice(1, 6))
    print(tally_dice(5, 10))
    print(tally_dice(2, 9999))


if __name__ == "__main__":
    main()
