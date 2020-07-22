import bs4 as bs, random
from urllib.request import urlopen, Request


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}

pagination = [10,20,30,40,50,60,70,80,90,100]
topics = [
  # 'animales',
  # 'astronomia',
  # 'fisica',
  # 'computacion',
  # 'espacio',
  # 'cultura',
  # 'Descubren',
  # 'Investigadores',
  # 'como%20ser',
  'espiritualidad'
]

# creating the url and getting information
initial_url = "https://www.google.com/search?tbm=nws&q={}&start={}".format(random.choice(topics),random.choice(pagination))
req = Request(url=initial_url, headers=headers)
source = urlopen(req).read()
soup = bs.BeautifulSoup(source,'lxml')

# select body part of page
body = soup.body

# get ancles of news
news = body.find('div', {"id":"rso"}).find_all("a")


# select a random link
while True:    
  
  selected = random.choice(news)
  if (
    selected.get('href') == "#" or 
    selected.get('href').startswith("https://webcache") or 
    selected.get('href').startswith("http://webcache") or
    "coronavirus" in selected.get('href') == True or 
    "pandemia" in selected.get('href') == True or 
    "cuarentena" in selected.get('href') == True  
  ):
    False
  else: 
    print(selected.get('href'))
    break


