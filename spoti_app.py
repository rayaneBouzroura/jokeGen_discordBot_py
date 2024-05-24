#import env
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
from datetime import datetime
#import pandas as pd

# Load env variabs from the .env file
load_dotenv()

# Fetch the client ID, client secret, and redirect URI from environment variables
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

#define scope of access
SCOPE = 'user-library-read playlist-modify-public'

# Fct to fetch the user's liked songs
def fetch_liked_songs():
    # auth and create the spotify object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=SCOPE))
    
    #Fetch liked songs
    results = sp.current_user_saved_tracks()

    #List to hold track info
    tracks = []

    #Loop through results and extract tracks info
    for items in results['items']:
        track = items['track']
        track_info = {
            'id': track['id'],
            'Name':track['name'],
            'Artist': ', '.join([artist['name'] for artist in track['artists']]),
            'Album': track['album']['name'],
            'Release Date': track['album']['release_date'],
            'Popularity': track['popularity']
        }
        tracks.append(track_info)
    return tracks
a = "2"



# Function to create a new playlist and add liked songs to it
def create_playlist_and_add_songs(tracks):
    # Authenticate and create the Spotify object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=SCOPE))
    
    # Get the current user's ID
    user_id = sp.current_user()['id']
    
    # Create a new playlist with the current date in the name
    playlist_name = f"likedSongsPlayList {datetime.now().strftime('%Y-%m-%d')}"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    
    # Extract the track IDs
    track_ids = [track['id'] for track in tracks]
    
    # Add the tracks to the new playlist
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)

    print(f"Created playlist '{playlist_name}' with {len(track_ids)} tracks.")




#launch app in main
if __name__ == '__main__':
    tracks = fetch_liked_songs()
    print("Fetched liked songs:", tracks)
    create_playlist_and_add_songs(tracks)
    print("Liked songs have been added to the new playlist.")

