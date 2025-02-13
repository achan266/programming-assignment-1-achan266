# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    # Define the set vowels (both lowercase and uppercase)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    #initialize a counter for vowels
    count = 0

    #Iterate through each character in the string
    for char in s:
        if char in vowels:
            count += 1
    return count
# Part 2
def short_lists(lists: list[list[int]]) -> list[list[int]]:
    # Use a list comprehension to filter sublist of length 2
    return [sublist for sublist in lists if len(sublist) == 2]

# Part 3
def ascending_pairs(lists: list[list[int]]) -> list[list[int]]:
    # Iterate through each sublist in the input list
    result = []
    for sublist in lists:
        # If the sublist has exactly 2 elements, sort it in ascending order
        if len(sublist) == 2:
            result.append(sorted(sublist))
        else:
            # Otherwise, add the sublist as is
            result.append(sublist)
    return result

# Part 4
from data import Price, Book  # Import the Price class from the provided data module

def add_prices(price1: Price, price2: Price) -> Price:
    # Calculate the total dollars and cents
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    # Handle overflow of cents (if cents >= 100)
    if total_cents >= 100:
        total_dollars += total_cents // 100  # Convert excess cents to dollars
        total_cents = total_cents % 100       # Keep the remaining cents

    # Return a new Price object with the calculated dollars and cents
    return Price(total_dollars, total_cents)

# Part 5
from data import Rectangle

def rectangle_area(rect: Rectangle) -> float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return width * height

# Part 6
def books_by_author(self: str, books: list["Book"]) -> list["Book"]:
        return [book for book in books if book.author == self]


# Part 7
import math

class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x  # X-coordinate of the center
        self.y = y  # Y-coordinate of the center
        self.width = width
        self.height = height

class Circle:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x  # X-coordinate of the center
        self.y = y  # Y-coordinate of the center
        self.radius = radius

def circle_bound(rect: Rectangle) -> Circle:
    # The circle is centered at the rectangle's center
    center_x = rect.x
    center_y = rect.y
    # The radius is the distance from the center to a corner
    radius = math.sqrt((rect.width / 2) ** 2 + (rect.height / 2) ** 2)
    return Circle(center_x, center_y, radius)

# Part 8
class Employee:
    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay

def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []

    total_pay = sum(emp.pay for emp in employees)
    average_pay = total_pay / len(employees)

    return [emp.name for emp in employees if emp.pay < average_pay]
