from bs4 import BeautifulSoup
import requests
import re


class HundredSongs:

    def __init__(self, year, month, day):
        self.response = requests.get(f'https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/')
        self.billboard_100 = self.response.text
        self.soup = BeautifulSoup(self.billboard_100, 'html.parser')

    def songs(self):

        first_song = self.soup.find_all(name='h3', id='title-of-a-story',
                                        class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size'
                                               '-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-'
                                               'max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter'
                                               '-spacing-0028@tablet')
        # print(first_song)
        else_songs = self.soup.find_all(name='h3', id='title-of-a-story',
                                        class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font'
                                               '-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@'
                                               'mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')

        # print(first_song)
        # print(else_songs)

        songs = [song.getText() for song in first_song]
        for song in else_songs:
            songs.append(song.getText())
        # print((songs))

        songs_false = []
        songs_true = []
        for x in range(100):
            if '\n' and '\t' in songs[x]:
                song = re.sub('\n', '', songs[x])
                songs_false.append(song)
                song = re.sub('\t', '', songs_false[x])
                songs_true.append(song)
        # print(songs)
        # print(songs_false)
        return songs_true

    def artists(self):

        first_artist = self.soup.find_all(name='span',
                                          class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')

        else_artists = self.soup.find_all(name='span',
                                          class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')

        artists = [artist.getText() for artist in first_artist]
        for artist in else_artists:
            artists.append(artist.getText())

        artists_false = []
        artists_true = []
        for x in range(100):
            if '\n' and '\t' in artists[x]:
                artist = re.sub('\n', '', artists[x])
                artists_false.append(artist)
                artist = re.sub('\t', '', artists_false[x])
                artists_true.append(artist)
        return artists_true
