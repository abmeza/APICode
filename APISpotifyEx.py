import requests
import spotipy

# Important constant values
CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
SECRET_id = "487346bb76a54e05b308947a10a96ebe"
AUTH_URL = 'https://accounts.spotify.com/api/token'

# Request for access token
response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_id,
    'client_secret': SECRET_id,
})
access_token = response.json()['access_token']

# Get an album from spotify
BASE_url = 'https://api.spotify.com/v1/'
playlist_id = '37i9dQZF1DXcBWIGoYBM5M'  # Todays top hits 50

# Get Playlist
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
playlist_res = requests.get(BASE_url + 'playlists/' + playlist_id,
                            headers = headers)
playlist = playlist_res.json()
print(playlist["id"])

# Store and print out desired information 
# about the playlist that was selected
print("Today's Top 50 Hits Songs")
print("-------------------------")
todayTopSongs = {}
count = 0
for item in playlist["tracks"]["items"]:
    track = item["track"]
    if track is not None:
        #get all artists names
        artist_names = []
        for artist in track["artists"]:
            artist_names.append(artist["name"])
        
        print(count, ":" ,track["album"]["name"],)
        print("     by:", artist_names)
        print("     Popularity:", track["popularity"])
        todayTopSongs[count] = {"Name": track["album"]["name"],
                                "Artists": artist_names,
                                "Popularity": track["popularity"]}
    count += 1
print(todayTopSongs)