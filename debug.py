#!/usr/bin/env python3

from lib.book import Book
from lib.shoe import Shoe

# Test Book functionality
print("=== Book Class Demo ===")
book = Book("The Great Gatsby", 180)
print(f"Title: {book.title}")
print(f"Page count: {book.page_count}")

# Test page turning
book.turn_page()

# Test page_count validation
print("\nTesting page_count validation:")
book.page_count = "not a number"  # Should print error message
book.page_count = 200  # Should work fine
print(f"New page count: {book.page_count}")

print("\n=== Shoe Class Demo ===")
shoe = Shoe("Nike", 10)
print(f"Brand: {shoe.brand}")
print(f"Size: {shoe.size}")

# Test cobbling
print("\nBefore cobbling:")
print(f"Condition: {getattr(shoe, 'condition', 'Not set')}")
shoe.cobble()
print(f"After cobbling - Condition: {shoe.condition}")

# Test size validation
print("\nTesting size validation:")
shoe.size = "not a number"  # Should print error message
shoe.size = 11  # Should work fine
print(f"New size: {shoe.size}")