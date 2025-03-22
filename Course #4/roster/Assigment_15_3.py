# Name: Miller Quintero
# Date: Mar 17, 2025
# Brief: Creating a database from MOOC users and courses data in a JSON

import json
import sqlite3

# First, create the database if it doesn't exist and connect to it
conn = sqlite3.connect('assigment_roster_db.sqlite')
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
    role        INTEGER,
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
    role = data[2]

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
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES ( ?, ?, ? )''', (user_id, course_id, role))

    conn.commit()

cur.execute('''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;''')

query_data = cur.fetchall()

for tuple in query_data:
    print(f'{tuple[0]}|{tuple[1]}|{tuple[2]}')

cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;''')
print(cur.fetchall()[0][0])

# Close SQLite resources
cur.close()
conn.close()