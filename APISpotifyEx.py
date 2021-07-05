import requests
import spotipy
import os
import pandas as pd
from sqlalchemy import create_engine

# Gets access token to use spotify API
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


# Gets json playlist from spotify API
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


# Parses playlist json and gives DataFrame
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


# Create table in database based on given DataFrame
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

    
# Saves database information in file specified
# @para database: string name of database
# @para fileName: string name of file
# @return: None
def save_database_in_file(database, fileName):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + database + '; "')
    os.system("mysqldump -u root -pcodio " + database +
              " > " + fileName + ".sql")


# Load database from file to the current terminal
# @para database: string name of database
# @para fileName: string name of file
# @return: None
def load_database_from_file(database, fileName):
    os.system("mysql -u root -pcodio " + database + 
              " < " + fileName + ".sql")

# Make DataFrame from database table
# @para  database: string name of database
# @para     table: string name of table
# @return: DataFrame that is desired
def dataframe_from_table(database, table): 
    engine = create_engine('mysql://root:codio@localhost/' + database)
    return pd.read_sql_table(table, con=engine)
  
# @para database: string name of database
# @para    table: string name of table
# @return: None
def update_database_table(database, table)
    

# Handle user input to make interface of database manipulation understandable
# @para h: string dicating what string to print
# @return answer: int for response
def user_input(h)
    if (h == "menu"):
        print("Welcome! Do you wish to: \n" +
                       "   (1) - Update 'Today's Top Hits' database \n" +
                       "   (2) - Look at song in the current database \n" +
                       "   (3) - Look at search history \n" +
                       "   (0) - Exit")
    else:
        print("Give your input:")
    answer = input()
    return answer

# Handle user inputs to get song based on rank on "Todays Top Chartrs"
# @para:
# @return: when finished
def view_songs()
    num = 0
    while (num != ""):
        num = input("Choose what track to see based on ranking:")
        if (1 <= num and num <= 50):
            print_song_info(num)
            
        else if (num == ""):
            print("Quitting loop")
        else:
            print("Invlaid input")


def main():
    #Authentication Information
    CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
    SECRET_id = "487346bb76a54e05b308947a10a96ebe"
    access_token = get_access_token(CLIENT_id, SECRET_id)

    playlist_id = '37i9dQZF1DXcBWIGoYBM5M'   # Todays top hits 50
    playlist = get_playlist_json(playlist_id, access_token)

    todayTopHitsdf = playlist_json_to_dataframe(playlist)

    #User Input to manipulate database
    help_level = "menu"
    answer = user_input(help_level)
    
    while (answer is not 0):
        # Exit loop
        if (answer == 0):
            save_database_in_file('spotify_music','spotifyMusicFile')
            break

        # Update 'today_top_hits' playlist table        
        else if (answer == 1):
            create_database_table(todayTopHitsdf,'spotify_music','today_top_hits')
            save_database_in_file('spotify_music','spotifyMusicFile')
            print("Updated the file!")

        # Get song info           
        else if (answer == 2):
            print("Select song to view based on rank from 1-50, or click \n"
                  "and input nothing to quit current prompt")
            veiw_songs()

        #Look at search history
        else if (answer == 3):
            print("Here is search history of last 5 songs")
            print(dataframe_from_table('spotify_music', 
                                       'searchHistory').head())

        else:
            print("Bad input, please refer to the menu for correct input")
            help_level = "menu"

        answer = user_input(help_level)
        help_level = ""

    print("Thank you!")
        
if __name__ == '__main__':
    main()
