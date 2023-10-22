"""
Tommy Ju
A01347715
"""
from unittest import TestCase
from is_sorted import is_sorted


def main():
    pass


if __name__ == "__main__":
    main()


class TestSorting(TestCase):
    def test_one_integer(self):
        actual = is_sorted([-1])
        expected = True
        self.assertEquals(expected, actual)

    def test_two_integers_correctly_sorted(self):
        actual = is_sorted([1, 2])
        expected = True
        self.assertEquals(expected, actual)

    def test_two_integers_incorrectly_sorted(self):
        actual = is_sorted([2, 1])
        expected = False
        self.assertEquals(expected, actual)

    def test_multiple_integers_correctly_sorted(self):
        actual = is_sorted([-999, -1, 0, 2, 7, 7, 1000])
        expected = True
        self.assertEquals(expected, actual)

    def test_multiple_integers_incorrectly_sorted(self):
        actual = is_sorted([-5, -1, 0, 1, 1, 100, 5])
        expected = False
        self.assertEquals(expected, actual)