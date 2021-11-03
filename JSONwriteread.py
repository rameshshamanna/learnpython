book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street NY',
    'phone': 360888333
}

book['ramesh'] = {
    'name': 'ramesh',
    'address': '1 green street NY',
    'phone': 360888222
}

#dumps is dump as string
import json
s = json.dumps(book)
with open("C://code//book.txt","w") as f:
    f.write(s)

