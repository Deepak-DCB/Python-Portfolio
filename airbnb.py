
import seaborn as sns
import pandas as pd


"""
Each commented out code is the code for printing out the boxplot, having more than one boxplot code causes them to overlap each other
"""

df = pd.read_csv("AB_NYC_2019.csv")

"""
prints boxplot 1, be sure to uncomment v.set function as well
"""
#v = sns.boxplot(x = 'neighbourhood_group', y = 'price', hue = 'room_type', data = df)
#v.set(ylim=(0, 400))

gdf = df.groupby(['host_id']).count()
gdf.sort_values('name', ascending=False)
gdf.head()

onedf = df.loc[df['host_id'] == 219517861]
twodf = df.loc[df['host_id'] == 107434423]

"""
prints second boxplot, vo = visual one
"""
#vo = sns.boxplot(x = 'minimum_nights', y = 'price', hue = 'room_type', data = onedf)


"""
prints third boxploxt, vt = visual two
"""
vt = sns.boxplot(x = 'minimum_nights', y = 'price', hue = 'room_type', data = twodf)
