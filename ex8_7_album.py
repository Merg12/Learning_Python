#write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist
#name and an album title, and it should return a dictionary 
#containing these 2 pieces of information. Use the function to make
#3 dictionaries representing different albums. Print each return
#value to show that the dictionaries are storing the album info
#correctly

#Add an optional parameter to make_album() that allows you to store
#the number of tracks on an album. If the calling line includes a
#value for the number of tracks, add that value to the album's
#dictionary. make at least one new function call that includes the
#number of tracks on an album

def make_album(artist_name, album_title, track_number = ''):
    artist_album = {'artist' : artist_name, 'album' : album_title}

    if track_number:
        artist_album['track'] = track_number

    return artist_album

album_mapped = make_album('enrique iglesias', 'love')
print(album_mapped)

album_mapped = make_album('taylor swift', 'more love', track_number = '21')
print(album_mapped)