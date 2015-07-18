import requests
from bs4 import BeautifulSoup
from copy import deepcopy

url = 'http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2014-2015-season-33883/'
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, 'lxml')
main = soup.find(class_ = 'entry-content')

p = main.find_all('p')
index = 4
canceled_shows = []

for i in range(index, len(p)-3):
    title = []
    network = []
    temp = []
    try:
        title.append(p[i].find('strong').text.encode('utf-8'))
        network.append(p[i].contents[2].text.encode('utf-8'))
    except:
        title.append(p[i].find('a').text.encode('utf-8'))
        network.append(p[i].text.encode('utf-8'))
    temp.extend(title)  
    temp.extend(network)
    temp.append('Concluded')
    canceled_shows.append(temp)

canceled_shows[7][1] = canceled_shows[7][1].replace('', 'Adult Swim')
canceled_shows[9][1] = canceled_shows[9][1].replace('', 'Spike TV')
canceled_shows[14][1] = canceled_shows[14][1].replace('', 'syndicated')
canceled_shows[18][1] = canceled_shows[18][1].replace('', 'CNN')
canceled_shows[24][1] = canceled_shows[24][1].replace('', 'syndicated')
canceled_shows[25][1] = canceled_shows[25][1].replace('', 'TeenNick')
canceled_shows[27][1] = canceled_shows[27][1].replace('', 'Nickelodeon')
canceled_shows[29][1] = ''
canceled_shows[29][1] = canceled_shows[29][1].replace('', 'Fox')
canceled_shows[44][1] = canceled_shows[44][1].replace('', 'Disney')
canceled_shows[51][1] = canceled_shows[51][1].replace('', 'Nickelodeon')
canceled_shows[52][1] = canceled_shows[52][1].replace('', 'syndicated')
canceled_shows[58][1] = canceled_shows[58][1].replace('', 'El Rey')
canceled_shows[75][1] = canceled_shows[75][1].replace('', 'Disney')
canceled_shows[76][1] = canceled_shows[76][1].replace('', 'syndicated')
canceled_shows[81][1] = canceled_shows[81][1].replace('', 'Univision')
canceled_shows[82][1] = canceled_shows[82][1].replace('', 'CNN')
canceled_shows[91][1] = canceled_shows[91][1].replace('', 'CNBC')
canceled_shows[93][1] = canceled_shows[93][1].replace('', 'Pivot')
canceled_shows[95][1] = canceled_shows[95][1].replace('', 'CNN')
#canceled_shows

url_other = 'http://tvseriesfinale.com/tv-show/ending-or-cancelled-tv-shows-for-the-2013-14-season-30312/'
response_other = requests.get(url_other)
page_other = response_other.text
soup_other = BeautifulSoup(page_other, 'lxml')
content = soup_other.find(class_ = 'entry-content')
p_o = content.find_all('p')
index = 5
canc_shows_2014 = []

for i in range(index, len(p_o)-3):
    title = []
    network = []
    temp = []
    
    try:
        title.append(p_o[i].find('strong').text.encode('utf-8'))
        network.append(p_o[i].contents[2].text.encode('utf-8'))
    except:
        try:
            title.append(p_o[i].find('a').text.encode('utf-8'))
        except:
            title.append('')
        network.append(p_o[i].text.split(' ', 1)[0].encode('utf-8'))
    temp.extend(title)  
    temp.extend(network)
    temp.append('Concluded')
    canc_shows_2014.append(temp)

for show in canc_shows_2014:
    if len(show) != 3:
        if show[0] == show[1]:
            del show[1]
        if show[2] == '':
            del show[2]

    for i in range(len(show)):
        if show[i] == '':
            show[i] = show[i].replace('', 'N/A')

del canc_shows_2014[56]
del canc_shows_2014[95]
del canc_shows_2014[112]
            
#canc_shows_2014

url_other = 'http://tvseriesfinale.com/tv-show/ending-cancelled-tv-shows-2012-2013-24110/'
response_other = requests.get(url_other)
page_other = response_other.text
soup_other = BeautifulSoup(page_other, 'lxml')
content = soup_other.find(class_ = 'entry-content')
p_o = content.find_all('p')
index = 5
canc_shows_2013 = []

for i in range(index, len(p_o)-3):
    title = []
    network = []
    temp = []
    
    try:
        title.append(p_o[i].find('strong').text.encode('utf-8'))
        network.append(p_o[i].text.split('(', 1)[1].split(')')[0].encode('utf-8'))
    except:
        try:
            title.append(p_o[i].find('a').text.encode('utf-8'))
        except:
            title.append('')
        network.append(p_o[i].contents[2].text.encode('utf-8'))
    temp.extend(title)  
    temp.extend(network)
    temp.append('Concluded')
    canc_shows_2013.append(temp)
    
del canc_shows_2013[80]
    
#canc_shows_2013

url_list = ['http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2011-12-season-20684/',
            'http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2011-12-season-24069/',
            'http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2011-12-season-24071/']

page = 0
index = 6

canc_shows_2012 = []

for url in url_list:
    page += 1
    if page == 2:
        index = 5
    elif page != 2:
        index = 6
    url_other = url
    response_other = requests.get(url_other)
    page_other = response_other.text
    soup_other = BeautifulSoup(page_other, 'lxml')
    content = soup_other.find(class_ = 'entry-content')
    p_o = content.find_all('p')
        
    for i in range(index, len(p_o)-3):
        title = []
        network = []
        temp = []
        
        try:
            title.append(p_o[i].find('strong').text.encode('utf-8'))
            network.append(p_o[i].text.split('(', 1)[1].split(')')[0].encode('utf-8'))
        except:
            try:
                title.append(p_o[i].find('a').text.encode('utf-8'))
            except:
                title.append('')
            try:
                network.append(p_o[i].contents[2].text.encode('utf-8'))
            except:
                network.append('')
        temp.extend(title)  
        temp.extend(network)
        temp.append('Concluded')
        canc_shows_2012.append(temp)

#canc_shows_2012
url_list = ['http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2010-2011-18992/',
            'http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2010-2011-19604/',
            'http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2010-2011-19965/',
            'http://tvseriesfinale.com/tv-show/cancelled-tv-shows-2010-2011-19966/']

index = 4
canc_shows_2011 = []

for url in url_list:
    url_other = url
    response_other = requests.get(url_other)
    page_other = response_other.text
    soup_other = BeautifulSoup(page_other, 'lxml')
    content = soup_other.find(class_ = 'entry-content')
    p_o = content.find_all('p')
        
    for i in range(index, len(p_o)-3):
        title = []
        network = []
        temp = []
        try:
            title.append(p_o[i].find('strong').text.encode('utf-8'))
            network.append(p_o[i].text.split('(', 1)[1].split(')')[0].encode('utf-8'))
        except:
            try:
                title.append(p_o[i].find('a').text.encode('utf-8'))
            except:
                title.append('')
            try:
                network.append(p_o[i].contents[2].text.encode('utf-8'))
            except:
                network.append('')
        temp.extend(title)  
        temp.extend(network)
        temp.append('Concluded')
        canc_shows_2011.append(temp)
        
#canc_shows_2011

canceled_shows.extend(canc_shows_2014)
canceled_shows.extend(canc_shows_2013)
canceled_shows.extend(canc_shows_2012)
canceled_shows.extend(canc_shows_2011)

title = sorted([show[0] for show in canceled_shows])
