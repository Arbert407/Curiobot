from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

print("Hola me llamo Curiobot, soy una IA que recomienda noticias curiosas :)")
while True:
  usuario = input(">>> ")
  respuesta = chatbot.get_response(usuario)
  print("Curiobot: "+str(respuesta))