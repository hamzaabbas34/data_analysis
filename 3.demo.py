# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# def get_title(soul):
#     try:
#         title = soul.find('span' , attrs={'id': "productTitle"}).text.strip()
#         title_value = title.text
#         title_str = title_value.strip()
#     except AttributeError:
#         title_str = None
#     return title_str




# url = 'https://www.amazon.com/s?k=playstation+5&sprefix=play%2Caps%2C498&ref=nb_sb_ss_ts-doa-p_1_4'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-US , en;q=0.5'
# }

# website = requests.get(url=url, headers=headers)
# soup = BeautifulSoup(website.content, 'html.parser')
# links = soup.find_all("a", class_=["a-size-medium", "a-color-base", "a-text-normal"])

# all_links = []
# for link in links:
#         href = link.get('href')
#         all_links.append('http://amazon.com' + href)
# titles = []
# for   l  in all_links:
#     new_website = requests.get(l, headers=headers)
#     new_soup = BeautifulSoup(new_website.content, 'html.parser')
#     titles.append(get_title(new_soup))
# print(titles)

import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_title(soul):
    try:
        title = soul.find('span', attrs={'id': "productTitle"}).text.strip()
        print("succesfull")
        title_str = title.strip()
    except AttributeError:
        title_str = None
    return title_str
def get_prices(soul):
    try:
        price = soul.find('span', attrs={'class': "a-offscreen"}).string.strip()
    except AttributeError:
        price = None
    return price

def get_rating(soul):
    try:
        rating = soul.find("span" , atters={'class':"a-icon-alt"}).string.strip()
    except:
        rating = None


url = 'https://www.amazon.com/s?k=playstation+5&sprefix=play%2Caps%2C498&ref=nb_sb_ss_ts-doa-p_1_4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US , en;q=0.5'
}

website = requests.get(url=url, headers=headers)
soup = BeautifulSoup(website.content, 'html.parser')
links = soup.find_all("a", class_=["a-size-medium", "a-color-base", "a-text-normal"])

all_links = set()
for link in links:
    href = link.get('href')
    if href.startswith('/'):
        href = 'https://www.amazon.com' + href
    all_links.add(href)

all_links = list(all_links)
titles = []
prices = []
rating = []
for l in all_links:
    new_website = requests.get(l, headers=headers)
    new_soup = BeautifulSoup(new_website.content, 'html.parser')
    titles.append(get_title(new_soup))
    prices.append(get_prices(new_soup))
    rating.append(get_rating(new_soup))

print("Complete")
print(titles , prices , rating)
df = {'Title':titles , "prices":prices , 'Rating':rating}
df = pd.DataFrame(df)
print(df)
df.to_csv('scraped_data.csv', index=False)

# -------------------------------------------------------------------
# base_url = 'https://www.amazon.com/s'
# search_query = 'playstation+5'

# titles = []
# prices = []

# for page in range(1, 11):
#     params = {
#         'k': search_query,
#         'sprefix': 'play%2Caps%2C498',
#         'ref': f'nb_sb_ss_ts-doa-p_{page}_4'
#     }

#     website = requests.get(url=base_url, params=params, headers=headers)
# ------------------------------------------------------------------------