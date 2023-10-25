import bs4, requests as req

res = req.get("http://www.example.com")
print(res.text)

# lxml : simple path syntax
soup = bs4.BeautifulSoup(res.text, "lxml") #parses data
print(soup,"\n")

# returns list of tag
print(*soup.select('meta'), end="\n")
paras = soup.select('p')

print(paras)
print(len(paras))

#retune the list elt
print("\n", paras[0])
print(type(paras[0]))
#retuens the tag content
print("\n", paras[0].getText())

file = open('./2_data.txt', 'w+')
for p in paras:
    file.write(p.getText() + "\n")