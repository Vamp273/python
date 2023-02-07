import re

value = "This is a string."
output = re.search("^This.*string$",value)

print(output)

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"

# comment down each symbol and write its meaning and function.

# . : Matches any single character (except a newline).
# * : Matches zero or more of the preceding character or group.
# + : Matches one or more of the preceding character or group.
# ? : Matches zero or one of the preceding character or group.
# [ ] : Matches any character within the brackets.
# ^ : Matches the start of a string.
# $ : Matches the end of a string.
# \d : Matches any digit (equivalent to [0-9]).
# \w : Matches any word character (equivalent to [a-zA-Z0-9_]).
# \s : Matches any whitespace character (including space, tab, and newline).