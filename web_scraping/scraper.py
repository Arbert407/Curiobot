import bs4 as bs, random
from urllib.request import urlopen, Request


class Scraper:
  'Getting information from internet'

  def __init__(self, headers, pagination, topics):

    self.headers = headers
    self.pagination = pagination
    self.topics = topics

  def set_soup(self):

    # creating the url and getting information
    initial_url = "https://www.google.com/search?tbm=nws&q={}&start={}".format(random.choice(self.topics),random.choice(self.pagination))
    req = Request(url=initial_url, headers=self.headers)
    source = urlopen(req).read()
    soup = bs.BeautifulSoup(source,'lxml')
    return soup

  def find_link(self):
    
    bad_links = 0

    # select body part of page
    body = self.set_soup().body

    # get ancles of news
    news = body.find('div', {"id":"rso"}).find_all("a")
    
    # select a random link
    while True:  

      if bad_links == len(news):
        link = self.find_link()
      
      selected = random.choice(news)
      
      if (
        selected.get('href') == "#" or 
        selected.get('href').startswith("https://webcache") or 
        selected.get('href').startswith("http://webcache") or
        "coronavirus" in selected.get('href') == True or 
        "pandemia" in selected.get('href') == True or 
        "cuarentena" in selected.get('href') == True  
      ):
        bad_links += 1
        False
      else:
        link = selected.get('href')  
        print(link)
        break
    
    return link


# scrap = Scraper(

#   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"},
#   pagination = [10,20,30,40,50,60,70,80,90,100],  
#   topics = [
#     'animales',
#     'astronomia',
#     'fisica',
#     'computacion',
#     'espacio',
#     'cultura',
#     'ingenieria',
#     'Descubren',
#     'Investigadores',
#     'como%20ser',
#     'espiritualidad',
#     # 'como%20hacer',
#   ]

# )

# scrap.find_link()