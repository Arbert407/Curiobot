from chatterbot import ChatBot
from textblob.classifiers import NaiveBayesClassifier
from web_scraping.scraper import Scraper 

chatbot = ChatBot("Curiobot")

with open('text_classifier/data.json','r') as fp:
  classifier = NaiveBayesClassifier(fp, format="json")

scrap = Scraper(

  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"},
  pagination = [10,20,30,40,50,60,70,80,90,100],  
  topics = [
    'animales',
    'astronomia',
    'fisica',
    'computacion',
    'espacio',
    'cultura',
    'ingenieria',
    'Descubren',
    'Investigadores',
    'como%20ser',
    'espiritualidad',
    # 'como%20hacer',
  ]

)

print("Soy Curiobot, mi proposito es compartir noticias curiosas :)")

while True:
  
  usuario = input(">>> ")
  if classifier.classify(usuario):
    scrap.find_link()
    continue
  respuesta = chatbot.get_response(usuario)
  print("Curiobot: "+str(respuesta))