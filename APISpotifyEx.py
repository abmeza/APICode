import requests
import spotipy
import pandas as pd
from sqlalchemy import create_engine


# Program returns access token requiered for get requests when connecting
# to the spotify API. This is based on the given cliend id and
# secret id that the client has.
# @para   cid: str value Client ID
# @para   sid: str value Secret ID
# @return token: str val of access token
#                None    if unsuccessful
def get_access_token(cid, sid):
    token = None
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # Request for access token
    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': sid,
    })

    # Update token if success
    if (response.status_code == 200):
        token = response.json()['access_token']
    return token


# Program returns gets json() of playlist requested based on
# given playlist ID. Access token required by spotify to make
# get requests.
# @para            pid: str value Playlist ID
# @para   access_token: str value access token
# @return playlist: json() information of playlist
#                   None   if error
def get_playlist(pid, access_token):
    playlist = None
    BASE_url = 'https://api.spotify.com/v1/playlists/'

    # Get request for playlist
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    response = requests.get(BASE_url + pid, headers=headers)

    # Update playlist if successful get request
    if (response.status_code == 200):
        playlist = response.json()

    return playlist


# Parses through given json playlist, grabs desired infromation,
# which can be changed as desired. This is then turned into a
# data frame and returned
# @para playlist: json() information of playlist
# @return playlist_df: pd.DataFrame of desired information from playlist
def parse_playlist_to_dataframe(playlist):
    playlist_df = pd.DataFrame()   # return value
    playlist_dict = {}
    count = 0   # track order of songs in playlist

    # Loop through playlist items
    for item in playlist["tracks"]["items"]:
        track = item["track"]

        # Make sure item is track before parsing
        if track is not None:
            # Parse artists to make list of names
            artist_names = []
            for artist in track["artists"]:
                artist_names.append(artist["name"])

            playlist_dict[count] = {"Name": track["album"]["name"],
                                    "Add Date": item["added_at"],
                                    "Popularity": track["popularity"],
                                    "Artists": artist_names[0]}
        count += 1
    playlist_df = pd.DataFrame.from_dict(playlist_dict,
                                         orient="index",
                                         columns=['Name',
                                                  'Artists',
                                                  'Add Date',
                                                  'Popularity'])
    return playlist_df


# DEBUGGING HELPFUL
# Takes playlist json(), and prints out information in nice format.
# Information that is printed can be changed as desired. 
# @para playlist: json() information of playlist
# @return None 
def print_playlist_json_info(playlist):
    print("Today's Top 50 Hits Songs")
    print("-------------------------")

    count = 0
    for item in playlist["tracks"]["items"]:
        track = item["track"]

        # Avoid error if call to radio in playlist
        if track is not None:

            # Get all artists names in list
            artist_names = []
            for artist in track["artists"]:
                artist_names.append(artist["name"])

            print(count, ":", track["album"]["name"],)
            print("     by:", artist_names)
            print("     Add Date:", item["added_at"])
            print("     Popularity:", track["popularity"])
        count += 1
    return


def main():
    # Collect Items for Authentication
    CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
    SECRET_id = "487346bb76a54e05b308947a10a96ebe"
    access_token = get_access_token(CLIENT_id, SECRET_id)

    # Get playlist from spotify
    playlist_id = '37i9dQZF1DXcBWIGoYBM5M'   # Todays top hits 50
    playlist = get_playlist(playlist_id, access_token)

    # Create Dataframe from json file
    todayTopHitsdf = parse_playlist_to_dataframe(playlist)

    # Create Database with given information
    engine = create_engine('mysql://root:codio@localhost/spotify_music')
    todayTopHitsdf.to_sql('today_top_hits', con=engine,
                          if_exists='replace', index=True)


if __name__ == '__main__':
    main()
