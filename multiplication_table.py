"""
Tommy Ju
A01347715

We are going print a multiplication table from 1 to n inclusive.
Example:
    1   2   3   4
1   1   2   3   4
2   2   3   6   8
"""


def multiplication_table(max_operand_value):
    # create a number sequence from 1 to n inclusive
    table_size = range(1, int(max_operand_value) + 1)

    # create the top row
    for column_value in table_size:
        print("\t" + str(column_value), end='')
    print()

    # create each row
    for row_value in table_size:
        # print the left most digit of each row
        print(row_value, end='')

        # multiply each row by the respective column
        for column_value in table_size:
            print("\t" + str(row_value * column_value), end='')

        # create newline for next row
        print()


def main():
    multiplication_table(4)


if __name__ == "__main__":
    main()
