"""
Word Occurrences
Estimate: 20 minutes
Actual:   43 minutes
"""

string_to_count = {}
text = input("Text: ")
strings = text.split()

for string in strings:
    if string in string_to_count:
        string_to_count[string] += 1
    else:
        string_to_count[string] = 1

word_width = max((len(word) for word in strings))

for word in sorted(string_to_count):
    print(f"{word:{word_width}} : {string_to_count[word]}")