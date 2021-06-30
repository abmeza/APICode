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
playlist_res = requests.get(BASE_url + 'playlists/' + 
        playlist_id, headers = headers)
playlist = playlist_res.json()
print(playlist["id"])

# Print out information about the playlist
print("Today's Top 50 Hits Songs")
print("-------------------------")
count = 0
for item in playlist["tracks"]["items"]:
    track = item["track"]
    if track is not None:
        print(count, "|",
            track["album"]["name"], "|",
            "Time Added:", item["added_at"], "|",
            "Popularity Rank:", track["popularity"])
    count += 1
