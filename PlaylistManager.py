# spotify script to transfer songs in playlist to Liked Songs
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def setup_spotipy():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8888/callback'),
        scope='playlist-read-private,playlist-modify-private,user-library-read,user-library-modify'))
    return sp

def get_playlists(sp):
    playlists = sp.current_user_playlists()
    return playlists['items']   

def get_playlist_tracks(sp):
    playlists = get_playlists(sp)
    all_playlist_songs = []
    for playlist in playlists:
        current_playlist_songs = sp.playlist_items(playlist['id'])
        all_playlist_songs += current_playlist_songs['items']

    return all_playlist_songs

def get_liked_songs(sp):
    liked_songs = sp.current_user_saved_tracks()
    total_songs = liked_songs['total']  

    x = 0
    while x < total_songs:
        current_batch = sp.current_user_saved_tracks(limit=50, offset=x)
        liked_songs['items'] += current_batch['items']
        x += 50

    return liked_songs['items']


def compare_missing_and_add(sp, all_playlist_songs, liked_songs):
    for song in all_playlist_songs:
        if song not in liked_songs:
            if song['track'] is None:
                continue
            sp.current_user_saved_tracks_add([song['track']['id']])
            print(f"Added {song['track']['name']} to Liked Songs")
        else:
            print(f"{song['track']['name']} already in Liked Songs")

if __name__ == "__main__":
    sp = setup_spotipy()
    compare_missing_and_add(sp, get_playlist_tracks(sp), get_liked_songs(sp))



# Set up authentication
# Get all playlists
# Get all Liked Songs
# Compare and if not in Liked, add to Liked
# Show progress (playlist x/y)

# current_user()
# Get detailed profile information about the current user. An alias for the ‘me’ method.

# current_user_playlists(limit=50, offset=0)
# Get current user playlists without required getting his profile Parameters:
    # limit - the number of items to return
    # offset - the index of the first item to return

# playlist_add_items(playlist_id, items, position=None)
# Adds tracks/episodes to a playlist
    # Parameters:
    # playlist_id - the id of the playlist
    # items - a list of track/episode URIs or URLs
    # position - the position to add the tracks

# playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))
# Get full details of the tracks and episodes of a playlist.
    # Parameters:
    # playlist_id - the playlist ID, URI or URL
    # fields - which fields to return
    # limit - the maximum number of tracks to return
    # offset - the index of the first track to return
    # market - an ISO 3166-1 alpha-2 country code.
    # additional_types - list of item types to return.

# user_playlist_add_tracks(user, playlist_id, tracks, position=None)

# user_playlists(user, limit=50, offset=0)
# Gets playlists of a user
    # Parameters:
    # user - the id of the usr
    # limit - the number of items to return
    # offset - the index of the first item to return