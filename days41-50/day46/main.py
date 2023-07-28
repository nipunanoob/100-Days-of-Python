import os
import pprint
import requests
import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIFY_REDIRECT_URI')


def get_past_date():
    try:
        songDate = input("Enter the year you would like to travel back to? Enter in YYYY-MM-DD:")
        datetime.date.fromisoformat(songDate)
    except ValueError:
        raise ValueError("Date not entered in YYYY-MM-DD format")
    return songDate


def scrape_top_100_billboard(songDate):
    URL = "https://www.billboard.com/charts/hot-100/" + songDate
    response = requests.get(URL, "lxml")
    webpage = response.text

    soup = BeautifulSoup(webpage, features="lxml")
    songTitlesTags = soup.select("li > #title-of-a-story")
    songTitles = []
    for songTitle in songTitlesTags:
        songTitles.append(songTitle.text.strip())
    return songTitles


def get_song_uri(song_name, songDate):
    songYear = int(songDate[:4]) 
    results = sp.search(q=f"track:{song_name}",
                        type='track', limit=10)
    # Check if there are any search results
    if results['tracks']['items']:
         # Filter the results to only include songs from the specified year
        filtered_results = [
            track for track in results['tracks']['items'] 
            if songYear-3 <= int(track['album']['release_date'][:4]) <= songYear+3
        ]
        if filtered_results:
            song_uri = results['tracks']['items'][0]['uri']
            return song_uri
        else:
            print(f"{song_name} not found in Spotify") 
    else:
        print(f"{song_name} not found in Spotify")  
    return None



def get_song_uri_top_100_billboard(songList, songDate):
    songURIList = []
    for song in songList:
        songURI = get_song_uri(song, songDate)
        if songURI == None:
            continue
        songURIList.append(songURI)
    return songURIList
         

songDate = get_past_date()
songList = scrape_top_100_billboard(songDate)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private"))
songURIList = get_song_uri_top_100_billboard(songList, songDate)
spotify_user = sp.current_user()['id']
playlist = sp.user_playlist_create(spotify_user, f"{songDate} Billboard 100", public=False)
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(songURIList)

sp.user_playlist_add_tracks(spotify_user, playlist['id'], songURIList, position=None)
print(f"Playlist created {playlist['id']}")

