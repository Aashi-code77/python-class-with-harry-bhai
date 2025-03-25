name = "Aashi"
print(len(name))
print(name.endswith("hi"))  # true
print(name.startswith("AA")) # false
print(name.startswith("Aa")) # true
print(name.capitalize()) # capital the first letter




### String Methods:
# len(s) – Returns the length of the string.

# s.lower() – Converts all characters in s to lowercase.

# s.upper() – Converts all characters in s to uppercase.

# s.strip() – Removes leading and trailing spaces (or specified characters).

# s.lstrip() – Removes leading spaces (or specified characters).

# s.rstrip() – Removes trailing spaces (or specified characters).

# s.replace(old, new) – Replaces occurrences of old with new.

# s.split(delimiter) – Splits the string into a list using delimiter (default is whitespace).

# s.join(iterable) – Joins elements of an iterable with s as a separator.

# s.find(sub) – Returns the first index of sub in s or -1 if not found.

# s.index(sub) – Returns the first index of sub in s, raises an error if not found.

# s.count(sub) – Counts occurrences of sub in s.

# s.startswith(prefix) – Checks if s starts with prefix, returns True or False.

# s.endswith(suffix) – Checks if s ends with suffix, returns True or False.

# s.capitalize() – Capitalizes the first letter and makes the rest lowercase.

# s.title() – Capitalizes the first letter of each word.

# s.swapcase() – Swaps uppercase and lowercase characters.

# s.isalpha() – Returns True if all characters are alphabetic.

# s.isdigit() – Returns True if all characters are digits.

# s.isalnum() – Returns True if all characters are alphanumeric (letters or digits).

# s.isspace() – Returns True if all characters are whitespace.

# s.islower() – Returns True if all characters are lowercase.

# s.isupper() – Returns True if all characters are uppercase.

# s.zfill(width) – Pads the string with zeros on the left to match width.


s = "  Hello World!  "

print(len(s))          # 15
print(s.lower())       # "  hello world!  "
print(s.upper())       # "  HELLO WORLD!  "
print(s.strip())       # "Hello World!"
print(s.replace("World", "Python"))  # "  Hello Python!  "
print(s.split())       # ['Hello', 'World!']
print("-".join(["Python", "is", "fun"]))  # "Python-is-fun"
print(s.find("World")) # 8
print(s.startswith(" ")) # True
print(s.endswith("!"))  # True

# Escape Sequence characters -- \n , \t , \"BOY\"
a = "Harry is a good boy\nbut not a bad\t\"BOY\""
print(a)


# Escape Sequence	Description
# \'	Single quote (')
# \"	Double quote (")
# \\	Backslash (\)
# \n	Newline (Line break)
# \t	Tab (Horizontal Tab)
# \r	Carriage return
# \b	Backspace
# \f	Form feed
# \v	Vertical tab
# \0	Null character
# \ooo	Octal value (e.g., \101 for 'A')
# \xhh	Hexadecimal value (e.g., \x41 for 'A')



print('Hello\nWorld')   # Newline
print('Tab\tSpace')     # Tab space
print('Backslash: \\')  # Backslash
print('Single Quote: \'')  # Single quote inside a string
print('Double Quote: \"')  # Double quote inside a string