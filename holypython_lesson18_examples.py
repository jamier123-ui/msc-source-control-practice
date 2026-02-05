"""PEP8-friendly examples for Python operators (Holypython Lesson 18)."""

from __future__ import annotations


def arithmetic_examples() -> None:
    """Arithmetic operators: +, -, *, /, //, %, **."""
    a = 7
    b = 3
    print("Arithmetic:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")


def assignment_examples() -> None:
    """Assignment operators: =, +=, -=, *=, /=."""
    x = 5
    print("\nAssignment:")
    x += 2
    print("x += 2 ->", x)
    x *= 3
    print("x *= 3 ->", x)
    x -= 1
    print("x -= 1 ->", x)


def comparison_examples() -> None:
    """Comparison operators: ==, !=, >, <, >=, <=."""
    a = 10
    b = 20
    print("\nComparison:")
    print("a == b ->", a == b)
    print("a != b ->", a != b)
    print("a < b  ->", a < b)
    print("a <= b ->", a <= b)
    print("a > b  ->", a > b)
    print("a >= b ->", a >= b)


def logical_examples() -> None:
    """Logical operators: and, or, not."""
    t = True
    f = False
    print("\nLogical:")
    print("t and f ->", t and f)
    print("t or f  ->", t or f)
    print("not t   ->", not t)


def bitwise_examples() -> None:
    """Bitwise operators: &, |, ^, ~, <<, >>."""
    a = 0b1010  # 10
    b = 0b0110  # 6
    print("\nBitwise:")
    print("a & b ->", bin(a & b))
    print("a | b ->", bin(a | b))
    print("a ^ b ->", bin(a ^ b))
    print("~a    ->", bin(~a))
    print("a << 1 ->", bin(a << 1))
    print("a >> 1 ->", bin(a >> 1))


def membership_examples() -> None:
    """Membership operators: in, not in."""
    seq = [1, 2, 3]
    print("\nMembership:")
    print("2 in seq ->", 2 in seq)
    print("5 not in seq ->", 5 not in seq)
    print("'py' in 'python' ->", "py" in "python")


def identity_examples() -> None:
    """Identity operators: is, is not."""
    a = [1, 2, 3]
    b = a
    c = list(a)
    print("\nIdentity:")
    print("a is b ->", a is b)
    print("a == c ->", a == c)
    print("a is c ->", a is c)


def precedence_example() -> None:
    """Operator precedence demonstration."""
    result = 3 + 4 * 2 / (1 - 5) ** 2
    print("\nPrecedence:")
    print("3 + 4 * 2 / (1 - 5) ** 2 ->", result)


def main() -> None:
    """Run all examples."""
    arithmetic_examples()
    assignment_examples()
    comparison_examples()
    logical_examples()
    bitwise_examples()
    membership_examples()
    identity_examples()
    precedence_example()


if __name__ == "__main__":
    main()