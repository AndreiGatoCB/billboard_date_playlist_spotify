from billboard_songs import HundredSongs
from date import Date
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

spotify_client_id = '157b1892c120463bb9efbf7f45cac455'
spotify_client_secret = '841ad71bf18a496bb07c7dee1bd070df'
spotify_url = 'https://acounts.spotify.com/api/token'
uri_spotify = 'https://example.com/callback'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri=uri_spotify,
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path='token.txt'
    )
)
user_id = sp.current_user()['id']
print('Bienvenido a la máquina del tiempo, acá encontrarás las 100 canciones más sonadas según los billboards en la '
      'fecha que ingreses. Empecemos.')

date = Date()
year = date.year()
month = date.month()
day = date.day()

song = HundredSongs(year, month, day)
songs = song.songs()
# print(songs)

artists = song.artists()
# print(artists)

last_year = (int(year) - 1)

track_data = []
track_ids = []
for id_ in range(100):
    track_data.append(sp.search(q=f'artist: {artists[id_]} track: {songs[id_]} year:{last_year or year}', type='track'))

# print(track_data)
for x in range(100):
    try:
        track_id_json_last_year = json.dumps(track_data[x]['tracks']['items'][0]['uri'])
        track_ids.append(track_id_json_last_year)
        # print(track_id_json_last_year)
    except IndexError:
        track_ids.append('')
# print(track_ids)
track_data_year = []
for id_ in range(100):
    track_data_year.append(sp.search(q=f'artist: {artists[id_]} track: {songs[id_]} year:{year}', type='track'))
track_ids_year = []
for x in range(100):
    try:
        track_id_json_year = json.dumps(track_data_year[x]['tracks']['items'][0]['uri'])
        track_ids_year.append(track_id_json_year)
        # print(track_id_json_year)
    except IndexError:
        track_ids_year.append('')
# print(track_ids)
# print(track_ids_year)
mixed = []
for i in range(100):
    mixed.append(track_ids_year[i])
    if i < 100:
        mixed.append(track_ids[i])

mixed2 = []
for x in range(100):
    if '"' in mixed[x]:
        mix = mixed[x].strip('"')
        mixed2.append(mix)

# print(mixed2)
end_mixed = list(dict.fromkeys(mixed2))
try:
    end_mixed.remove('')
except ValueError:
    pass
# print(end_mixed)
# print(len(end_mixed))

# for x in range(len(end_mixed)):

new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f'{year}-{month}-{day} Billboard 100',
    public=False,
)
# print(new_playlist['id'])

final_playlist = sp.playlist_add_items(
    playlist_id=new_playlist['id'],
    items=end_mixed
)

# print(type(final_playlist))
