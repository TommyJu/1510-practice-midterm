"""
Tommy Ju
A01347715

 (5) Write a program that generates a random number in the range of 1 through 100 inclusive, and asks the user to
 guess what the number is. While the user’s guess is higher than the random number or lower than the random number,
 the program should display “Too high, try again” or “Too low, try again” as appropriate, and the program should let
 the user ask again. When the user correctly guesses the number, print out the number of guesses the user made and a
  congratulatory message.
(Recall that the random module contains a function called randint(a, b) which accepts two integers and returns a
 random integer N such that a <= N <= b.)
"""
import random


def random_number():
    answer = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the random number from 1 to 100 inclusive: "))
        attempts += 1

        if guess > answer:
            print("\nToo high, try again.")
        elif guess < answer:
            print("\nToo low, try again.")
        else:
            print("\n🎉🎉🎉 Congratulations! You are correct. The answer is {}, it took you {} attempts.".format(answer, attempts))
            return


def main():
    random_number()


if __name__ == "__main__":
    main()
