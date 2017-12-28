from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

qTerms_file = 'qTerms.txt'
#########################################################################################
#Variables que contienen las credenciales de Twitter 
access_token = "427881352-jMDnsdYmrAoIqEWwapkRxOLXbeqrQKu96pCBlZyV"
access_secret = "nzvhhLpq21B02EN7WbdLtA4CHVYaj0eLrXrjTbQpo3iER"
consumer_key = "x9N0Rnphl1xVM8LWaOlPpWtVl"
consumer_secret = "K0JnfXuQGPtQEtFI9JSHAfHnOGOb7pYw3svDjk1jREug6p47DN"

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
	#This handles Twitter authetification and the connection to Twitter Streaming API
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
