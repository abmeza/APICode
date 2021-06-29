import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "2b1a105e0bf94d69924ed5789171693f"
secret_id = "487346bb76a54e05b308947a10a96ebe"






text_input = input("Give text you would like to input: ")

url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': text_input}

response = requests.post(url, data = myobj)

print(response.json())