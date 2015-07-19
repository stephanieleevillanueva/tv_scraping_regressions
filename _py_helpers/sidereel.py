import requests
from bs4 import BeautifulSoup

#variables:
#show_titles = list of shows, title only
#show_list = show name and genre

genres = ['action', 'cartoons', 'comedy', 'crime', 'drama', 'fantasy', 'reality', 'science-fiction']

show_list = []

for genre in genres:   
    url_list = ['http://www.sidereel.com/_television/genres/%s?page=A#letter_nav' % (genre),
            'http://www.sidereel.com/_television/genres/%s?page=D#letter_nav' % (genre),
            'http://www.sidereel.com/_television/genres/%s?page=H#letter_nav' % (genre),
            'http://www.sidereel.com/_television/genres/%s?page=L#letter_nav' % (genre),
            'http://www.sidereel.com/_television/genres/%s?page=P#letter_nav' % (genre),
            'http://www.sidereel.com/_television/genres/%s?page=T#letter_nav' % (genre),
            'http://www.sidereel.com/_television/genres/%s?page=V#letter_nav' % (genre)]
    
    for url in url_list:
        response = requests.get(url)
        page = response.text
        soup = BeautifulSoup(page, 'lxml')

        listing = soup.find_all(class_ = 'listing-section')

        for column in listing:
            for title in column.find_all('a'): 
                show = []
                show.append(title.text.encode('utf-8'))
                show.append(genre.title())
                show.append(title.get('href'))
                show_list.append(show)

show_titles = sorted([show[0] for show in show_list])