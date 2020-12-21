books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
book_dict = dict()
for i in range(len(books)):
    key = books[i]
    characters = len(key)
    unique_characters = len(set(key))
    value = (characters, unique_characters)
    book_dict[key] = value
# "ULYSSES": (7, 5)
# "ULYSSES", (7, 5, 6.0)
for book in book_dict.keys():
  
  (characters, unique_characters) = book_dict[book]
  avg = (characters + unique_characters) / 2
  book_dict[book] = (characters, unique_characters, avg)

for book in book_dict.keys():
    value = book_dict[book]
    print(book + " -> " + str(value))

