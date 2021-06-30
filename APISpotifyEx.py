import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Important constant values
CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
SECRET_id = "487346bb76a54e05b308947a10a96ebe"
AUTH_URL = 'https://accounts.spotify.com/api/token'

#Request for 
response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_id,
    'client_secret': SECRET_id,
})

print(response)
print(response.json())

access_token = response.json()['access_token']
print(access_token)

#headers = {
#    'Authorization': 'Bearer {token}'.format(token=access_token)
#}

#BASE_URL = 'https://api.spotify.com/v1/'
#track_id = '6mFkJmJqdDVQ1REhVfGgd1'
#r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
#r = r.json()
#print(r)

