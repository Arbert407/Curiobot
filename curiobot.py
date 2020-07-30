from chatterbot import ChatBot
from textblob.classifiers import NaiveBayesClassifier
from chatterbot.trainers import ChatterBotCorpusTrainer
from web_scraping.scraper import Scraper 

class Curiobot:

  def train(
    self, 
    chatbot = ChatBot("Curiobot")
  ):
    'train the chatbot'

    trainer = ChatterBotCorpusTrainer(chatbot)

    trainer.train("chatterbot.corpus.spanish", './food/')

  def play(
    self, 
    text_classifier, 
    scraper,
    search_depth, 
    chatbot,
  ):
    'run chatbot'

    print("Curiobot: Soy Curiobot, mi proposito es compartir noticias curiosas :)")

    while True:
      
      usuario = input("Yo: ")
      if text_classifier.classify(usuario):
        print("Curiobot: Estoy buscando algo para tí...")
        if not scraper.find_link(search_depth):
          print("Curiobot: No encontré algo interesante :(  mis disculpas.")
        continue
      respuesta = chatbot.get_response(usuario)
      print("Curiobot: "+str(respuesta))


curiobot = Curiobot()

# curiobot.train()

curiobot.play(
  text_classifier = NaiveBayesClassifier(open('./text_classifier/data.json','r'), format="json"),
  scraper = Scraper(
    headers = {
      "User-Agent"  : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
    },
    pagination = [0,10,20,30,40,50,60,70,80,90,100],  
    topics = [
      # '%C2%BFQu%C3%A9%20es',
      # '%C2%BFQu%C3%A9%20fue',
      # '%C2%BFc%C3%B3mo',
      # 'animales',
      # 'astronomia',
      # 'computacion',
      # 'como%20hacer',
      # 'como%20ser',
      # 'covid', 
      # 'cultura',
      'Descubren',
      # 'espacio',
      # 'espiritualidad',
      # 'fisica',
      # 'ingenieria',
      # 'Investigadores',
      # 'invento',
      # 'matematicas',
    ],
    words_to_prevent = {
      "asesina",
      "Coronavirus",  
      "coronavirus",  
      "COVID",
      "Covid",
      "covid",
      "Covid-19",
      "covid-19",
      "covid19",
      "cuarentena", 
      "erot", 
      "muertes",
      "pandemia",
      "sucesos",
    }
  ),
  search_depth = 2,
  chatbot = ChatBot("Curiobot")
)

