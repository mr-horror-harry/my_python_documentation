import bs4, requests as req

res = req.get("https://en.wikipedia.org/wiki/Wikipedia")

soup = bs4.BeautifulSoup(res.text, "lxml")

#accessing class : (.)
class_content = soup.select('.vector-toc-link')
print(class_content)

print("\n", class_content[5])
print("\n", class_content[5].getText())

#accessing id : (#)
id_content = soup.select('#vector-main-menu')
print(id_content)

print("\n", id_content[0])
print(id_content[0].getText())

#accessing div : ('div')
#accessing all child ('div span')
#accessing immediate child ('div > span')
