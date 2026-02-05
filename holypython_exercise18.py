"""Exercise solutions for Holypython Exercise 18 (operators)."""

from __future__ import annotations


def solve_exercises() -> None:
    """Run small exercises demonstrating operators and assertions."""
    # Exercise 1: swap two variables
    a = 1
    b = 2
    a, b = b, a
    assert (a, b) == (2, 1), "Swap failed"

    # Exercise 2: quotient and remainder
    dividend = 27
    divisor = 4
    quotient = dividend // divisor
    remainder = dividend % divisor
    print("Quotient:", quotient)
    print("Remainder:", remainder)

    # Exercise 3: membership and identity
    items = ["apple", "banana", "cherry"]
    assert "banana" in items
    copy_items = list(items)
    assert copy_items == items and copy_items is not items


def main() -> None:
    solve_exercises()


if __name__ == "__main__":
    main()