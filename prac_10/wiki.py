import wikipedia
from wikipedia import DisambiguationError, PageError, search

search_title = input("Enter page title: ")
while search_title != "":
    try:
        page = wikipedia.page(search_title, auto_suggest =False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(search(search_title))
    except PageError:
        print(f"Page id '{search_title}' does not match any pages. Try another id!")
    print()
    search_title = input("Enter page title: ")
print("Thank you.")