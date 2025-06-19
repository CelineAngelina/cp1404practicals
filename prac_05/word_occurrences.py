"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
start 1:33
"""

string_to_count = {}
text = input("Text: ")
strings = text.split()

word_width = max((len(word) for word in strings))

for string in strings:
    if string in string_to_count:
        string_to_count[string] += 1
    else:
        string_to_count[string] = 1
    print(f"{string:{word_width}} : {string_to_count[string]}")