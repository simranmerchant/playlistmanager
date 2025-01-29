# Spotify Playlist to Liked Songs Utility

A Python script that automatically transfers songs from your Spotify playlists to your Liked Songs collection.

## Features

- Fetches all tracks from your Spotify playlists
- Checks which songs aren't in your Liked Songs
- Automatically adds missing songs to Liked Songs
- Shows progress as songs are added
- Handles pagination for large playlists

## Prerequisites

- Python 3.6 or higher
- A Spotify Developer account
- Spotify API credentials (Client ID and Client Secret)

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install spotipy python-dotenv
```

3. Create a `.env` file in the project root and add your Spotify API credentials:
```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
```

4. Get your Spotify API credentials:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Copy the Client ID and Client Secret
   - Add `http://localhost:8888/callback` as a Redirect URI in your app settings

## Usage

Run the script:
```bash
python spotify_transfer.py
```

The script will:
1. Authenticate with your Spotify account
2. Fetch all your playlists
3. Compare playlist tracks with your Liked Songs
4. Add any missing songs to your Liked Songs
5. Display progress in the console

## Error Handling

- The script handles rate limiting and API timeouts
- Skips any null tracks or invalid entries
- Provides feedback for each operation

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.

## Security Notes

- Never commit your `.env` file
- Keep your Spotify API credentials secure
- Use the provided `.env.example` for reference
