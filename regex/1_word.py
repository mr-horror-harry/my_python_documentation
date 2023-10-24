import re 

sent="the brown little fox jumped over the lazy dog!"
word1="fox"

#search() : to find the first occurence of the given keyword
print(re.search(word1, sent))
print(re.search(word1, sent).span())
print(re.search(word1, sent).group())

#findall() : to look for count of given keyword entirely 
word2='the'
print(re.findall(word2, sent))

li = re.finditer(word2, sent)
for i in li:
    print(i.span()) #indices of all found matches
    print(i.group()) #printing all span indices