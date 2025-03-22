# Name: Miller Quintero
# Date: Mar 17, 2025
# Brief: Creating a database from MOOC users and courses data in a JSON

import json
import sqlite3

# First, create the database if it doesn't exist and connect to it
namedb = str(input("Please enter your database name: "))+'.sqlite'
conn = sqlite3.connect(namedb)
# This is the cursor object to interact with the database
cur = conn.cursor()

# Make some fresh tables using executescript() that allow us to run SQL commands
# Our primary keys are the id columns and they are unique, furthermore,
# since tha name is unique, it comes with autoincrement in the ID implicitly
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
    name    TEXT UNIQUE              
);
                  
CREATE TABLE Course(
    id      INTEGER NOT NULL PRIMARY KEY UNIQUE,
    title   TEXT UNIQUE              
);
                  
CREATE TABLE Member(
    user_id     INTEGER,
    course_id   INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# While loop until do a succesful file read
while True:
    try:
        name = input("Enter file name (It works with JSON files): ")
        # Get full of JSON file as a single string
        json_text = open(name).read()
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

# Parse it with JSON library
json_data = json.loads(json_text)
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

for data in json_data:
    user = data[0]
    title = data[1]

    # Insert and manage user data
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (user, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (user, ))
    user_id = cur.fetchone()[0]

    # Insert and manage course data
    cur.execute('''INSERT OR IGNORE INTO Course (title)
    VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # Insert data into Member table
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id)
        VALUES ( ?, ? )''', (user_id, course_id))

    conn.commit()