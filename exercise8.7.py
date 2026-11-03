def make_album(artist, title, songs=None):
    """Bangun dictionary berisi informasi album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

print(make_album('Dewa 19', 'Pandawa Lima'))
print(make_album('Sheila on 7', 'Kisah Klasik untuk Masa Depan'))
print(make_album('Raisa', 'Heart to Heart'))
print(make_album('Kahitna', 'Permaisuriku', songs=10))