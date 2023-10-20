import re 

sent="the brown little fox jumped over the lazy dog!"
word1="fox"

print(re.search(word1, sent))
print(re.search(word1, sent).span())
print(re.search(word1, sent).group())

word2='the'
print(re.findall(word2, sent))

li = re.finditer(word2, sent)
for i in li:
    print(i.span())
    print(i.group())