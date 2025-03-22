# Name: Miller Quintero
# Date: Mar 16, 2025
# Brief: Creating a tracks database (including genre) with SQLite3 using a ¡Tunes file CSV

import sqlite3

# First, create the database if it doesn't exist and connect to it
conn = sqlite3.connect('track_and_genre_db.sqlite')
# This is the cursor object to interact with the database
cur = conn.cursor()

# Make some fresh tables using executescript() that allow us to run SQL commands
# Our primary keys are the id columns and they are unique, furthermore, 
# since tha name is unique, it comes with autoincrement in the ID implicitly
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
                  
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# While loop until do a succesful file read
while True:
    name = input("Enter file name (It works with a CSV files of listened track from !Tunes): ")
    try:
        handle = open(name)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

""" There are these elements in each line of the CSV file for example :
    name, artist, album, count, rating, length, genre"""
# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
#   0                          1      2           3  4   5

for line in handle:
    line = line.strip();
    pieces = line.split(',')

    # If the tracks doesn't have all the elements, we skip it
    if len(pieces) < 6 :
        print(f"'{line}' skipped because it doesn't have all the elements")
        continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # Debygging line
    #print(name, artist, album, count, rating, length)

    # Inserting the data of artist in the database, and if it already exists, is omitted
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    # Since the artist is unique, we can get the id of the artist
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    # Inserting the data of album in the database, and if it already exists, is omitted
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    # Since the album is unique, we can get the id of the album
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    # Take the first row (actually it should always be just one for a unique album)
    album_id = cur.fetchone()[0]

    # Inserting the data of genre in the database, and if it already exists, is omitted
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    # Since the genre is unique, we can get the id of the genre
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    # Inserting the data of track in the database, and if it already exists, is omitted
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    # Commit the changes saved in program cache to the database
    conn.commit()

# After finish with the database creation, we will test with the following query

query = cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')

print(query.fetchall())