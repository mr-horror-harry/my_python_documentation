import requests

result = requests.get("http://www.example.com")
print(type(result))
print(result.text)

file = open('./read_data.html','w+')
file.write(result.text)
file.close()

file = open('./read_data.txt','w+')
file.write(result.text)
file.close()
