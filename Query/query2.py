
#SECOND PART
import sqlite3
import pandas as pd

#Creating database and its cursor
db = sqlite3.connect('energy.db')
cursor = db.cursor()

#reading in file, creating columns
energy = pd.read_csv('energy.csv')
energy.columns = ['year', 'state', 'source', 'mwh']

#writing to table, if table already exists, it will replace it
energy.to_sql('production', db, if_exists='replace', index=True)

#Returns list of sum of all solar and wind production by state, ordered by mwh so that you can find the max producers.
q = '''SELECT state, sum(mwh) FROM production WHERE source = 'Solar Thermal and Photovoltaic' OR source = 'Wind' GROUP BY state ORDER BY mwh DESC'''
print("MAXIMUM PRODUCERS OF SOLAR AND WIND ENERGY")
print(cursor.execute(q).fetchall())

print()
#Returns list of total solar and wind in the US by year, does not track state
q = '''SELECT year, source, mwh FROM production WHERE source= 'Solar Thermal and Photovoltaic' OR source = 'Wind' GROUP BY source, year ORDER BY year;'''
print("TOTAL SOLAR AND WIND PRODUCTION IN THE US BY YEAR")
print(cursor.execute(q).fetchall())


db.commit()
db.close()
