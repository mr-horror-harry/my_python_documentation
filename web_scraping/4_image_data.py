import requests as req, bs4
print("Images from Inida Today on 10/25/2023: ")
res = req.get("https://www.indiatoday.in/movies/regional-cinema/story/leo-box-office-collection-day-6-thalapathy-vijay-film-continues-its-dream-run-2453255-2023-10-25")

soup = bs4.BeautifulSoup(res.text, 'lxml')
images = soup.select('img')

print("Toatal No. of image content:", len(images))

file=""
for i in range(len(images)):
    img_tag = images[i]
    try:
        link = img_tag['src']

        img_data = req.get(link)

        file = open(f'./images/image{i}.jpg', 'wb')
        file.write(img_data.content)
    except:
        continue

file.close()