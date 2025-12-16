# format specifiers : {value:format_spec} format a value based on the format_spec provided
# syntax : f"{value:format_spec}"

# example of format specifiers
num = 123.4567
print(f"Original number: {num}")

# format to 2 decimal places
print(f"Formatted to 2 decimal places: {num:.2f}")

# to allocate space to display a value, after the colon we can specify the width
print(f"Number with width 10: {num:10}") # allocates 10 spaces for the number

# if we add 0 before the width, it pads with leading zeros
print(f"Number with leading zeros: {num:010}") # pads with leading zeros to make width 10

# align text within allocated space
text = "Hello"
print(f"Left aligned: {text:<10}")   # left align within 10 spaces
print(f"Right aligned: {text:>10}")  # right align within 10
print(f"Center aligned: {text:^10}") # center align within 10 spaces

# , as a thousands separator
large_num = 1234567890
print(f"With thousands separator: {large_num:,}") # Output: 1,234,567,890

# percentage formatting
percentage = 0.8567
print(f"Percentage: {percentage:.2%}") # Output: 85.67%