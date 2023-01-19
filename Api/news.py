import requests
from bs4 import BeautifulSoup

urls = [
    'https://sport.ua/uk',
    'https://www.ua-football.com/ua/sport'
    'https://sportarena.com/uk/'
]
translate = {
    'футбол': 'football',
    'теніс': 'tennis',
    'баскетбол': 'basketball',
    'хокей': 'hockey',
    'волейбол': 'volleyball',
    'бокс': 'boxing',
    'бейсбол': 'baseball',
    'біг': 'running',
    'біатлон': 'biathlon',
    'бадмінтон': 'badminton',
    'волейбол': 'volleyball',
    'гандбол': 'handball',
    'Спортивна гімнастика': 'gymnastics',
    'кікбоксінг': 'kickboxing',
    'керлинг': 'curling',
    'кіберспорт': 'cybersport',
    'легка атлетика': 'athletics',
    'моторспорт': 'automoto',
    'Авто/мото': 'automoto',
    'MMA': 'mma',
    'шахи': 'chess',
    'Фехтування': 'fencing',
    'Боротьба': 'wrestling',
    'війна': 'war',
    'ПРОЧИЕ': 'other',
    'КИБЕРСПОРТ': 'cybersport',
    'КЕРЛИНГ': 'curling',
    'биатлон': 'biathlon',
    'фехтование': 'fencing',
    'інші новини': 'other',
    'єдиноборства': 'wrestling',
    'автоспорт': 'automoto',
    'загальні новини': 'other',
    'інші види': 'other',
    'борьба': 'wrestling',
}


def get_news_1(url=urls[0]):
    news_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('div', class_='news-items').find_all('div', class_='item')
    for i in data:
        news = {}
        news['time'] = i.find('span', class_='item-date').text.strip()
        sport = i.find('span', class_='item-sport').text.casefold()
        news['sport'] = translate[sport]
        news['url'] = i.find('a').get('href')
        news['news'] = i.find('div', {'class': 'item-title'}).text.strip()
        news_list.append(news)
        print(news)
    return news_list


def get_news_2(url=urls[1]):
    news_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('div', class_='ContentList_content-list__list__Kp0X0')
    for i in data:
        news = {}
        news['time'] = i.find('div', {'class': 'NewsItem_news-item__text-wrapper__xiCs4'}).find('span').text.strip()
        sport = i.find('span', {'class': 'UiText_text__hN_oQ'}).text.casefold()
        news['sport'] = translate[sport]
        news['url'] = i.find('a').get('href')
        news['news'] = i.find('div', {'class': 'NewsItem_news-item__text-wrapper__xiCs4'}).find('a').text.strip()
        print(news)
        news_list.append(news)
    return news_list


def get_news_3(url=urls[2]):
    news_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('li', {'class': 'liga-news-item'})
    print(data)
    for i in data:
        news = {}
        news['time'] = i.find('span', {'class': 'time fz-12 mr-2'}).text.strip()
        sport = i.find('span', {'class': 'section-name fz-12'}).text.casefold()
        news['sport'] = translate[sport]
        news['url'] = i.find('a').get('href')
        news['news'] = i.find('span', {'class': 'fz-16 fw-500 d-block'}).text.strip()
        print(news)
        news_list.append(news)
    return news_list
