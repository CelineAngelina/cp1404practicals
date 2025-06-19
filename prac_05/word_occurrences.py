"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
"""

string_to_count = {}
text = input("Text: ")
strings = text.split()

for string in strings:
    if string in string_to_count:
        string_to_count[string] += 1
    else:
        string_to_count[string] = 1
    print(f"{string} : {string_to_count[string]}")