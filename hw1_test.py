import math
import unittest

import data
import hw1
from data import Price
from hw1 import Rectangle


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    class TestVowelCount(unittest.TestCase):
        def test_vowel_count_1(self):
            # Test with a string containing lowercase vowels
            self.assertEqual(hw1.vowel_count("hello"), 2)

        def test_vowel_count_2(self):
            # Test with a string containing uppercase vowels
            self.assertEqual(hw1.vowel_count("WORLD"), 1)

        def test_vowel_count_3(self):
            # Test with a string containing both lowercase and uppercase vowels
            self.assertEqual(hw1.vowel_count("Hello World"), 3)

        def test_vowel_count_4(self):
            # Test with a string containing no vowels
            self.assertEqual(hw1.vowel_count("xyz"), 0)

        def test_vowel_count_5(self):
            # Test with an empty string
            self.assertEqual(hw1.vowel_count(""), 0)

        def test_vowel_count_6(self):
            # Test with a string containing all vowels
            self.assertEqual(hw1.vowel_count("aeiouAEIOU"), 10)

    if __name__ == '__main__':
        unittest.main()

    # Part 2
    import unittest

    class TestShortLists(unittest.TestCase):
        def test_short_lists_1(self):
            # Test with a list containing sublist of varying lengths
            input_list = [[1, 2], [3, 4, 5], [6, 7], [8], [9, 10]]
            expected_output = [[1, 2], [6, 7], [9, 10]]
            self.assertEqual(hw1.short_lists(input_list), expected_output)

        def test_short_lists_2(self):
            # Test with a list containing no sublist of length 2
            input_list = [[1], [2, 3, 4], [5, 6, 7, 8]]
            expected_output = []
            self.assertEqual(hw1.short_lists(input_list), expected_output)

        def test_short_lists_3(self):
            # Test with a list containing only sublist of length 2
            input_list = [[1, 2], [3, 4], [5, 6]]
            expected_output = [[1, 2], [3, 4], [5, 6]]
            self.assertEqual(hw1.short_lists(input_list), expected_output)

        def test_short_lists_4(self):
            # Test with an empty list
            input_list = []
            expected_output = []
            self.assertEqual(hw1.short_lists(input_list), expected_output)

        def test_short_lists_5(self):
            # Test with a list containing sublist of length 2 and other lengths
            input_list = [[1, 2], [3], [4, 5], [6, 7, 8], [9, 10]]
            expected_output = [[1, 2], [4, 5], [9, 10]]
            self.assertEqual(hw1.short_lists(input_list), expected_output)


    # Part 3
    import unittest

    class TestAscendingPairs(unittest.TestCase):
        def test_ascending_pairs_1(self):
            # Test with a list containing sublist of varying lengths
            input_list = [[1, 2], [4, 3], [5, 6, 7], [9, 8], [10]]
            expected_output = [[1, 2], [3, 4], [5, 6, 7], [8, 9], [10]]
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)

        def test_ascending_pairs_2(self):
            # Test with a list containing no sublist of length 2
            input_list = [[1], [2, 3, 4], [5, 6, 7, 8]]
            expected_output = [[1], [2, 3, 4], [5, 6, 7, 8]]
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)

        def test_ascending_pairs_3(self):
            # Test with a list containing only sublist of length 2
            input_list = [[2, 1], [4, 3], [6, 5]]
            expected_output = [[1, 2], [3, 4], [5, 6]]
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)

        def test_ascending_pairs_4(self):
            # Test with an empty list
            input_list = []
            expected_output = []
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)

        def test_ascending_pairs_5(self):
            # Test with a list containing sublist of length 2 and other lengths
            input_list = [[2, 1], [3], [5, 4], [6, 7, 8], [10, 9]]
            expected_output = [[1, 2], [3], [4, 5], [6, 7, 8], [9, 10]]
            self.assertEqual(hw1.ascending_pairs(input_list), expected_output)


    # Part 4
    import unittest

    class TestAddPrices(unittest.TestCase):
        def test_add_prices_1(self):
            # Test with no overflow in cents
            price1 = Price(5, 50)
            price2 = Price(3, 25)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 8)
            self.assertEqual(result.cents, 75)

        def test_add_prices_2(self):
            # Test with overflow in cents
            price1 = Price(2, 75)
            price2 = Price(3, 50)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 6)
            self.assertEqual(result.cents, 25)

        def test_add_prices_3(self):
            # Test with both prices having zero cents
            price1 = Price(10, 0)
            price2 = Price(5, 0)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 15)
            self.assertEqual(result.cents, 0)

        def test_add_prices_4(self):
            # Test with one price having zero dollars
            price1 = Price(0, 50)
            price2 = Price(0, 60)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 1)
            self.assertEqual(result.cents, 10)

        def test_add_prices_5(self):
            # Test with large values
            price1 = Price(100, 99)
            price2 = Price(200, 99)
            result = hw1.add_prices(price1, price2)
            self.assertEqual(result.dollars, 301)
            self.assertEqual(result.cents, 98)

    if __name__ == '__main__':
        unittest.main()

    # Part 5
    import unittest

    class TestRectangleArea(unittest.TestCase):
        def test_rectangle_area_1(self):
            rect = data.Rectangle(data.Point(2, 7), data.Point(5, 3))
            self.assertEqual(hw1.rectangle_area(rect), 12)

        def test_rectangle_area_2(self):
            rect = data.Rectangle(data.Point(0, 10), data.Point(10, 0))
            self.assertEqual(hw1.rectangle_area(rect), 100)

        def test_rectangle_area_3(self):
            rect = data.Rectangle(data.Point(1, 5), data.Point(4, 2))
            self.assertEqual(hw1.rectangle_area(rect), 9)

        def test_rectangle_area_4(self):
            rect = data.Rectangle(data.Point(-3, 4), data.Point(2, -1))
            self.assertEqual(hw1.rectangle_area(rect), 25)


    # Part 6
from data import Book

book1 = Book("Book A", "Author X")
book2 = Book("Book B", "Author Y")
book3 = Book("Book C", "Author X")
book4 = Book("Book D", "Author Z")

book_list = [book1, book2, book3, book4]

result = hw1.books_by_author("Author X", book_list)
print(result)  # Expected output: [Book("Book A", "Author X"), Book("Book C", "Author X")]
    # Part 7
def test_circle_bound():
    rect = Rectangle(0, 0, 4, 6)
    circle = hw1.circle_bound(rect)

    assert circle.x == rect.x, "Circle's center X should match rectangle's center X"
    assert circle.y == rect.y, "Circle's center Y should match rectangle's center Y"
    assert math.isclose(circle.radius, 5.0, rel_tol=1e-6), "Radius should be the correct diagonal distance"

    print(result)


test_circle_bound()

    # Part 8
def test_below_pay_average():
    employees = [
        hw1.Employee("Alice", 50000),
        hw1.Employee("Bob", 60000),
        hw1.Employee("Charlie", 40000),
        hw1.Employee("David", 70000)
    ]

    result = hw1.below_pay_average(employees)
    expected = ["Alice", "Charlie"]  # Their pay is below the average (55,000)

    assert set(result) == set(expected), f"Expected {expected}, but got {result}"

    # Edge case: empty list
    assert hw1.below_pay_average([]) == [], "Expected empty list for no employees"

    # Edge case: all employees have the same pay
    same_pay_employees = [hw1.Employee("Eve", 50000), hw1.Employee("Frank", 50000)]
    assert hw1.below_pay_average(same_pay_employees) == [], "No employee should be below average when all are equal"

    print(result)

test_below_pay_average()



if __name__ == '__main__':
    unittest.main()
