from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

qTerms_file = 'qTerms.txt'
#########################################################################################
#Variables que contienen las credenciales de Twitter 
access_token = 'access_token'
access_secret = 'access_secret'
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

file = open('twPolData.txt', 'a')
query_terms = []
#########################################################################################
# En esta seccion se crea el listener para el stream de tweets
# hereda la clase StreamListener de tweeepy
#
#########################################################################################
class Listener(StreamListener):
    #override las clases para que hagan algo
    def on_data(self, data):
       #json parser a texto  y las guard en un archivo de texto
       json_data = json.loads(data)
       file.write(str(json_data))

    def on_error(self, status_code):
        if (status_code == 420):
            return False

    def on_status(self, status):
    	#se hacer override del metodo
        print(status.text)

#########################################################################################

if __name__ == '__main__':
    #Se inicializan las conexiones (introducir las llaves para la API)
    l = Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #Importa los termino de busqueda del archivo de texto
    with open('qTerms.txt','r') as f:
        for line in f:
            query_terms.append(line.strip('\n'))

    # aqui se realizar el flitro de informacion considerando los terminos entre comillas
    stream.filter(track=query_terms)
