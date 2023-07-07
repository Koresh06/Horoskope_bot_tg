from bs4 import BeautifulSoup
import requests
import json
import lxml



HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

ITEMS_DICT = {
    'Овен ♈': 'https://1001goroskop.ru/?znak=aries', 
    'Телец ♉': 'https://1001goroskop.ru/?znak=taurus',
    'Близнец ♊': 'https://1001goroskop.ru/?znak=gemini',
    'Рак ♋': 'https://1001goroskop.ru/?znak=cancer',
    'Лев ♈': 'https://1001goroskop.ru/?znak=leo',
    'Дева ♍': 'https://1001goroskop.ru/?znak=virgo',
    'Весы ♎': 'https://1001goroskop.ru/?znak=libra',
    'Скорпион ♐': 'https://1001goroskop.ru/?znak=scorpio',
    'Стрелец ♐': 'https://1001goroskop.ru/?znak=sagittarius',
    'Козерог ♑': 'https://1001goroskop.ru/?znak=capricorn',
    'Водолей ♒': 'https://1001goroskop.ru/?znak=aquarius',
    'Рыбы ♓': 'https://1001goroskop.ru/?znak=pisces',

}


def get_html(url):
    res = requests.get(url, headers=HEADERS)
    return res

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('div', class_='maincenter').find_all('p')

    items = items[:-1]
    res = []
    for item in items:
        res.append(item.get_text().strip())
           
    return(items)

