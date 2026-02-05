"""
Holy Python Exercise 18: Python Operators - Exercises
Rewritten to PEP 8 standards with solutions
"""

# Exercise 18-a: Assignment Operator (=)
# Assign a list of colors to the variable
colors = ["yellow", "white", "blue"]
print(colors)

# Exercise 18-b: Division Operator (/)
# Assign division of a to b to the variable
a = 10
b = 3
result = a / b
print(result)

# Exercise 18-c: Addition using +=
# Add 100 to the variable using +=
vertical_speed = 750
vertical_speed += 100
print(vertical_speed)

# Additional practice exercises following PEP 8

# Exercise with arithmetic operators
num_1 = 20
num_2 = 5
sum_result = num_1 + num_2
diff_result = num_1 - num_2
product_result = num_1 * num_2
quotient_result = num_1 / num_2
remainder_result = num_1 % num_2
power_result = num_1 ** 2

print(f"\nArithmetic Operations:")
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
print(f"Remainder: {remainder_result}")
print(f"Power: {power_result}")

# Exercise with comparison operators
is_greater = num_1 > num_2
is_equal = num_1 == num_2
is_not_equal = num_1 != num_2

print(f"\nComparison Operations:")
print(f"{num_1} > {num_2}: {is_greater}")
print(f"{num_1} == {num_2}: {is_equal}")
print(f"{num_1} != {num_2}: {is_not_equal}")

# Exercise with membership operators
items = ["apple", "banana", "cherry"]
is_in = "apple" in items
is_not_in = "grape" not in items

print(f"\nMembership Operations:")
print(f"'apple' in items: {is_in}")
print(f"'grape' not in items: {is_not_in}")

# Exercise with logical operators
condition_1 = True
condition_2 = False

and_result = condition_1 and condition_2
or_result = condition_1 or condition_2
not_result = not condition_1

print(f"\nLogical Operations:")
print(f"True and False: {and_result}")
print(f"True or False: {or_result}")
print(f"not True: {not_result}")

# Exercise with assignment operators
value = 15
value += 5
print(f"\nAssignment Operations (+=): {value}")

value -= 3
print(f"After -=: {value}")

value *= 2
print(f"After *=: {value}")

value //= 4
print(f"After //=: {value}")
