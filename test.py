from bs4 import BeautifulSoup

f.open("index.html")
soup = BeautifulSoup(f, 'html.parser')
f.close()

print(soup.prettify())
print(soup.findALL('span'))

for content in soup.findAll('span'):
    print(soup.text)
