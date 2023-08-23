
#FIRST PART
import sqlite3
import pandas as pd

"""
READS CSV TO PANDAS DATAFRAME, THEN WRITES DATAFRAME INTO SQL DATABASE
"""

#Creating database and its cursor
d = sqlite3.connect('books.db')
cursor = d.cursor()

#reading in file, creating columns
pbooks = pd.read_csv('books.csv')
pbooks.columns = ['bookID', 'title', 'author', 'year']


#writing to table, if table already exists, it will replace it
pbooks.to_sql('books', d, if_exists='replace', index=False)


#simple query, displays all contents of table
q = '''SELECT * FROM books'''
p = cursor.execute(q).fetchall()

print(p)
print()
d.commit()
d.close()