import re

filereader = open("text.txt", mode="r", encoding="utf-8")
mytext = filereader.read()
filereader.close()

# examples
# \d - any digit 0-9
# \D - any non digit
# \w - any alphabet symbol [A-Z, a-z]
# \W - any non alphabet symbol
# \s - whitespace
# \S - non whitespace
# [0-9] - any digit 0-9
# [A-Z] - any uppercase alphabet symbol
# [a-z] - any lowercase alphabet symbol
# + - one and more
# * - zero and more


def find_template(template):
    print(re.findall(template, mytext))


print("\n*** Example 1 ***")
find_template(r"good")

print("\n*** Example 2 ***")
find_template(r"\d\d\d\d\d\d\d")

print("\n*** Example 3 ***")
find_template(r"[0-9]{6}")

print("\n*** Example 4 ***")
find_template(r"[A-Z][a-z]+")
find_template(r"[A-Z][a-z]*")

print("\n*** Example 5 ***")
find_template(r"\w+\.\w+")

print("\n*** Example 6 ***")
find_template(r"\w+\@\w+\.\w+")
