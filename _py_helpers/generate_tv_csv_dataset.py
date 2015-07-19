#Output:    data/tv.csv (tv dataset to be used for analysis)

import _py_helpers.sidereel #for show_list(title, genre, tag) and show_titles(title only) lists 
import _py_helpers.tvseriesfinale #for canceled_shows(title, network, status) and title(title only) lists
import _py_helpers.wikipediastate
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

def intersect(a, b):
     return list(set(a) & set(b))

def calLen(value):
    return len(value)

sidereel_titles = _py_helpers.sidereel.show_titles
finale_titles = _py_helpers.tvseriesfinale.title
inter = intersect(sidereel_titles, finale_titles) #tv show dataset

shows = [[show] for show in inter]
shows_cols = ['Title']
finale_df = pd.DataFrame(shows, columns=shows_cols) #tv show dataframe

show_list_norm = [] #normalized show title
for row in _py_helpers.sidereel.show_list:
    temp = []
    temp.append(row[0])
    temp.append(row[1])
    temp.append(row[2])
    temp.append(''.join(letter for letter in row[0] if letter.isalnum()).lower())
    show_list_norm.append(temp)
sidereel_cols = ['Title', 'Genre', 'Tag', 'Title_Norm']
sidereel_df = pd.DataFrame(show_list_norm, columns=sidereel_cols) #normalized show dataframe

show_genre_tag = pd.merge(finale_df, sidereel_df, on='Title', how='left')
show_genre_tag = show_genre_tag[show_genre_tag['Title'] != 'Stars Earn Stripe']
show_genre_tag.sort(['Title', 'Genre'], inplace=True)

###Webscraping with BeautifulSoup

tags = show_genre_tag['Tag'].tolist()
url = 'http://www.sidereel.com'
sidereel_data = []

for i in range(len(tags)):
    per = []
    response = requests.get(url + tags[i])
    page = response.text
    soup = BeautifulSoup(page, 'lxml')

    main = soup.find(class_ = 'tv-show-card-main')
    main_grid = main.find(class_ = 'row grid')
    main_grid_status = main_grid.find(class_ = 'country')

    #get title
    title = soup.find(class_ = 'title').text.strip().encode('utf-8')
    per.append(soup.find(class_ = 'title').text.strip().encode('utf-8'))
    #get seasons
    season = main_grid.find_all('span')[0].text.encode('utf-8')
    per.append(main_grid.find_all('span')[0].text.encode('utf-8'))
    #get episodes
    episode = main_grid.find_all('span')[1].text.encode('utf-8')
    per.append(main_grid.find_all('span')[1].text.encode('utf-8'))
    #get current_status
    try:
        current_status = main_grid_status.text.strip('\n').split(':')[1].encode('utf-8').strip()
        per.append(main_grid_status.text.strip('\n').split(':')[1].encode('utf-8').strip())
    except:
        per.append('Concluded')
    #get runtime
    try:
        runtime = main_grid.find(class_ = 'duration-data').text.encode('utf-8')
        per.append(main_grid.find(class_ = 'duration-data').text.encode('utf-8'))
    except:
        try:
            runtime = main_grid.find(class_ = 'airtime content airs').text.split('(')[1].split(')')[0].encode('utf-8')
            per.append(main_grid.find(class_ = 'airtime content airs').text.split('(')[1].split(')')[0].encode('utf-8'))
        except:
            per.append('None')
    #get rating
    try:
        user_rating = str(main.find(class_ = 'rating-group').find_all('meta')[1]).split('"')[1]
        per.append(str(main.find(class_ = 'rating-group').find_all('meta')[1]).split('"')[1])
    except:
        per.append(0.00)
    
    sidereel_data.append(per)

sidereel_data_cols = ['Title', 'Seasons', 'Episodes', 'Status', 'Duration', 'UserRating']
sidereel_data_df = pd.DataFrame(sidereel_data, columns=sidereel_data_cols).drop_duplicates() #sidereel data dataframe

#merge title dataset with sidereel data
tv_df = pd.merge(show_genre_tag, sidereel_data_df, on='Title', how='left')

series_finale = [[show[0], show[1]] for show in _py_helpers.tvseriesfinale.canceled_shows]
cols_sf = ['Title', 'Network']
series_finale_df = pd.DataFrame(series_finale, columns=cols_sf).drop_duplicates() #finale data frame

#merge dataset with finale data
tv_df = pd.merge(tv_df, series_finale_df, on='Title', how='left').drop_duplicates()

show_state_norm = []
for row in _py_helpers.wikipediastate.show_state:
    temp = []
    temp.append(row[0])
    temp.append(row[1])
    temp.append(''.join(letter for letter in row[0] if letter.isalnum()).lower())
    show_state_norm.append(temp)
wiki_cols = ['Title', 'State', 'Title_Norm']
wiki_state_df = pd.DataFrame(show_state_norm, columns=wiki_cols) #wikipedia data frame

tv_df = pd.merge(tv_df, wiki_state_df, on='Title_Norm', how='left', suffixes=('_SR', '_Wiki'))
tv_df = tv_df.where((pd.notnull(tv_df)), None)
tv_df.to_csv('data/tv.csv')