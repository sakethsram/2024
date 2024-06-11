# 1 book
book = {"name": "C", "count":10}

print(book)
print(book["name"])
print(book["count"])


# 1 book list
book_list = [
    {"name": "C", "count":10}
    ]

print(book_list)
print(book_list[0]["name"])
print(book_list[0]["count"])


# Multiple book list
book_list = [
    {"name": "C", "count":10}
    {"name": "Python", "count":2}
    ]

print(book_list)
print(book_list[0]["name"])
print(book_list[0]["count"])

print(book_list[1]["name"])
print(book_list[1]["count"])

for book in book_list:
    print(book)

# Multiple book list with multiple people
bh_book_list = [
    {"name": "C", "count":10},
    {"name": "Python", "count":2},
    {"name": "ML", "count":3},
    {"name": "Networking", "count":4},
    ]

sk_book_list = [
    {"name": "C", "count":6},
    {"name": "DS", "count":2},
    {"name": "ML", "count":10},
    {"name": "OS", "count":3},
    ]

merged_book_list = [
    {"name": "C", "count":16},
    {"name": "Python", "count":2},
    {"name": "ML", "count":13},
    {"name": "Networking", "count":4},
    {"name": "DS", "count":2},
    {"name": "OS", "count":3},
]