"""
LearnPython.org: Basic Operators - Examples
Rewritten to PEP 8 standards
"""

# Arithmetic Operators

# Addition
result_add = 5 + 3
print(f"5 + 3 = {result_add}")

# Subtraction
result_sub = 10 - 4
print(f"10 - 4 = {result_sub}")

# Multiplication
result_mul = 6 * 7
print(f"6 * 7 = {result_mul}")

# Division
result_div = 15 / 3
print(f"15 / 3 = {result_div}")

# Modulo (remainder)
result_mod = 17 % 5
print(f"17 % 5 = {result_mod}")

# Power
result_pow = 2 ** 3
print(f"2 ** 3 = {result_pow}")

# Floor Division
result_floor_div = 17 // 5
print(f"17 // 5 = {result_floor_div}")

# Using Operators with Strings

# Concatenation with +
greeting = "Hello" + " " + "World"
print(f"String concatenation: {greeting}")

# Repetition with *
repeated_string = "Ha" * 3
print(f"String repetition: {repeated_string}")

# Using Operators with Lists

# Joining lists with +
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined_list = list_a + list_b
print(f"Combined lists: {combined_list}")

# Repeating list with *
repeated_list = [1, 2] * 3
print(f"Repeated list: {repeated_list}")

# Exercise: Create two lists with repeated values
x = 10
y = 20
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(f"x_list: {x_list}")
print(f"y_list: {y_list}")
print(f"big_list: {big_list}")
print(f"Length of big_list: {len(big_list)}")
