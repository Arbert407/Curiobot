import bs4 as bs, random
from urllib.request import urlopen, Request


class Scraper:
  'Getting information from internet'

  def __init__(self, headers, pagination, topics, words_to_prevent):

    self.headers = headers
    self.pagination = pagination
    self.topics = topics
    self.words_to_prevent = words_to_prevent

  def set_soup(self):
    'creating the url and getting information'

    initial_url = "https://www.google.com/search?tbm=nws&q={}&start={}".format(
      random.choice(self.topics),
      random.choice(self.pagination
    ))
    # print(initial_url)
    req = Request(url=initial_url, headers=self.headers)
    source = urlopen(req).read()
    soup = bs.BeautifulSoup(source,'lxml')
    return soup

  def find_link(self, iterations=1):
    
    bad_links = 0

    # select body part of page
    body = self.set_soup().body

    # get news
    news = list(body.find('div', {"id":"rso"}))
    
    # select a random link
    while True:  

      if bad_links == len(news):
        
        if iterations == 0:
          return False
        else:
          return self.find_link(iterations=iterations-1)
      
      selected = random.choice(news)
      title = selected.find("div", {"class":"JheGif nDgy9d"}).text
      link = selected.find("a").get("href")
      
      if (
        any(word in title for word in self.words_to_prevent) or 
        any(word in link for word in self.words_to_prevent)
      ):
        bad_links += 1
        continue
      else:
        print("-------------------------------------------")
        print(title)
        print("   "+link)
        print("-------------------------------------------")
        break

    return link


# # Object for practice
# scrap = Scraper(

#   headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
#   },
#   pagination = [0,10,20,30,40,50,60,70,80,90,100],  
#   topics = [
#     # '%C2%BFQu%C3%A9%20es',
#     # '%C2%BFQu%C3%A9%20fue',
#     # '%C2%BFc%C3%B3mo',
#     # 'animales',
#     # 'astronomia',
#     # 'computacion',
#     # 'como%20hacer',
#     # 'como%20ser',
#     # 'covid', 
#     # 'cultura',
#     'Descubren',
#     # 'espacio',
#     # 'espiritualidad',
#     # 'fisica',
#     # 'ingenieria',
#     # 'Investigadores',
#     # 'invento',
#     # 'matematicas',
#   ],
#   words_to_prevent = {
#     "asesina",
#     "Coronavirus",  
#     "coronavirus",  
#     "COVID",
#     "Covid",
#     "covid",
#     "Covid-19",
#     "covid-19",
#     "covid19",
#     "cuarentena", 
#     "erot", 
#     "muertes",
#     "pandemia",
#     "sucesos",
#   }

# )

# scrap.find_link(3)