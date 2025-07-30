import wikipedia
from wikipedia import search

from wikipedia import DisambiguationError

search_title = input("Enter page title: ")
while search_title != "":
    try:
        page = wikipedia.page(search_title, auto_suggest =False)
        print(page.title)
        print(search(search_title))
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
    search_title = input("Enter page title: ")
print("Thank you.")