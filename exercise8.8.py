def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\n(ketik 'q' kapan saja untuk keluar)")
    artist = input("Nama artis: ")
    if artist == 'q':
        break
    title = input("Judul album: ")
    if title == 'q':
        break
    print(make_album(artist, title))