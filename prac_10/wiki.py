from wikipedia import search

search_title = input("Enter page title: ")
while search_title != "":
    print(search(search_title))
    search_title = input("Enter page title: ")
print("Thank you.")