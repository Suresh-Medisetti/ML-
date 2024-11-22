# String slicing
print("STRING SLICING")
text = "Hello, World!"

# Accessing a single character
print("Original String:", text)
print("Character at index 0:", text[0])  # H
print("Character at index -1 (last):", text[-1])  # !

# Substring slicing
print("Substring from index 0 to 4:", text[0:5])  # Hello
print("Substring from index 7 to end:", text[7:])  # World!
print("Substring with step 2:", text[::2])  # Hlo ol!

# Reversing a string
print("Reversed String:", text[::-1])  # !dlroW ,olleH

print("\nLIST SLICING")
# List slicing
numbers = [10, 20, 30, 40, 50, 60]

# Accessing single elements
print("Original List:", numbers)
print("Element at index 0:", numbers[0])  # 10
print("Element at index -1 (last):", numbers[-1])  # 60

# Sublist slicing
print("Sublist from index 1 to 3:", numbers[1:4])  # [20, 30, 40]
print("Sublist from index 3 to end:", numbers[3:])  # [40, 50, 60]
print("Sublist with step 2:", numbers[::2])  # [10, 30, 50]

# Reversing a list
print("Reversed List:", numbers[::-1])  # [60, 50, 40, 30, 20, 10]
