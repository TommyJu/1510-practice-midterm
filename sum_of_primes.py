"""
Tommy Ju
A01347715

(10) If we add all the prime numbers between 10 and 20, we get 11 + 13 + 17 + 19 = 60 Implement a
function called sum_of_primes. This function accepts two positive integers called lower_bound and upper_bound,
in that order. This function doesn’t promise to work if the arguments are not positive integers.
This function doesn’t promise to work if upper_bound is less than lower_bound. However, if upper_bound is
equal to or greater than lower_bound, then sum_of_primes must return the sum of the prime numbers between the bounds.
The bounds are included.
"""


# bounds are included
def sum_of_primes(lower_bound, upper_bound):

    result = 0
    numbers = list(range(lower_bound, upper_bound + 1))

    for number in numbers:
        if is_prime(number):
            result += number
        else:
            continue
    return result


def is_prime(integer):

    if integer == 1:
        return False

    number_of_factors = 0
    factor = 1

    while factor <= integer:
        if integer % factor == 0:
            number_of_factors += 1
        else:
            pass

        factor += 1

    if number_of_factors > 2:
        return False
    else:
        return True


def main():
    print(is_prime(1))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(7))
    print(is_prime(10))
    print(is_prime(13))
    print("-" * 10)
    print(sum_of_primes(10, 20))
    print(sum_of_primes(13, 13))
    print(sum_of_primes(10, 10))


if __name__ == "__main__":
    main()
