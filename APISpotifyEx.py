import requests
import spotipy
import os
import pandas as pd
from sqlalchemy import create_engine
import matplotlib
import matplotlib.pyplot as plt


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
    })   # Access token request

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
# @para    exists: string of if exists paramater, default 'replace'
# @return: None
def create_database_table(dataframe, database, table, exists):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + database + '; "')
    engine = create_engine('mysql://root:codio@localhost/' + database)
    if (exists == 'append'):
        dataframe.to_sql(table, con=engine,
                         if_exists=exists, index=True)
    else:
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


# Handle user input to make interface of database manipulation understandable
# @para h: string dicating what string to print
# @return answer: int for response
def user_input(h):
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


# Handles inspection info of songs in database, and stores in search history
# database as reference
# @para: none
# @return: when finished
def view_songs():
    num = 100
    df = dataframe_from_table('spotify_music', 'today_top_hits')
    history = dataframe_from_table('spotify_music', 'search_history')

    print("Select song to view based on rank from 1-50, or \n"
          "input 0 to quit current prompt")
    while (num != 0):
        num = int(input("Choose what track to see based on ranking:"))
        if (1 <= num and num <= 50):
            print(df.iloc[[num-1]])
            history = pd.concat([df.iloc[[num-1]], history])
        elif (num == 0):
            print("Quitting loop")
        else:
            print("Invalid input")
    create_database_table(history, 'spotify_music', 'search_history',
                          'replace')


# Function to hold user interface that allows for the manipulation
# of tracks from the given spotify playlist
# @para dataframe: dataframe of input playlist
# @return: when finished
def user_interface_playlist_viewer(dataframe):
    help_level = "menu"
    answer = user_input(help_level)

    # Create table if they do not exist to avoid errors
    create_database_table(pd.DataFrame(), 'spotify_music',
                          'search_history', 'append')
    create_database_table(pd.DataFrame(), 'spotify_music',
                          'today_top_hits', 'append')

    while (answer is not 0):
        # Exit loop
        if (answer == '0'):
            save_database_in_file('spotify_music', 'spotifyMusicFile')
            break

        # Update 'today_top_hits' playlist table
        elif (answer == '1'):
            create_database_table(dataframe, 'spotify_music',
                                  'today_top_hits', 'replace')
            save_database_in_file('spotify_music', 'spotifyMusicFile')
            print("Updated the file!")

        # Get song info
        elif (answer == '2'):
            view_songs()

        # Look at search history
        elif (answer == '3'):
            print("Here is search history of last 5 songs")
            print(dataframe_from_table('spotify_music',
                                       'search_history').head())

        else:
            print("Bad input, please refer to the menu for correct input")
            help_level = "menu"

        answer = user_input(help_level)
        help_level = ""
    print("Thank you!")


# Creates plot that compares a songs 'popularity' field to the ranking
# it has on the playlist chart from 1 as best to 50 as lowest
# @para         x: array of x-axis values
# @para       x_l: string of x-axis value
# @para         y: array of y-axis values
# @para       y_l: string of y-axis value
# @para     title: string title of plot
# @para dataframe: dataframe of input data
# @return: when finished
def popularity_scatter(x, x_l, y, y_l, title):
    fig = plt.figure()
    scatter = fig.add_subplot()
    scatter.scatter(x=x, y=y)
    scatter.set_xlabel(x_l)
    scatter.set_ylabel(y_l)
    scatter.set_title(title)
    plt.show()


def main():
    # Authentication Information
    CLIENT_id = "2b1a105e0bf94d69924ed5789171693f"
    SECRET_id = "487346bb76a54e05b308947a10a96ebe"
    access_token = get_access_token(CLIENT_id, SECRET_id)

    playlist_id = '37i9dQZF1DXcBWIGoYBM5M'   # Todays top hits 50
    playlist = get_playlist_json(playlist_id, access_token)

    todayTopHitsdf = playlist_json_to_dataframe(playlist)

    # User Input to manipulate database
    # user_interface_playlist_viewer(todayTopHitsdf)

    # popularity_scatter(todayTopHitsdf['Popularity'], 'Popularity Rank',
    #                   list(range(1,51)), 'Chart Rank',
    #                   'Song Popularity Based On Ranking')
    #
    # Extracting statistical Info
    print(todayTopHitsdf.head())
    print(todayTopHitsdf["Popularity"].mean())


if __name__ == '__main__':
    main()
