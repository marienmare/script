import requests
from bs4 import BeautifulSoup

def get_info(key):
    if key.startswith('http'):
        r = requests.get(key)
    else:
        r = requests.get('https://pastebin.com/' + key)
    soup = BeautifulSoup(r.text, 'html.parser')
    metadataline = soup.find('div', class_='paste_box_line2')
    if metadataline.find('a') is None:
        user = 'guest'
    else:
        user = metadataline.find('a').text
    return {
        'date': parse(
            metadataline.find('span').attrs['title'],
            tzinfos = {'CDT': 'America/Mexico_City'}
    ),
    'user': user,
    'data': soup.find(id='paste_code').text
    }
