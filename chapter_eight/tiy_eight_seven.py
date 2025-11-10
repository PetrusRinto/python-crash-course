# Patrick 10.11.2025.
# 8-7 Album.

def make_album(artist_name, album_title, song_amount=None):
    """Storing album details in a dictionary."""
    music_album = {
        'artist': artist_name,
        'title': album_title,
        }

    if song_amount:
        music_album['songs'] = song_amount
    return music_album

album_1 = make_album('alan walker', 'different world', 10)
print(f"\n{album_1}")

album_2 = make_album('huntrix', 'k-pop demon hunters')
print(f"\n{album_2}")

album_3 = make_album('bruno mars', 'doo woops and hooligans', 11)
print(f"\n{album_3}")
