"""Rewritten examples for learnpython.org 'Basic Operators'."""

from __future__ import annotations


def basic_arithmetic() -> None:
    """Show basic arithmetic operations and formatted division."""
    a, b = 8, 3
    print("Basic arithmetic examples")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b:.3f}")


def comparisons_and_logic() -> None:
    """Show comparisons combined with logical operators."""
    x, y = 5, 10
    print("\nComparisons and logic")
    print("x < y ->", x < y)
    print("(x < y) and (y == 10) ->", (x < y) and (y == 10))
    print("(x > y) or (y == 10) ->", (x > y) or (y == 10))


def main() -> None:
    basic_arithmetic()
    comparisons_and_logic()


if __name__ == "__main__":
    main()