# Strings are IMMUTABLE
name = "vijay"

# Length of string
print(len(name)) # 5

# Check if string ends with desired characters
# string.endswith("rry")
print(name.endswith("ay")) # True
print(name.endswith("ja")) # False

# Check if string starts with desired characters
# string.endswith("rry")
print(name.startswith("vi")) # True
print(name.startswith("ja")) # False

# string.count("a") – counts the total number of occurrences of any character
print(name.count("i")) # 1

# string.capitalize() - To capitalise the first letter of a string
print(name.capitalize())

# More string functions

# string.find("sub") – returns the first index of substring, -1 if not found
print(name.find("j"))   # 2
print(name.find("z"))   # -1

# string.replace("old", "new") – replaces all occurrences of old with new
print(name.replace("vijay", "raju"))  # raju
text = "banana"
print(text.replace("a", "o"))

# string.upper() – converts string to uppercase
print(name.upper())  # VIJAY

# string.lower() – converts string to lowercase
print(name.lower())  # vijay

# string.title() – converts first letter of every word to uppercase
print("vijay bhaskar".title())  # Vijay Bhaskar

# string.swapcase() – swaps lowercase to uppercase and vice versa
print("ViJaY".swapcase())  # vIjAy

# string.strip() – removes leading and trailing whitespaces
print("   hello   ".strip())  # hello

# string.lstrip() – removes leading whitespaces
print("   hello".lstrip())  # hello

# string.rstrip() – removes trailing whitespaces
print("hello   ".rstrip())  # hello

# string.isalpha() – checks if all characters are alphabets
print("vijay".isalpha())  # True
print("vijay123".isalpha())  # False

# string.isdigit() – checks if all characters are digits
print("123".isdigit())  # True
print("12a3".isdigit())  # False

# string.isalnum() – checks if all characters are alphanumeric
print("vijay123".isalnum())  # True
print("vijay 123".isalnum())  # False (space not allowed)

# string.isspace() – checks if string contains only whitespaces
print("   ".isspace())  # True
print(" a ".isspace())  # False

# string.startswith() and string.endswith() can also take index ranges
print(name.startswith("i", 1, 3))  # True (checks from index 1 to 2)
print(name.endswith("j", 0, 3))    # True (checks till index 2)
