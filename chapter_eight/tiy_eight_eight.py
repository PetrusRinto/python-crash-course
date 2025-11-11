# Patrick 11.11.2025.
# 8-8 User Albums.

def make_album(artist_name, album_title, song_amount=None):
    """Storing album details in a dictionary."""
    music_album = {
        'artist': artist_name,
        'title': album_title,
        }

    if song_amount:
        music_album['songs'] = song_amount
    return music_album

albums = []

enter_album = True

while enter_album:
    print("\nThink of an album and enter the following:")
    print("(enter 'q' at any time to quit)")

    artist = input("Name of the artist: ")
    if artist == 'q':
        break
    
    title = input("Name of the album: ")
    if title == 'q':
        break

    songs_question = input(
        f"Do you know how many songs there is in {title.title()}? (yes / no) "
        )
    if songs_question == 'no':
        songs = None
        enter_album = False
    elif songs_question == 'q':
        break
    else:
        songs = input("Number of songs: ")
        enter_album = False

album = make_album(artist, title, songs)
print("\nA new album was created:")
print(f"{album}\n")
