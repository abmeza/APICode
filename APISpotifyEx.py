import requests
import spotipy
import os
import pandas as pd
from sqlalchemy import create_engine

# @para   cid: str value Client ID
# @para   sid: str value Secret ID
# @return token: str val of access token
#                None if unsuccessful
def get_access_token(cid, sid):
    token = None
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': sid,
    }) # Access token request

    if (response.status_code == 200):
        token = response.json()['access_token']
    return token


# @para            pid: str value Playlist ID
# @para   access_token: str value access token
# @return playlist: json() information of playlist
#                   None   if issue
def get_playlist_json(pid, access_token):
    playlist = None
    BASE_url = 'https://api.spotify.com/v1/playlists/'
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    response = requests.get(BASE_url + pid, headers=headers)

    if (response.status_code == 200):
        playlist = response.json()
    return playlist


# @para playlist: json() information of playlist
# @return playlist_df: pd.DataFrame of desired information from playlist
#                      empty DataFrame otherwise
def playlist_json_to_dataframe(playlist):
    playlist_df = pd.DataFrame()
    playlist_dict = {}
    count = 0   # track order of songs in playlist

    # Return empty playlist is empty
    if playlist is None:
        return playlist_df

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


# @para dataframe: DataFrame being converted
# @para  database: string name of database
# @para     table: string name of table
# @return: None
def create_database_table(dataframe, database, table): 
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + database + '; "')
    engine = create_engine('mysql://root:codio@localhost/' + database)
    dataframe.to_sql(table, con=engine,
                          if_exists='replace', index=True)

    
# @para database: string name of database
# @para fileName: string name of file
# @return: None
def save_database_in_file(database, fileName):
    os.system("mysqldump -u root -pcodio" + database +
              " > " + fileName + ".sql")


# @para database: string name of database
# @para fileName: string name of file
# @return: None
def load_database_from_file(database, fileName):
    os.system("mysql -u root -pcodio " + database +
              " < " + fileName + ".sql")
  

# @para database: string name of database
# @para    table: string name of table
# @return: None
# def update_database_table(database, table, )
  
  
def main():
    #Authentication Information
    CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
    SECRET_id = "487346bb76a54e05b308947a10a96ebe"
    access_token = get_access_token(CLIENT_id, SECRET_id)

    playlist_id = '37i9dQZF1DXcBWIGoYBM5M'   # Todays top hits 50
    playlist = get_playlist_json(playlist_id, access_token)

    todayTopHitsdf = playlist_json_to_dataframe(playlist)

    create_database_table(todayTopHitsdf,'spotify_music','today_top_hits')

    save_database_in_file('spotify_music','spotifyMusicFile')

if __name__ == '__main__':
    main()
