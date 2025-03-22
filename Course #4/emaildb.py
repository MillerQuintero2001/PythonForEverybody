# Name: Miller Quintero
# Date: Mar 15, 2025
# Brief: Creating a database with SQLite from a file

import sqlite3

# Connection to the database
conn = sqlite3.connect('emaildb.sqlite')
# Creation of the cursor object, this is the object to interact with the database
cur = conn.cursor()

# A clean creation of the table
cur.execute('DROP TABLE IF EXISTS Counts')

# Creation of the table
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# While loop until do a succesful file read
while True:
    name = input("Enter file name: ")
    try:
        fh = open(name)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

for line in fh:
    # Avoiding the lines that doesn't start with 'From: '
    if not line.startswith('From: '): continue

    # Analyzing the lines that start with 'From: ', we can get the email with this
    pieces = line.split()
    email = pieces[1]

    # This part here, is like doing a dictionary

    # First, we check if the email is already in the database
    # NOTE: The '?' is a placeholder for the email variable, it's a good practice to use it to avoid SQL injection
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    # # Take the first row (actually it should always be just one for a unique email address)
    row = cur.fetchone()
    # If the email is not in the database, we insert it in a new row with a count of 1
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    # Otherwise, we update the count of the email
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    # Commit the changes saved in program cache to the database
    conn.commit()

# https://www.sqlite.org/lang_select.html, query to get the top 10 emails (it already count the first one, so we get 9)
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Print top 10 emails
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])