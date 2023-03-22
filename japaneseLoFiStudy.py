# Spotify playlist playback script

import spotipy
import spotipy.util as util
import os

# Get Client ID and client secret and username from environment variables
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
username = os.environ['SPOTIFY_USERNAME']

# Set scope for accessing user's library
scope = 'playlist-read-private user-modify-playback-state user-read-playback-state user-library-read'

# Redirect URI for token authorization
redirect_uri = 'http://localhost:8888/callback'

# Get access token for user
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, cache_path=None)

# Create Spotify object with access token
spotify = spotipy.Spotify(auth=token)

# Get computer device ID
devices = spotify.devices()
computer_device_id = None
for device in devices['devices']:
    if device['type'] == 'Computer':
        computer_device_id = device['id']
if computer_device_id is None:
    print('No active computer devices found.')
    exit()

# Set computer as active device
spotify.transfer_playback(computer_device_id, force_play=True)

# Search playlist by ID
playlist_id = '5QjgJ20xSbkyfDY2iPERtz'
playlist = spotify.playlist(playlist_id)
playlist_uri = playlist['uri']

# Start playback of playlist
spotify.start_playback(device_id=computer_device_id, context_uri=playlist_uri)
