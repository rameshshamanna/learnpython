f = open("C://code//book.txt","r")
s = f.read()
print(s)

# loads is load string
import json
book = json.loads(s)
print(book)

print(type(book))

g = book['ramesh']
print(g)

h = book['ramesh']['phone']
print(h)

for person in book:
    print(book[person])


