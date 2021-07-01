import requests
import spotipy
import pandas as pd
from sqlalchemy import create_engine

# Program returns access token requiered for get requests when connecting
# to the spotify API. This is based on the given cliend id and
# secret id that the client has.
# 
# @para   cid: str value Client ID
# @para   sid: str value Secret ID  
# 
# @return token: str val of access token
#                None    if error
def get_access_token(cid, sid):
    token = None
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # Request for access token
    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': sid,
    })

    #Update token if success
    if (response.status_code == 200):
        token = response.json()['access_token']

    return token

# Program returns gets json() of playlist requested based on
# given playlist ID. Access token required by spotify to make 
# get requests.
# 
# @para            pid: str value Playlist ID
# @para   access_token: str value access token  
# 
# @return playlist: json() information of playlist
#                   None   if error
def get_playlist(pid, access_token):
    return None;

def main():
    # Collect Items for Authentication
    CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
    SECRET_id = "487346bb76a54e05b308947a10a96ebe"
    access_token = get_access_token(CLIENT_id,SECRET_id) 

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
    todayTopHits = {}
    mostArtists = 0 # Constant with song that has most aritists
    count = 0
    for item in playlist["tracks"]["items"]:
        track = item["track"]

        if track is not None:
            #get all artists names
            artist_names = []
            for artist in track["artists"]:
                artist_names.append(artist["name"])

            todayTopHits[count] = {"Name": track["album"]["name"],
                                  "Add Date": item["added_at"],
                                  "Popularity": track["popularity"],
                                  "Artists": artist_names[0]}

            # print(count, ":" ,track["album"]["name"],)
            # print("     by:", artist_names)
            # print("     Add Date:", item["added_at"])
            # print("     Popularity:", track["popularity"])
        count += 1

    # Create Dataframe From Dictionary
    todayTopHitsdf = pd.DataFrame.from_dict(todayTopHits,
                                            orient = "index",
                                            columns=['Name', 
                                                     'Artists',
                                                     'Add Date',
                                                     'Popularity'])
    print(todayTopHitsdf.head())
    
    #Creating an Engine
    engine = create_engine('mysql://root:codio@localhost/spotify_music')
    todayTopHitsdf.to_sql('today_top_hits', con=engine,
                          if_exists='replace', index=True)

if __name__ == '__main__':
    main()