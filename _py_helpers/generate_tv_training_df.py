#Output:	tv_df (tv dataset dataframe)


import csv
import math
import pandas as pd

def calLen(value):
    return len(value)

with open('data/tv.csv') as train:
    reader = csv.reader(train)
    tv = [row for row in reader]
del tv[0]

#remove rows with 0 value in seasons and user rating
tv = [x for x in tv if (x[9] != '0.0')] 
tv = [x for x in tv if (x[5] != '0')]

#convert seasons, episodes, user rating to float/int
#add a new column SeasonsLog
for title in tv:
    title[5] = float(title[5])
    title[6] = int(title[6])
    title[9] = float(title[9])
    title.append(math.log(title[5]))

#create dataframe object
cols = ['Ind', 'Title_SR', 'Genre', 'Tag', 'Title_Norm', 'Seasons', 'Episodes', 'Status', 'Duration', 'UserRating', 'Network', 'Title_Wiki', 'State', 'SeasonsLog']
tv_df = pd.DataFrame(tv, columns=cols)
tv_df['Network_Count'] = tv_df['Network'].apply(calLen)
tv_df = tv_df[tv_df['Network_Count'] <= 15]
tv_df.sort(['UserRating'], inplace=True)